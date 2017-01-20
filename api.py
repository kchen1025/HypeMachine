import requests
import urllib.parse 
import collections
import json

import tracks



class Api():

	def __init__(self):
		pass


	#get popular tracks from the front page based on queries, if nothing just returns top
	#mode: now, lastweek, remix, noremix (string)
	#count: items per page (int)

	#returns class that you can iterate through the json with
	def getPopularTracks(self, mode=None, page=None, count=None):
		popularTracksUrl = 'https://api.hypem.com/v2/popular?key=swagger&'

		query = collections.OrderedDict()
		if mode != None:
			query['mode'] = mode
		if page != None:
			query['page'] = page
		if count != None:
			query['count'] = count

		params = urllib.parse.urlencode(query)
		apiUrl = popularTracksUrl + params
		popularTracks = tracks.PopularTracks(requests.get(apiUrl))
		return popularTracks
		

		

a = Api()
temp = a.getPopularTracks('lastweek',1,3)
print(temp.getJson())
