import requests
import urllib.parse 
import collections


#for the popular tracks object to reside 
class PopularTracks():
	def __init__(self,r):
		#r that is passed in is the requests object from which we can manipulate
		self.requestsObj = r

	def getJson(self):
		return self.requestsObj.json()