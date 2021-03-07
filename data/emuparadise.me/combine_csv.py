import pandas as pd

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

filenames = []

for key in consoles:
	filenames.append(key+'_genre_ratings.csv')


combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )

combined_csv.to_csv('game_dataset_emuparadise.csv', index=False )