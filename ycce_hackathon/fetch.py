import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API = os.getenv("OPENWEATHER_API_KEY")

# ------------------------
# Get coordinates from lat/lon (or city fallback)
# ------------------------
def get_coordinates(city=None, lat=None, lon=None):
    """
    Returns (lat, lon) for a city or uses provided lat/lon directly.
    """
    if lat is not None and lon is not None:
        return float(lat), float(lon)
    
    if not city or city.strip() == "":
        raise ValueError("City name cannot be empty if lat/lon are not provided.")
    
    city = city.strip()
    query = f"{city}, India"
    url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).json()
    
    if not r:
        raise ValueError(f"City '{city}' not found. Please enter a valid city name.")
    
    return float(r[0]["lat"]), float(r[0]["lon"])

# ------------------------
# Weather API
# ------------------------
def get_weather(city=None, lat=None, lon=None):
    lat, lon = get_coordinates(city, lat, lon)
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API}&units=metric"
    r = requests.get(url).json()
    
    if "main" not in r:
        raise ValueError(f"Weather data not found. Response: {r}")
    
    return {
        "lat": lat,
        "lon": lon,
        "temp": r["main"]["temp"],
        "humidity": r["main"]["humidity"],
        "rain": r.get("rain", {}).get("1h", 0)
    }

# ------------------------
# Soil API
# ------------------------
def get_soil(city=None, lat=None, lon=None):
    lat, lon = get_coordinates(city, lat, lon)
    url = f"https://rest.isric.org/soilgrids/v2.0/properties/query?lon={lon}&lat={lat}"
    r = requests.get(url).json()
    
    if "properties" not in r or "layers" not in r["properties"]:
        raise ValueError(f"Soil data not found. Response: {r}")
    
    soil = r["properties"]["layers"]
    return {
        "soil_ph": soil[0]["depths"][0]["values"],      # pH at 0–5cm
        "soil_carbon": soil[1]["depths"][0]["values"]   # Organic Carbon at 0–5cm
    }