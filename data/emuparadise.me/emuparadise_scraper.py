import requests
import bs4
import csv
import json
import time

# create a dictionary of all consoles you need data for, along with link to all title on emuparadise.me
consoles = {
'nes' : '/Nintendo_Entertainment_System_ROMs/List-All-Titles/13',
'super_nintendo' : '/Super_Nintendo_Entertainment_System_(SNES)_ROMs/List-All-Titles/5',
'sega_megadrive' : '/Sega_Genesis_-_Sega_Megadrive_ROMs/List-All-Titles/6',
'sega_saturn' : '/Sega_Saturn_ISOs/List-All-Titles/3',
'ps_one' : '/Sony_Playstation_ISOs/List-All-Titles/2',
'sega_dreamcast' : '/Sega_Dreamcast_ISOs/List-All-Titles/1',
'n64' : '/Nintendo_64_ROMs/List-All-Titles/9',
'ps2' : '/Sony_Playstation_2_ISOs/List-All-Titles/41'
}

# iterate though consoles dictionary
for key, value in consoles.items():

	# create/open csv file titled key_list.csv eg nes_list.csv
	games = open(key+'_list.csv', 'w', newline='', encoding="utf-8")

	# create csv writer object and write the header
	csvwriter_games = csv.writer(games)
	header = ['console','title','href']
	csvwriter_games.writerow(header)

	# url = "https://www.emuparadise.me"+value in dictionary to get list of all games for each console.
	url = 'https://www.emuparadise.me'+value
	headers={'User-Agent':'Mozilla/5'}

	# request page and parse to bs4
	page = requests.get(url, headers = headers)
	soup = bs4.BeautifulSoup(page.content,'html.parser')

	# iterate through all games and write row to csv file. This will populate all _list.csv
	for game in soup.find_all("a", class_="index gamelist"):
		title = game.text
		href = game.get("href")
		csvwriter_games.writerow([key,title,href])

	# close games csv file.
	games.close()

	# create/open second csv file titled key_genre_ratings.csv eg nes_genre_ratings.csv
	genre_ratings = open(key+'_genre_ratings.csv', 'w', newline='', encoding="utf-8")

	# create csv writer object and write the header
	csvwriter_genre_ratings = csv.writer(genre_ratings)
	header = ['console','title','average_rating','rating_count','genres']
	csvwriter_genre_ratings.writerow(header)

	# read in games from _list.csv.
	with open(key+'_list.csv', 'r', encoding="utf8") as read_obj:
		csvreader = csv.reader(read_obj)
		# skip heading row
		next(csvreader)
		for row in csvreader:

			# row[2] is the game href
			game_href = row[2]

			# url = "https://www.emuparadise.me"+game_href to get rating and genres of all games.
			url = 'https://www.emuparadise.me'+game_href
			headers={'User-Agent':'Mozilla/5'}

			# request page and parse to bs4
			page = requests.get(url, headers = headers)
			soup = bs4.BeautifulSoup(page.content,'html.parser')

			# try get average rating and number of raters for each game and if it does not exist set values equal zero.
			try:
				rows = soup.find_all('td', bgcolor="#4C6977")
				average_rating = rows[1].find_all("span")[0].text
				rating_count = rows[1].find_all("span")[1].text
			except:
				average_rating = 0
				rating_count = 0

			# get genres for each game and append to list.
			genres = []
			for genre in soup.find_all("a", class_="genre small-genre"):
				genres.append(genre.text)

			# write row to csv and sleep for one second so as to not overload the website. 
			csvwriter_genre_ratings.writerow([key,row[1],average_rating,rating_count,genres])
			time.sleep(1)

	# close genre_ratings csv file.
	genre_ratings.close()






