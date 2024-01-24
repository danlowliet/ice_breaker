from langchain.serpapi import SerpAPIWrapper
from langchain_community.utilities import SerpAPIWrapper


#using the SerpAPIWrapper method to go over the fluff and get the LinkedIn url
def get_profile_url(text: str) -> str:
    """Searches for LinkedIn Profile Page."""
    search = SerpAPIWrapper()
    res = search.results(f"{text}")
    return res["organic_results"][0]["link"]
