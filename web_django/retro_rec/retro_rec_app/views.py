from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseRedirect
from .models import DatasetIgdb

import pickle
import json
import random

def index(request):
    pass


@csrf_exempt
def onLoadGameData(request):
    ''' passes ids mapped to names for the games onload'''

    items = DatasetIgdb.objects.values('id', 'name')
    
    # sort by name order
    items = sorted(items, key=lambda i: i['name'])

    id_name_json = json.dumps(list(items))
    #print(app_json)

    return HttpResponse(id_name_json)


@csrf_exempt
def recommend_games(request):
    ''' makes a recommendation based on games passed back to the server'''


    game_ids = list(DatasetIgdb.objects.values_list('id', flat=True))

    # read in matrix pickle file and store as var similarities
    filename = 'similarity_matrix'
    infile = open(filename, 'rb')
    similarities = pickle.load(infile)
    infile.close()

    data_extract = request.body.decode('utf-8') 
    body = json.loads(data_extract)

    # either want random games
    if body == 'random':
        # get list of games rated >= 80 and by 10 or more people
        # 497 sample size.
        quality_games = list(DatasetIgdb.objects.filter(
            total_rating__gte=80, total_rating_count__gte=10).values_list('id', flat=True))

        # get a random 10 games
        random.shuffle(quality_games)
        top_recs = quality_games[:10]

    # else has sent back a list of target games
    else:
        target_games = []
        for game in body:
            target_games.append(str(game['id']))
    
        # Get simss to target games. dictionary[game_id]:sim.
        sims = {}
        for game_id in game_ids:
            if str(game_id) not in target_games:
                mean_relevance = 0
                for target_id in target_games:
                    score = similarities.get_value(target_id, str(game_id))
                    mean_relevance += score
                if mean_relevance > 0:
                    sims[str(game_id)] = mean_relevance / len(target_games)

        # get list of top x num of games from sims dict.
        num_recs = 10
        top_recs = []
        if len(sims) > 0:
            count = 0
            # this sorts dictionary by highest value meaning best rated games first in dict.
            for key, value in sorted(sims.items(), key=lambda x: x[1], reverse=True):
                if count < num_recs and count < len(sims):
                    top_recs.append(key)
                    count += 1


    recs=[]

    for game in top_recs:
        recs.append(DatasetIgdb.objects.filter(
            id=game).values('id', 'name', 'summary')[0])

    return HttpResponse(json.dumps(recs))




