# !user/bin/python
# -*- coding: utf-8 -*

# Author: Chun Zheng
# Name: Test File
# Lang: python 2.7
# (╯°□°）╯︵ ┻━┻ table flipping emoji for sanity

import re
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
        self.products = {}
        self.reviews = {}
        self.sentiment_review = {}
        self.answer = {}

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
            self.products[str(self.recommendations[i]['itemId'])] = self.recommendations[i]['name']
        print '\n Recommendations'
        print '------------------------------------------------------------------------------'
        pprint.pprint(self.products)
        print '------------------------------------------------------------------------------'

    def review_text(self):

        # prints the overall ratings for the initial recommendations
        for key in self.reviews:
            # Review API URI
            reviews_resp = requests.get(self.reviews_request + str(key) + '?' + self.apiKey)
            reviews_json = reviews_resp.json()

            # Long string containing first 5 reviews (if they exist)
            review = ''
            for i in range(5):
               review = review + reviews_json['reviews'][i]['reviewText']
            self.reviews[key] = review
            print "key: %s , review: %s \n" % (key, review)

    def sentiment_analysis(self):
        for key in self.reviews:
            string = self.reviews[key]
            text = re.sub(r'[^\w]', ' ', string)
            req = requests.post("http://text-processing.com/api/sentiment/", data={'text': text})
            sentiment_json = req.json()
            self.sentiment_review[key] = sentiment_json['probability']['pos']
            self.answer[self.products[key]] = sentiment_json['probability']['pos'] 

    def print_recommendations(self):
        for key, value in sorted(self.answer.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            print "Name: %s | Pos Rating: %s" %(key, self.answer[key])

test = test()
test.recommendations()
test.review_text()
test.sentiment_analysis()
test.print_recommendations()
