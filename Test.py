# !user/bin/python

# Author: Chun Zheng
# Name: Walmart Code Challenge
# Lang: python 2.7
# @([O.O])@ codemonkey for encouragement

import json
import pprint
import requests


class test(object):

    def __init__(self):

        # promt user the search itemk
        search = raw_input('What would you like to search: ')
        # replace the spaces in the search input with '+' for the query string
        item = search.replace(' ', '+')

        # global api key
        self.apiKey = '&apiKey=9s7yx3b5sxchpmb8szzefu9x'
        # desired format
        return_format = '&format=json'

        # request url
        search_request = 'http://api.walmartlabs.com/v1/search?query=' + item + return_format + self.apiKey
        self.reviews_request = 'http://api.walmartlabs.com/v1/reviews/'
        self.recommendation_request = 'http://api.walmartlabs.com/v1/nbp?'

        # Search API URI
        print "Search API URI: %s" % search_request
        resp = requests.get(search_request)

        # data for the item
        self.data = resp.json()
        self.reviews = {}

    # retrive first 10 recommendations productID
    def recommendations(self):

        # take the first item from the search to build the URI
        first_item = '&itemId=' + str(self.data['items'][0]['itemId'])
        recommend_request = self.recommendation_request + self.apiKey + first_item

        # Recommendation API URI
        print "Recommendation API URI: %s" % recommend_request
        recommendation_resp = requests.get(recommend_request)

        self.recommendations = recommendation_resp.json()
        for i in range(11):
            self.reviews[str(self.recommendations[i]['itemId'])] = self.recommendations[i]['name']
        print '\n Recommendations'
        print '------------------------------------------------------------------------------'
        pprint.pprint(self.reviews)
        print '------------------------------------------------------------------------------'

    def overall_rating_review(self):

        # prints the overall ratings for the initial recommendations
        for key in self.reviews:
            print "key: %s, value: %s" % (str(key), str(self.reviews[key]))
            reviews_resp = requests.get(self.reviews_request + str(key) + '?' + self.apiKey)
            reviews_json = reviews_resp.json()
            self.reviews[key] = reviews_json['reviews'][0]['overallRating']['rating']
        print self.reviews

    def sentiment_analysis(self):
        print sorted(self.reviews)


test = test()
test.recommendations()
test.overall_rating_review()
