import requests
import json
import schedule
import time
from datetime import datetime

from DB_conect import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()


def fetch_data():
    url = "https://api.tzevaadom.co.il/alerts-history/"

    # Set start_date and end_date to the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    params = {
        'start_date': current_date,
        'end_date': current_date,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Return the fetched data
        return json.loads(response.text)
    else:
        # Log details about the error
        print(f"Error {response.status_code}: Unable to fetch data.")
        print(response.text)  # Print the response content for debugging


class AlertItem:
    def __init__(self, id, city, time):
        self.id = id
        self.City = city
        self.Time = time

    def save(self):
        # Insert data into the "alerts" table
        cursor.execute(
            "INSERT INTO alerts (id, city, time) VALUES (%s, %s, %s)",
            (self.id, self.City, self.Time),
        )
        conn.commit()


# Function to format time
def format_time(entry):
    for alert in entry['alerts']:
        # Format time as real date-time
        dt_object = datetime.fromtimestamp(alert['time'])
        alert['time'] = dt_object.strftime("%Y-%m-%d %H:%M:00")

    return entry


def main():
    json_data = fetch_data()
    formatted_data = [format_time(entry) for entry in json_data]

    for entry in formatted_data:
        for alert in entry['alerts']:
            for city in alert['cities']:
                ID = entry['id']
                City = city.split(' -')[0]
                Time = alert['time']
                item = AlertItem(ID, City, Time)
                item.save()

    conn.close()


# Schedule to run at 23:59 every day
schedule.every().day.at("23:59").do(main)

# Unending cycle
while True:
    schedule.run_pending()
    time.sleep(1)


           

                    







