import requests


class DistanceMatrix:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_distance(self, from_location, to_location):
        # Define the parameters
        origins = from_location
        destinations = to_location
        units = 'imperial'

        # Construct the request URL
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destinations}&units={units}&key={self.api_key}"

        # Make the request to Google Maps Distance Matrix API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            return f"Error: Unable to fetch data (status code: {response.status_code})"

        data = response.json()

        # Check if the response contains the expected data
        try:
            if 'rows' in data and data['rows']:
                distance_str = f"Distance between {origins} and {destinations} is: {data['rows'][0]['elements'][0]['distance']['text']}"
                return (distance_str, data)
            else:
                return "Error: No distance data available for the provided locations."
        except Exception as e:
            print(e)
            
            

class GetLatLong:
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def geocode_lat_long(self,postal_code):
        geo_postal_code = postal_code
                # Construct the request URL
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={postal_code}&key={self.api_key}"

        # Make the request to Google Maps Distance Matrix API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            return f"Error: Unable to fetch data (status code: {response.status_code})"

        data = response.json()
        
        
        # Check if the response contains the expected data
        try:
            if data['status'] == 'OK':
                # Get the latitude and longitude from the response
                location = data['results'][0]['geometry']['location']
                latitude = location['lat']
                longitude = location['lng']
                #print(f"Latitude: {latitude}, Longitude: {longitude}")
                return latitude,longitude
            else:
                print("No results found or an error occurred.")
        except Exception as e:
            print(e)
        
        


class Places_Water:
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def find_places_water(self,latitute, longitute):
        
        lat, lng = latitute, longitute
        radius= 5000
        keyword= ["beach", "lake" ,"river"]
        placetype ="natural_feature"
        
        try:
            for key in keyword:
                #url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword={key}&location={lat}%2C{lng}&radius={radius}&key={API_KEY}"
                url2 = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword={key}&location={lat}%2C{lng}&type={placetype}&radius={radius}&key={self.api_key}"
                response = requests.get(url2)
                data = response.json()
                print(f'\nWATER FOUND found in radius of {radius} for Latitude Longitude is : {latitute, longitute}\n')
                
                for place in data["results"]:
                    print(place["name"], place['types'])
                
                return len(data["results"])
        except Exception as e:
            print(e)
            


class Places_FireStation:
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def find_places_firestation(self,latitute, longitute):
        
        lat, lng = latitute, longitute
        radius= 1000  #KEEP THIS SMALL meters
        placetype ="fire_station"
        
        try:
            url2 = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&type={placetype}&radius={radius}&key={self.api_key}"
            response = requests.get(url2)
            data = response.json()
            print(f'\nFIRESTATIONS found in radius of {radius} for Latitude Longitude is : {latitute, longitute}\n')
            
            for place in data["results"]:
                print(place["name"], place['types'])
            
            return len(data["results"])
        except Exception as e:
            print(e)
 
 
            
class Places_Hospital:
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def find_places_hospital(self,latitute, longitute):
        
        lat, lng = latitute, longitute
        radius= 2000  #KEEP THIS SMALL meters
        placetype ="hospital"
        
        try:
            url2 = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&type={placetype}&radius={radius}&key={self.api_key}"
            response = requests.get(url2)
            data = response.json()
            print(f'\nHOSPITALS found in radius of {radius} for Latitude Longitude is : {latitute, longitute}\n')
            
            for place in data["results"]:
                print(place["name"], place['types'])
            
            return len(data["results"])
        except Exception as e:
            print(e)
            


class Places_Police:
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def find_places_police(self,latitute, longitute):
        
        lat, lng = latitute, longitute
        radius= 2000  #KEEP THIS SMALL meters
        placetype ="police"
        
        try:
            url2 = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&type={placetype}&radius={radius}&key={self.api_key}"
            response = requests.get(url2)
            data = response.json()
            print(f'\nPOLICE STATION found in radius of {radius} for Latitude Longitude is : {latitute, longitute}\n')
            
            for place in data["results"]:
                print(place["name"], place['types'])
            
            return len(data["results"])
        except Exception as e:
            print(e)
            
            

class Places_SuperMarket:
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def find_places_supermarket(self,latitute, longitute):
        
        lat, lng = latitute, longitute
        radius= 500  #KEEP THIS SMALL meters
        placetype ="supermarket"
        
        try:
            url2 = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&type={placetype}&radius={radius}&key={self.api_key}"
            response = requests.get(url2)
            data = response.json()
            print(f'\nSUPERMARKET found in radius of {radius} for Latitude Longitude is : {latitute, longitute}\n')
            
            for place in data["results"]:
                print(place["name"], place['types'])
            
            return len(data["results"])
        except Exception as e:
            print(e)
            

class SeverWeatherAlerts:
    
    def __init__(self) -> None:
        pass 
    
    def get_alerts_states(self,state):
        alert_state= state
        url2=f'https://api.weather.gov/alerts/active?area={alert_state}'
        try: 
            response = requests.get(url2)
            print(response)
            data = response.json()
            print(data['features'][0]['properties']['severity'])
            print(data['features'][0]['properties']['urgency'])
            return len(data['features'])
        except Exception as e:
            print("None found",e)
            pass