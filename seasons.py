# import biblioteki
import requests

def showList():
    response = requests.get(f'https://api.jolpi.ca/ergast/f1/seasons/?limit=100')
    data = response.json()
    seasons = [season['season'] for season in data['MRData']['SeasonTable']['Seasons']]
    print(f"Lista sezonów: ", seasons, "\n")
        
# test wywołania - showList()