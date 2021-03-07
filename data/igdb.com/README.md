Consoles scraped:
	4 :	'Nintendo 64',
	7 :	'PlayStation',
	8 :	'PlayStation 2',
	18:	'Nintendo Entertainment System (NES)',
	19:	'Super Nintendo Entertainment System (SNES)',
	21:	'Nintendo GameCube',
	23:	'Dreamcast',
	29:	'Sega Mega Drive_Genesis',
	32:	'Sega Saturn'
	
1. Get API Key from igdb.com (free and allowed 50k API hits per month)
2. Insert API key into line 5 of igdb_scraper.py
3. Run igdb_scraper.py which produces 'game_dataset_igdb.csv'.
NOTE: If you want to scrape more or different consoles just edit platforms_dict in igdb_scraper.py.
4. Run either igdb_data_clean.ipynb or igdb_data_clean.py (both do the same thing) to clean the csv file and output final dataset as both 'dataset_igdb.csv' and 'dataset_igdb.txt'.