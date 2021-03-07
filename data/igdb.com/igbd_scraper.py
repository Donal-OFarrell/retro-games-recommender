import requests
import csv
import time

# insert key here
YOUR_API_KEY = "YOUR_API_KEY" 

# dictionary containing id's and names of all genres on igdb.com
genres_dict = {
	2 : 'Point-and-click',
 	4 : 'Fighting',
 	5 : 'Shooter',
 	7 : 'Music',
 	8 : 'Platform',
 	9 : 'Puzzle',
 	10: 'Racing',
 	11: 'Real Time Strategy (RTS)',
 	12: 'Role-playing (RPG)',
 	13: 'Simulator',
 	14: 'Sport',
 	15: 'Strategy',
 	16: 'Turn-based strategy (TBS)',
 	24: 'Tactical',
 	26: 'Quiz/Trivia',
 	25: "Hack and slash/Beat 'em up",
 	30: 'Pinball',
 	31: 'Adventure',
 	33: 'Arcade',
 	34: 'Visual Novel',
 	32: 'Indie',
 	35: 'Card & Board Game',
 	36: 'MOBA'
}

# dictionary containing id's and names of all themes on igdb.com
themes_dict = {
	20: 'Thriller',
	18: 'Science fiction',
	1 : 'Action',
	19: 'Horror',
	21: 'Survival',
	17: 'Fantasy',
	22: 'Historical',
	23: 'Stealth',
	27: 'Comedy',
	28: 'Business',
	31: 'Drama',
	32: 'Non-fiction',
	35: 'Kids',
	33: 'Sandbox',
	38: 'Open world',
	39: 'Warfare',
	41: '4X (explore, expand, exploit, and exterminate)',
	34: 'Educational',
	43: 'Mystery',
	40: 'Party',
	44: 'Romance',
	42: 'Erotic'
}

# dictionary containing id's and names of all player persepctives on igdb.com
player_perspectives_dict = {
	1 : 'First person',
	2 : 'Third person',
	3 : 'Bird view / Isometric',
	5 : 'Text',
	4 : 'Side view',
	7 : 'Virtual Reality',
	6 : 'Auditory'
}

# dictionary containing id's and names of consoles we're scraping from igdb.com. More can be added/removed
# console id's can be accessed here https://gist.github.com/ahmed-abdelazim/b533b443388baaafab3fc377e71e0109 .  
platforms_dict = {
	4 :	'Nintendo 64',
	7 :	'PlayStation',
	8 :	'PlayStation 2',
	18:	'Nintendo Entertainment System (NES)',
	19:	'Super Nintendo Entertainment System (SNES)',
	21:	'Nintendo GameCube',
	23:	'Dreamcast',
	29:	'Sega Mega Drive_Genesis',
	32:	'Sega Saturn'
}

# create/open csv file titled game_dataset_igdb.csv using append option
games = open('game_dataset_igdb.csv', 'a', newline='', encoding="utf-8")

# create csv writer object and write the header
csvwriter_games = csv.writer(games)
header = ['id','name','slug','platforms','game_url','comparisons','cover_id','cover_url','cover_height','cover_width','summary','first_release_date','total_rating','total_rating_count']
csvwriter_games.writerow(header)

for key in platforms_dict:

	# max limit of games returned for api so set limit to maximum allowed.
	limit = 500
	# offset is index where list starts from so an offset of 0 means we get 0-500 of games in the list on igdb, offset of 400 would mean we get from 400-900 etc.
	# max value of offset for api is 5000.
	offset = 0

	# want to call the api while it returns a response of games, once offset becomes too large this will not be the case.
	call_api = True

	while call_api:
		# call api (post rather than get). There are more fields that can be added. more information can be gotten in igdb api documentation.
		API_endpoint = "https://api-v3.igdb.com/"
		API_command = "games" 
		API_params = {
		        'headers': {'user-key': YOUR_API_KEY},
		        'data': """
		            fields name,category,cover.url,cover.height,cover.width,first_release_date,genres,platforms,player_perspectives,slug,summary,themes,total_rating,total_rating_count,url;
		            where platforms = [{}];
		            limit {};
		            offset {};
		        """.format(key,limit,offset)
		}

		API_url = API_endpoint + API_command
		r = requests.post(API_url, **API_params)
		response = r.json()

		# if no games returned from api set call_api to false to exit loop and no longer call api for this console.
		if len(response) == 0:
			call_api = False
		else:
			for x in range(len(response)):
				# get all variables need to write row on spreadsheet. first four should also be available for every game.
				game_id = response[x]['id']
				name = response[x]['name']
				slug = response[x]['slug']
				platforms = response[x]['platforms']
				game_url = response[x]['url']
				# Added error handling for rest of variables as they may not exist for all games.
				if 'genres' in response[x]: 
					genres = response[x]['genres']
				else:
					genres = []
				if 'themes' in response[x]: 
					themes = response[x]['themes']
				else:
					themes = []
				if 'player_perspectives' in response[x]: 
					player_perspectives = response[x]['player_perspectives']
				else:
					player_perspectives = []
				if 'cover' in response[x]:
					cover_id = response[x]['cover']['id']
					cover_url = response[x]['cover']['url']
					cover_height = response[x]['cover']['height']
					cover_width = response[x]['cover']['width']
				else:
					cover_id = 0
					cover_url = ''
					cover_height = 0
					cover_width = 0
				if 'summary' in response[x]: 
					summary = response[x]['summary']
				else:
					summary = ""
				if 'first_release_date' in response[x]: 
					first_release_date = response[x]['first_release_date']
				else:
					first_release_date = 0
				if 'total_rating' in response[x]: 
					total_rating = response[x]['total_rating']
				else:
					total_rating = 0
				if 'total_rating_count' in response[x]: 
					total_rating_count = response[x]['total_rating_count']
				else:
					total_rating_count = 0

				# platforms returns a list of consoles game available on so iterating through that here to replace console id with console name. 
				consoles = []
				for platform in platforms:
				# check if platform in platforms_dict so if game available on ps4 as well it wont show in out dataset which suits current need.
					if platform in platforms_dict:
						consoles.append(platforms_dict[platform])

				# for the recommender I want to combine genre, themes and player perspective into one list and also replace ids with actual name. All handled below.
				comparisons = []
				for genre in genres:
					comparisons.append(genres_dict[genre])	
				for theme in themes:
					comparisons.append(themes_dict[theme])	
				for player_perspective in player_perspectives:
					comparisons.append(player_perspectives_dict[player_perspective])	

				# replace _thumb in cover_url with _original and also add 'https:' to the beginning or url.
				if '_thumb' in cover_url:
					cover_url = 'https:' + cover_url.replace('_thumb','_original')

				# write row to csv file.
				csvwriter_games.writerow([game_id,name,slug,consoles,game_url,comparisons,cover_id,cover_url,cover_height,cover_width,summary,first_release_date,total_rating,total_rating_count])

			# increase offset each timeby 500 as limit is 500.
			offset += 500
			# max offset allowed by API is 5000 so if offset is greater than this then don't call api again with this larger value.
			if offset > 5000:
				call_api = False
				
			time.sleep(1)

# close games csv file.
games.close()
		

