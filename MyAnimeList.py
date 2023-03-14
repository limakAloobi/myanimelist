#download youtube videos offline to mp4 or whatever
#from pytube import YouTube
#YouTube('https://www.youtube.com/watch?v=lrk4oY7UxpQ&t=0s&index=2&list=PL8dPuuaLjXtOfse2ncvffeelTrqvhrz8H').streams.first().download()

#importing relevant modules
import numpy as np
import pandas as pd
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#variable for number of rows
number_of_rows = 0
#print(type(number_of_rows))
#URL to hit
myanimelist_url = str("https://myanimelist.net/topanime.php?limit=" + str(number_of_rows))
#print(myanimelist_url)


#creating the headers in excel
filename = "MyAnimeList.csv"
f = open(filename, "w")
headers = "ranking, anime, rating, episodes, airdate,members\n"
f.write("")
#
#downloading the information

uClient = uReq(myanimelist_url)
#
##storing the data
myanimelist_html = uClient.read()
uClient.close()

#parsing html
page_soup = soup(myanimelist_html, "html.parser")
#grabbing the giant box header box with ranking that contains
#all of the list
containers = page_soup.findAll("div",{"class":"pb12"})
#inspecting further 1 layer shows they are included all in 
#this subclass

containers = page_soup.findAll("tr",{"class":"ranking-list"})
container = containers[0]

#grabbing list of tv members and dates
ep_date_members = container.findAll("div",{"class":"information di-ib mt4"})
#cleaning list. need to just grab the 1:4 elements
#need to remove all special characters except letters and numbers
list_eps = str(ep_date_members).split("\n")
list_eps1 = str(list_eps[1:4]).split("br")
import re
for k in list_eps1:
    k.split("\n")
    print(re.sub(r"[^a-zA-Z0-9]+", ' ', k))

 container.findAll("td",{"class":"text on"})
 #########   NEED TO FIX THIS 
#gettin title and rankingg list
title = container.img["alt"]
ranking =
