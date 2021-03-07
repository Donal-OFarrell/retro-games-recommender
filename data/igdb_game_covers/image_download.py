import requests
import csv

headers={'User-Agent':'Mozilla/5'}

with open ('dataset_igdb.csv','r', encoding='utf8') as file:
	data = list(csv.reader(file))
	# start at 1 to avoid heading row.
	for x in range(1,len(data)):
		id = data[x][0]
		cover_url = data[x][7]

		pic_request = requests.get(cover_url, headers = headers)
		if pic_request.status_code == 200:
			with open("original/"+id+".jpg", 'wb') as p:
				print('saving '+id+'.jpg')
				p.write(pic_request.content)

	print('Done')