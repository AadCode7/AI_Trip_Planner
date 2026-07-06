import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper

class GooglePlaceSearchTool:
    def __init__(self, api_key: str):
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        self.places_tool = GooglePlacesTool(api_wrapper = self.places_wrapper)

    def google_search_attractions(self, place: str) -> dict:
        """Search for attractions in a given place using Google Places API."""
        return self.places_tool.run(f"Top attractions in and around {place}")
    
    def google_search_restaurants(self, place: str) -> dict:
        """Search for restaurants in a given place using Google Places API."""
        return self.places_tool.run(f"Top restaurants in and around {place}")

    def google_search_activity(self, place: str) -> dict:
        """Search for activities in a given place using Google Places API."""
        return self.places_tool.run(f"Top activities in and around {place}")
    
    def google_search_transportation(self, place: str) -> dict:
        """Search for transportation options in a given place using Google Places API."""
        return self.places_tool.run(f"Transportation options in and around {place}")
    

class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        """Search for attractions in a given place using Tavily Search API."""
        
        tavily_tool = TavilySearch(topic = 'general', include_answer = 'advance')
        result = tavily_tool.invoke({"query": f"Top attractions in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        else:
            return result

    def tavily_search_restaurants(self, place: str) -> dict:
        """Search for restaurants in a given place using Tavily Search API."""
        tavily_tool = TavilySearch(topic = 'general', include_answer = 'advance')
        result = tavily_tool.invoke({"query": f"Top 10 restaurants in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        else:
            return result
        
    def tavily_search_activity(self, place: str) -> dict:
        """Search for activities in a given place using Tavily Search API."""
        tavily_tool = TavilySearch(topic = 'general', include_answer = 'advance')
        result = tavily_tool.invoke({"query": f"Top activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        else:
            return result
        
    def tavily_search_transportation(self, place: str) -> dict:
        """Search for transportation options in a given place using Tavily Search API."""
        tavily_tool = TavilySearch(topic = 'general', include_answer = 'advance')
        result = tavily_tool.invoke({"query": f"Transportation options in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        else:
            return result
        
    