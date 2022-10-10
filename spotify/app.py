#app.py
#Authour : Marouane Tabaa
#
#
#Date : 10-OCT-2022
#
#
#

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, url_for, session, request, redirect
import json
import time
import pandas as pd
import numpy as np
from .download import DownloadVideosFromTitles



app = Flask(__name__)

app.secret_key = "Rabdom-code"
app.config['SESSION_COOKIE_NAME'] = 'Name cookie'
TOKEN_INFO = "token_info"


@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/download')
def download() :
    data = pd.read_csv('songs.csv')
    data = data['song names'].tolist()
    print("Found ", len(data), " songs!")
    DownloadVideosFromTitles(data)
    return redirect(url_for('getTracks', _external=True))


@app.route('/redirect')
def redirectPage():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('getTracks', _external=True))

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')



@app.route('/getTracks')
def getTracks():
    try:
        token_info = get_token()
    except:
        print("user no logged in")
        return redirect("/")
    sp = spotipy.Spotify(auth=token_info['access_token'])
    all_songs = []
    iter = 0

    while True:
        offset = iter * 50
        iter += 1
        items = sp.current_user_saved_tracks(limit=50, offset=offset)['items']
        for idx, item in enumerate(items):
            track = item['track']
            val = track['name'] + " - " + track['artists'][0]['name']
            all_songs += [val]


        if (len(items) < 50):
            break
    df = pd.DataFrame(all_songs, columns=["song names"])
    df.to_csv('songs.csv',index = False)



    return "Done"


def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise "exception"
    now = int(time.time())
    print(token_info['expires_at'])
    is_expired = token_info['expires_at'] - now < 30
    if (is_expired):
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info


def create_spotify_oauth():
    return SpotifyOAuth(
        client_id="cliendt_Id",
        client_secret="client_secret",#get them by applying to spotify dev
        redirect_uri=url_for('redirectPage', _external=True),
        scope="user-library-read")

