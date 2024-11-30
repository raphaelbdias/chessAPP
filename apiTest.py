import os
import berserk
import requests
import pprint as p

API_TOKEN = os.getenv('API_TOKEN')
session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session=session)



# API endpoint for Lichess cloud evaluation
url = "https://lichess.org/api/cloud-eval"

# Specify a FEN string
fen = "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2"  # Example position

# Make a request
headers = {
    'Authorization': f'Bearer lip_lcWriyipVPgYVYIEMrbU'  # Replace with your API token
}
params = {
    'fen': fen
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = (response.json())  # Print response data as JSON
    moves = data['pvs'][0]
    print(moves['moves'].split(' '))
else:
    print(f"Error: {response.status_code} - {response.text}")