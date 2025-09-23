
from tracker import records
from datetime import datetime
import json

travels=[
    records("Paris", "Great Place", "10-08-2022"),
    records("New York", "Loved it", "15-09-2023"),
    records("Tokyo", "Amazing culture", "20-12-2023")
]
for travel in travels:
    date_object = datetime.strptime(travel["date"], "%d-%m-%Y")
    travel["date"] = date_object.strftime("%B %d, %Y")

travels_json = json.dumps(travels, indent=4)
print(travels_json)

travels_obj = json.loads(travels_json)
for t in travels_obj:
    print(f"City: {t['city']}, Comment: {t['comment']}, Date: {t['date']}")