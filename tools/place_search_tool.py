import os

from numpy import place
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup the place search tools and return a list of tools."""

        @tool
        def search_attraction(place: str) -> List:
            """Search for attractions in a given location."""
            try:
                attraction_result = self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    return f"Attractions found: {attraction_result}"
                
            except Exception as e:
                tavily_result = self.tavily_search.search_attractions(place)
                return tavily_result

        @tool
        def search_restaurant(place: str) -> str:
            """Search for restaurants in a given location."""

            try:
                restaurants_result = self.google_places_search.google_search_restaurants(place)
                if restaurants_result:
                    return f"Restaurants found: {restaurants_result}"

            except Exception as e:
                tavily_result = self.tavily_search.search_restaurants(place)
                return tavily_result
            
        @tool
        def search_activity(place: str) -> str:
            """Search for activities in a given location."""

            try:
                activity_result = self.google_places_search.google_search_activity(place)
                if activity_result:
                    return f"Activities found: {activity_result}"

            except Exception as e:
                tavily_result = self.tavily_search.search_activity(place)
                return tavily_result

        @tool
        def search_transportation(place: str) -> str:
            """Search for transportation options in a given location."""

            try:
                transportation_result = self.google_places_search.google_search_transportation(place)
                if transportation_result:
                    return f"Transportation options found: {transportation_result}"

            except Exception as e:
                tavily_result = self.tavily_search.search_transportation(place)
                return tavily_result

        return [search_attraction, search_restaurant, search_activity, search_transportation]
    
    