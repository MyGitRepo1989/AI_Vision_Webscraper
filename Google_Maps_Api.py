
import Google_Maps_helper
from Google_Maps_helper import *


#DISTANCE MATRIX API
api_key_dm = 'XXXXXXXXXXX'
distance= DistanceMatrix(api_key_dm)
distance_str, data = distance.get_distance("Toronto", "New York")
print(f'\n{distance_str}\nFull Response: {data}\n')


##GEOCODE API GLOBAL LATITUDE LONGITUDE
api_key_geo= 'XXXXXXXXXXX'
Geolocation= GetLatLong(api_key_geo)
geo_postal_code= '75008'  # Example postal code (NY coastal 11770 10003, Paris 75008)
latitude, longitute = Geolocation.geocode_lat_long(geo_postal_code)
print(f'\nPostal Code: {geo_postal_code}\nLatitude Longitude is : {latitude, longitute}\n')


##PLACES API WATER GLOBAL - FINDS IF ANY WATER IS CLOSE BY
api_key_places= "XXXXXXXXXXX"
water_places= Places_Water(api_key_places)
no_water_found = water_places.find_places_water(latitude,longitute)
print(f"\nNUMBER OF WATER FOUND: { no_water_found}")


##PLACES API FIRE STATION GLOBAL - FINDS IF ANY FIRESTATION IS CLOSE BY
api_key_places= "XXXXXXXXXXX"
firestation_places= Places_FireStation(api_key_places)
no_firestation_found = firestation_places.find_places_firestation(latitude,longitute)
print(f"\nNUMBER OF FIRESTATIONS FOUND: { no_firestation_found}")



##PLACES API HOSPITALS GLOBAL - FINDS IF ANY HOSPITALS IS CLOSE BY
api_key_places= "XXXXXXXXXXX"
hospital_places= Places_Hospital(api_key_places)
no_hospitals_found = hospital_places.find_places_hospital(latitude,longitute)
print(f"\nNUMBER OF HOSPITALS FOUND: { no_hospitals_found}")


##PLACES API POLICE STATION GLOBAL - FINDS IF ANY HOSPITALS IS CLOSE BY
api_key_places= "XXXXXXXXXX"
police_places= Places_Police(api_key_places)
no_police_found = police_places.find_places_police(latitude,longitute)
print(f"\nNUMBER OF POLICE STATIONS FOUND: { no_police_found}")


##PLACES API GROCERY SUPERMARKET GLOBAL - FINDS IF ANY HOSPITALS IS CLOSE BY
api_key_places= "XXXXXXXXXX"
supermarket_places= Places_SuperMarket(api_key_places)
no_supermarket_found = supermarket_places.find_places_supermarket(latitude,longitute)
print(f"\nNUMBER OF SUPERMARKET FOUND: { no_supermarket_found}")


# GET WEATHER ALERTS USA STATES ONLY
weather_alerts = SeverWeatherAlerts()
state="TX"
no_current_alerts = weather_alerts.get_alerts_states(state)
print(f"\nNUMBER OF CURRENT WEATHER ALERTS FOR STATE: {state} is { no_current_alerts}")



'''
"message": "Does not have a value in the enumeration ["AM","AN","GM","LC","LE","LH","LM","LO","LS","PH","PK","PM","PS","PZ","SL"]" }, \
{ "parameter": "query.area[0]", "message": "Does not have a value in the enumeration ["AL","AK","AS","AR","AZ",\
    "CA","CO","CT","DE","DC","FL","GA","GU","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS",\
        "MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT",\
            "VT","VI","VA","WA","WV","WI","WY","MP","PW","FM","MH"]"
'''