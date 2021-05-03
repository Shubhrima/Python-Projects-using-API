from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_ID = input('Type in Client ID')
Client_Secret = input('Type in Client Secret Key')
URL = 'https://gaana.com/playlist/gaana-dj-bengali-retro-top-50'
response = requests.get(URL)
contents = response.text
soup = BeautifulSoup(contents, 'html.parser')

song_playlist = []
maa_playlist = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id = Client_ID,
        client_secret = Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user = maa_playlist.current_user()
user_id = user["id"]

songs = soup.select(selector = 'ul li.draggable ')
for song in songs:
    song_name=song.getText().split(',')[0].split(':')[1].split('"')[1]
    result = maa_playlist.search(q=f"track:{song_name}", type="track")
    try:
        song_track = result["tracks"]["items"][0]["uri"]
        print(song_name)
        print(song_track)
        song_playlist.append(song_track)
    except IndexError:
        pass

playlist = maa_playlist.user_playlist_create(user=user_id, name=f"মা", public=False)
# print(playlist)

maa_playlist.playlist_add_items(playlist_id=playlist["id"], items=song_playlist)
print(playlist)