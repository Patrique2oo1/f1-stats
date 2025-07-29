# import biblioteki
import requests

def showList():
    response = requests.get(f'https://api.jolpi.ca/ergast/f1/circuits/?limit=100')
    data = response.json()
    circuits = [circuit['circuitName'] for circuit in data['MRData']['CircuitTable']['Circuits']]
    print(f"Lista torów: ", circuits, "\n")
        
# test wywołania - showList()