# Walmart Code Challenge

Using technologies of your choice, develop a simple program to rank-order Walmart product recommendations based upon customer reviews.  
The program should invoke the Walmart Labs Open API to implement the following workflow:

* Search for products based upon a user-provided search string
* Use the first item in the search response as input for a product recommendation search
* Retrieve reviews of the first 10 product recommendations
* Rank order the recommended products based upon the review sentiments

## Install

```
$git clone https://github.com/ZhengC1/CodeChallenge.git
or
download the zip
```

### Usage
```
The Sentiment Analysis will take about 20 to 30 seconds

$python CodeChallenge.py
```

### Testing
```
For this project, i would have preferred even a mock json file of customers and  
their purchases so that i could see to what percentage my recommendations aligned  
with their product purchases

The Test.py file is essentially the CodeChallenge.py file but much wordier and prints out multiple reviews

$python Test.py
```

### Prerequisities

```
Python 2.7 +
Git
```
### Style

```
Uses PEP8 for python Style
```
## Built With

* Walmart Open API
* Natural Language Sentiment Analysis API
* Ubuntu 16.04
* Gnome-Terminal
* VIM - Visual Improved

## Assumptions for this Project

```
* assuming that "ordering the products based on review sentiment means sentiment analysis of reviews
* Using the first 5 reviews for each product
```

## Authors

* **Chun Zheng** - 
 * *Other projects* - [ZhengC1](https://github.com/ZhengC1?tab=repositories)
 * *Manual Implementation of Sentiment Analysis with Twitters API and NODEjs* - [AppHack7](https://github.com/ZhengC1/site_bias)


## Acknowledgments

* Thank you to all the programmers who made this possible - I.E. ME :D
* Thank you Walmart for making an API

[![Chun Zheng](http://www.gravatar.com/avatar/c439eea642425448f34f8ea49833a76e?s=144)](http://student.cs.appstate.edu/zhengc1)
