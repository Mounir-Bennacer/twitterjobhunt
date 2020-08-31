from TwitterAPI import TwitterAPI
import geopandas as gpd
import matplotlib.pyplot as plt
import json
import descartes

consumer_key = "API KEY HERE"
consumer_secret = "API SECRET KEY HERE"
access_token_key = "ACCESS TOKEN HERE"
access_token_secret = " ACCESS SECRET TOKEN HERE"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

response = api.request(
    "statuses/filter",
    {
        "track": [
            "jobs",
            "Leeds",
            "Manchester",
            "Derby",
            "Python",
            "Developer",
            "Software Engineer",
        ]
    },
)

coordinates = []
tweets = response.get_iterator()

count = 0
while count < 50:
    tweet = next(tweets)
    if "place" in tweet and tweet["place"] is not None:
        place = tweet["place"]["bounding_box"]["coordinates"][0][0]
        coordinates.append(place)
        count += 1
        print(place)

world_map = gpd.read_file("./TM_WORLD_BORDERS-0.3.shp")

fix, ax = plt.subplots(figsize=(15, 15))

world_map.plot(ax=ax)

for x, y in coordinates:
    plt.scatter(x, y, marker="o", color="red")

plt.savefig("map.png")
