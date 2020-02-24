from django.shortcuts import render
from django.views import View 

import requests
import datetime

querystring = {"secret":"5UwNDirf9EsCEVCV4K6O7fbdeieXReFW","key":"g97bKn8m6Z60JyZH"}

headers = {'x-rapidapi-host': "live-score-api.p.rapidapi.com",
    'x-rapidapi-key': "c5428d8bc5msh26174ba8bed4d70p13c153jsne42ab237d205"}

class PortugalView(View):

	template_name = 'football/pt.html'
	url_hist = "https://live-score-api.p.rapidapi.com/scores/history.json"
	url_matches = "https://live-score-api.p.rapidapi.com/fixtures/matches.json"
	def get(self, request):

		qs = querystring
		qs['competition_id'] = "8"
		qs_hist = qs

		qs_hist['from'] = str(datetime.date.today() - datetime.timedelta(days=7))
		qs_hist['to'] = str(datetime.date.today())
		response = requests.request("GET", self.url_hist, headers=headers, params=qs_hist)
		data_hist = response.json()['data']

		response = requests.request("GET", self.url_matches, headers=headers, params=querystring)
		data_matches = response.json()['data']

		dates = {}	
		for jogo in data_hist['match']:

			game = {"home": jogo['home_name'],
					"away": jogo['away_name'],
					"score": jogo['score'],
					"hour": jogo['scheduled']
			}

			if jogo['date'] not in dates:
				dates[jogo['date']] = [game]
			else:
				dates[jogo['date']].append(game)

		for jogo in data_matches['fixtures']:

			if jogo['date'] <= str(datetime.date.today() + datetime.timedelta(days=7)):
				game = {"home": jogo['home_name'],
						"away": jogo['away_name'],
						"local": jogo['location'],
						"hour": jogo['time'][0:5]
				}

				if jogo['date'] not in dates:
					dates[jogo['date']] = [game]
				else:
					dates[jogo['date']].append(game)

			
			#print(jogo['date'], jogo['scheduled'])			
			#print(jogo['home_name'], " VS ", jogo['away_name'])
			#print(jogo['score'])
		context = {"queryset": dates}
		return render(request, self.template_name, context)
