import requests
import re

text = 'Madden the Football game everyone loves around the season and holidays. Sure enough the game has improvements and handles great. The game offers many different modes and ultimate team is still great with picking players you may have seen on espn classic or when you were younger. The game would be rated 5 stars if it wasn't for these issues. The commentary has been brutally terrible in recent years and this year is still ongoing. The commentary is boring,flat and doesn't keep up with the pace of the game. With the advanced controls on WR being YAC,Aggressive and Possession gives the WR an advantage if you throw it up to a tall receiver 9/10 they catch it so its kind of over powering and has your wonder He Really Caught That!!!!. All in all great game if you're a seasoned madden player you'll love hate some parts of the game but still good fun with friends and family.This was fun to play. Not only did it look good but I love the cross between actual game "footage" from the previous NFL season but is also showing the new rosters and everything that happened in free agency. Very up to date. Very fun.Lots of great detail. The faces look crazy realI love sports games. This is perfect for me.I enjoy playing this game. I did get this game for my son and he plays it a lot. '

text = re.sub(r'[^\w]', ' ', text)

req = requests.post("http://text-processing.com/api/sentiment/", data={'text': str(text)})
print req.status_code
print req.json()
