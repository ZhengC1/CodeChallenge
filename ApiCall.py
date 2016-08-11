# !user/bin/python

# Author: Chun Zheng
# Name: Walmart Code Challenge
# Lang: python 2.7
# @([O.O])@ codemonkey for encouragement

import json
import requests


class ApiCall(object):

    def __init__(self):

        request = 'http://api.walmartlabs.com/v1/search?query='
        search = raw_input('What would you like to search: ')
        item = search.replace(' ', '+')
        return_format = '&format=json'
        self.apiKey = '&apiKey=9s7yx3b5sxchpmb8szzefu9x'
        resp = requests.get(request + item + return_format + self.apiKey)

        self.data = resp.json()

    def recommendations(self):
        first_item = '&itemId=' + str(self.data['items'][0]['itemId'])
        recommend_request = 'http://api.walmartlabs.com/v1/nbp?' + self.apiKey + first_item
        recommendation_resp = requests.get(recommend_request)
        recommendations = recommendation_resp.json()
        print recommendations[0]['name']


test = ApiCall()
test.recommendations()
