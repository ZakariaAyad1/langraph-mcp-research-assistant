"""Local SQLite storage - completely free."""
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
from config import settings

class StorageTool:
    """Local SQLite database for storing research and tasks."""
    
    def __init__(self):
        self.db_path = settings.DB_PATH
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_database()
    
    def _init_database(self):
        """Initialize database tables."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Research sessions
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                summary TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Search results
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER,
                title TEXT,
                url TEXT,
                snippet TEXT,
                FOREIGN KEY (session_id) REFERENCES sessions (id)
            )
        """)
        
        # Tasks
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER,
                description TEXT NOT NULL,
                deadline TEXT,
                priority TEXT DEFAULT 'medium',
                status TEXT DEFAULT 'pending',
                FOREIGN KEY (session_id) REFERENCES sessions (id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def create_session(self, topic: str) -> int:
        """Create new research session."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sessions (topic) VALUES (?)", (topic,))
        session_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return session_id
    
    def save_results(self, session_id: int, results: List[Dict[str, Any]]):
        """Save search results."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        for result in results:
            cursor.execute(
                "INSERT INTO results (session_id, title, url, snippet) VALUES (?, ?, ?, ?)",
                (session_id, result.get('title'), result.get('url'), result.get('snippet'))
            )
        
        conn.commit()
        conn.close()
    
    def save_summary(self, session_id: int, summary: str):
        """Save research summary."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE sessions SET summary = ? WHERE id = ?", (summary, session_id))
        conn.commit()
        conn.close()
    
    def save_tasks(self, session_id: int, tasks: List[Dict[str, Any]]):
        """Save extracted tasks."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        for task in tasks:
            cursor.execute(
                "INSERT INTO tasks (session_id, description, deadline, priority) VALUES (?, ?, ?, ?)",
                (session_id, task.get('description'), task.get('deadline'), task.get('priority', 'medium'))
            )
        
        conn.commit()
        conn.close()
    
    def get_all_sessions(self) -> List[Dict[str, Any]]:
        """Get all research sessions."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sessions ORDER BY created_at DESC")
        sessions = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return sessions
    
    def get_session_tasks(self, session_id: int) -> List[Dict[str, Any]]:
        """Get tasks for a session."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE session_id = ?", (session_id,))
        tasks = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return tasks

# Global instance
storage_tool = StorageTool()
