import requests
sd = input("enter the starting date :")
ed = input("enter the ending date :")
mm = input("enter the minimum magnitude")

res = requests.get(f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={sd}&endtime={ed}&minmagnitude={mm}")

data = res.json()
features = data["features"]

for feature in features:
    print(feature["properties"]["mag"] , feature["properties"]["place"])