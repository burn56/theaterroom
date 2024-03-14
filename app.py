from flask import Flask
import requests

app = Flask(__name__)

@app.route('/play_movie')
def play_movie():
    plex_token = 'Your_Plex_Auth_Token'
    player_id = 'Your_Player_Identifier'
    movie_id = 'Your_Movie_Identifier'
    plex_url = f'http://your-plex-server-ip:32400/player/playback/playMedia?X-Plex-Token={plex_token}&key=/library/metadata/{movie_id}&machineIdentifier={player_id}'
    response = requests.get(plex_url)
    return 'Playing movie'

if __name__ == '__main__':
    app.run(host='0.0.0.0')