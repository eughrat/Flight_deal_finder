import requests

SHEETY_KEY = "Basic ZXVnaHJhdDpTRVJlazEwLg"
sheety_enpoint = "https://api.sheety.co/389b3e8f47624ffe52763551e06f2006/flightDeals/arkusz1"

sheety_headers = {
    "Authorization": SHEETY_KEY,
}


class DataManager:

    def __init__(self):
        self.data = {}

    def get_sheet_data(self):
        response = requests.get(url=sheety_enpoint, headers=sheety_headers)
        result = response.json()
        return result

    def update_iata_code(self):
        for city in self.data:
            parameters = {
                "arkusz1": {
                    "iataCode": city['iataCode']
                }
            }
            print(city)
            response = requests.put(url=f"{sheety_enpoint}/{city['id']}",
                                    json=parameters,
                                    headers=sheety_headers)
            result = response.json()
            print(result)

# 2. Use the Sheety API to GET all the data in that sheet and print it out.

# 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
# pprint(data)

# 6. In the DataManager Class make a PUT request and use the row id from sheet_data
# to update the Google Sheet with the IATA codes. (Do this using code).
