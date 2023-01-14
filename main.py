import pprint

from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

sheety_data = data_manager.get_sheet_data()
sheet_data = sheety_data['arkusz1']
print(sheet_data)

for i in sheet_data:
    i["iataCode"] = flight_search.get_iata_code(i['city'])

print(sheet_data)


data_manager.data = sheet_data
data_manager.update_iata_code()





# 4. Pass the data back to the main.py file, so that you can print the data from main.py

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
