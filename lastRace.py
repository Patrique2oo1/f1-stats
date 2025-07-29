# import biblioteki
import requests

def showResults():
    # 1.1. wyniki wyścigu
    response = requests.get(f'https://api.jolpi.ca/ergast/f1/current/last/results/?limit=100')
    data = response.json()
    currentResults = data['MRData']['RaceTable']['Races'][0]['Results']
    currentSeason = data['MRData']['RaceTable']['Races'][0]['season']
    currentRaceName = data['MRData']['RaceTable']['Races'][0]['raceName']
    currentRaceDate = data['MRData']['RaceTable']['Races'][0]['date']

    print("\n"f"{currentSeason} {currentRaceName} ({currentRaceDate}) - wyniki:")
    for result in currentResults:
        position = result['position']
        driver = result['Driver']
        name = f"{driver['givenName']} {driver['familyName']}"
        constructor = result['Constructor']['name']
        print(f"{position}. {name} ({constructor})")
    
    # 1.2. klasyfikacja kierowców
    response = requests.get(f'https://api.jolpi.ca/ergast/f1/current/driverstandings/?limit=100')
    data = response.json()
    currentStandings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    print("\n"f"{currentSeason} {currentRaceName} ({currentRaceDate}) - klasyfikacja kierowców:")
    for rank in currentStandings:
        position = rank['position']
        driver = rank['Driver']
        name = f"{driver['givenName']} {driver['familyName']}"
        points = rank['points']
        print(f"{position}. {name} ({points} pts)")
        
    # 1.3. klasyfikacja konstruktorów
    response = requests.get(f'https://api.jolpi.ca/ergast/f1/current/constructorstandings/?limit=100')
    data = response.json()
    currentStandings = data['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
    print("\n"f"{currentSeason} {currentRaceName} ({currentRaceDate}) - klasyfikacja konstruktorów:")
    for rank in currentStandings:
        position = rank['position']
        constructor = rank['Constructor']
        name = f"{constructor['name']}"
        points = rank['points']
        print(f"{position}. {name} ({points} pts)")
        
# test wywołania - showResults()