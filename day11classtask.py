
from tripdata import details
from datetime import datetime
import json

trips=[
    details("Bangkok", "10-08-2022" ,"Business trip"),
    details("Paris", "15-09-2023", "Vacation"),
    details("Dubai", "20-12-2023", "Conference")
]
for trip in trips:
    date_object = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_object.strftime("%B %d, %Y")

trips_json = json.dumps(trips, indent=4)
print(trips_json)