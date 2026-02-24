"""Free web search tools - No API keys or credit cards required."""
from typing import List, Dict, Any
from duckduckgo_search import DDGS
import wikipediaapi

class FreeWebSearchTool:
    """Free web search using DuckDuckGo and Wikipedia."""
    
    def __init__(self):
        self.ddg = DDGS()
        self.wiki = wikipediaapi.Wikipedia('AI-Research-Assistant/1.0', 'en')
    
    def search_web(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """
        Search the web using DuckDuckGo (completely free).
        
        Args:
            query: Search query
            max_results: Maximum results to return
            
        Returns:
            List of search results with title, url, snippet
        """
        try:
            results = []
            ddg_results = self.ddg.text(query, max_results=max_results)
            
            for item in ddg_results:
                results.append({
                    'title': item.get('title', ''),
                    'url': item.get('href', ''),
                    'snippet': item.get('body', '')
                })
            
            return results
        except Exception as e:
            print(f"DuckDuckGo search error: {e}")
            return []
    
    def search_wikipedia(self, query: str) -> Dict[str, Any]:
        """
        Search Wikipedia for detailed information.
        
        Args:
            query: Topic to search
            
        Returns:
            Wikipedia article summary and URL
        """
        try:
            page = self.wiki.page(query)
            
            if page.exists():
                return {
                    'title': page.title,
                    'url': page.fullurl,
                    'summary': page.summary[:500],
                    'full_text': page.text[:2000]
                }
            else:
                return {'title': query, 'summary': 'No Wikipedia article found', 'url': ''}
        except Exception as e:
            print(f"Wikipedia search error: {e}")
            return {'title': query, 'summary': 'Error accessing Wikipedia', 'url': ''}
    
    def comprehensive_search(self, query: str, max_results: int = 5) -> Dict[str, Any]:
        """
        Perform comprehensive search using both DuckDuckGo and Wikipedia.
        
        Args:
            query: Search query
            max_results: Max web results
            
        Returns:
            Combined search results
        """
        web_results = self.search_web(query, max_results)
        wiki_result = self.search_wikipedia(query)
        
        return {
            'query': query,
            'web_results': web_results,
            'wikipedia': wiki_result,
            'total_sources': len(web_results) + (1 if wiki_result.get('summary') else 0)
        }

# Global instance
search_tool = FreeWebSearchTool()
