Scraped data from both emuparadise.me and igdb.com.
emuparadise scraped web pages for each console which took a lot longer to complete.
igdb has an api so scraping the api was a lot quicker and more efficient. Information seems a lot more complete also so decided to use this dataset for the retro game recommender.

Python scripts to scrape both sites and clean the results are in directories along with instructions on how to use them.

igdb_game_covers contains scripts to download game covers. Run 'image_download.py' which downloads the images into the original directory. Then run 'image_compress.py' which will compress all the original messages and save them into the compressed directory. This saves them at approx 25% of orignal file size.