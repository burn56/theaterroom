from flask import Flask, request, abort
import requests
import os

app = Flask(__name__)

@app.route('/play_movie/<player_id>/<movie_id>')
def play_movie(player_id, movie_id):
    plex_token = os.getenv('PLEX_TOKEN')
    if not plex_token:
        abort(500, "Plex token is not set in the environment variables.")
    plex_url = f'http://your-plex-server-ip:32400/player/playback/playMedia?X-Plex-Token={plex_token}&key=/library/metadata/{movie_id}&machineIdentifier={player_id}'
    response = requests.get(plex_url)
    return 'Playing movie'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4942)