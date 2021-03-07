Consoles scraped:
	'nes' : '/Nintendo_Entertainment_System_ROMs/List-All-Titles/13',
	'super_nintendo' : '/Super_Nintendo_Entertainment_System_(SNES)_ROMs/List-All-Titles/5',
	'sega_megadrive' : '/Sega_Genesis_-_Sega_Megadrive_ROMs/List-All-Titles/6',
	'sega_saturn' : '/Sega_Saturn_ISOs/List-All-Titles/3',
	'ps_one' : '/Sony_Playstation_ISOs/List-All-Titles/2',
	'sega_dreamcast' : '/Sega_Dreamcast_ISOs/List-All-Titles/1',
	'n64' : '/Nintendo_64_ROMs/List-All-Titles/9',
	'ps2' : '/Sony_Playstation_2_ISOs/List-All-Titles/41'
	
1. Run emuparadise_scraper.py
NOTE: If you want to scrape more or different consoles just edit 'consoles' in emuparadise_scraper.py.
2. This will produce two csv for each console '_list.csv' and '_genre_ratings.csv'.
3. '_list.csv' contains all games for the console along with the href to them on emuparadise.
4. '_genre_ratings.csv' all the data from '_list.csv' minus the href, plus ratings and genres for each game.
5. Run combine_csv.py which will combine all '_genre_ratings.csv' and save overall dataset as 'game_dataset_emuparadise.csv'.
6. Run either emuparadise_data_clean.ipynb or emuparadise_data_clean.py (both do the same thing) to clean the csv file and output final dataset as both 'dataset_emuparadise.csv' and 'dataset_emuparadise.txt'. 