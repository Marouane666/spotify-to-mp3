from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pathlib import Path
import youtube_dl
import requests
import pandas
import os
import urllib.request
import re
import time


def DownloadVideosFromTitles(los):
	ids = []
	for index, item in enumerate(los):
		vid_id = ScrapeVidId(item)
		ids += [vid_id]
	print("Downloading songs")
	DownloadVideosFromIds(ids)

def DownloadVideosFromIds(lov):

	ydl_opts = {
    	'format': 'bestaudio/best',
   		'postprocessors': [{
        		'key': 'FFmpegExtractAudio',
        		'preferredcodec': 'mp3',
        		'preferredquality': '192',
    		}],
		'outtmpl': 'C:/Users/LENOVO/Desktop/testest/%(title)s.%(ext)s',
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(lov)


def urlify(s):
		s = re.sub(r"[^\w\s]", '', s)
		s = re.sub(r"\s+", '+', s)

		return s


def ScrapeVidId(query):
	print ("Getting video id for: ", query)
	BASIC="http://www.youtube.com/results?search_query="
	query = urlify(query)
	URL = (BASIC + query)
	html = urllib.request.urlopen(URL)
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	return video_ids[0]


def __main__():





__main__()
