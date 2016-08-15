# !user/bin/python

# Author: Chun Zheng
# Name: Walmart Code Challenge
# Lang: python 2.7
# @([O.O])@ codemonkey for encouragement

import json
import requests


class CodeChallenge(object):

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

        # requested format from walmart
        print search_request
        resp = requests.get(search_request)

        self.data = resp.json()
        self.reviews = {}

    # retrive first 10 recommendations productID
    def recommendations(self):

        first_item = '&itemId=' + str(self.data['items'][0]['itemId'])
        recommend_request = self.recommendation_request + self.apiKey + first_item
        recommendation_resp = requests.get(recommend_request)
        self.recommendations = recommendation_resp.json()
        for i in range(11):
            self.reviews[str(self.recommendations[i]['itemId'])] = i
        print self.reviews

    def review(self):

        # http://api.walmartlabs.com/v1/reviews/53317526?format=json&apiKey=
        for key in self.reviews:
            print "key: %s, value: %s" % (str(key), str(self.reviews[key]))
            reviews_resp = requests.get(self.reviews_request + str(key) + '?' + self.apiKey)
            reviews_json = reviews_resp.json()
            self.reviews[key] = reviews_json['reviews']['reviewStatistics']['averageOverallRating']
        print self.reviews

    def sort_review(self):
        print sorted(self.reviews)


test = CodeChallenge()
test.recommendations()
test.review()
