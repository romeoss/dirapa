#No need to duplicate effort. Why parse our own XML when somebody made a library for this task?
import feedparser
#We want notifications
from gi.repository import Notify
#We need to mkdirs
import os
#We need to download things
import urllib

posts = 1
feeds = "./data/feeds.txt"
feedList = []


def notify(header, description):
	Notify.init(header)
	notification = Notify.Notification.new(header, description)
	notification.show()


def downloadEpisodes(podcast):
	i = 0
	while i < posts:
		#Declare all the things we will need. 
		feedName = podcast.channel.title
		homePath = os.getenv("HOME")
		feedPath = homePath + "/Podcasts/" + feedName 
		episodeURLString = podcast.entries[i].enclosures[0].href
		episodeFilename = episodeURLString.split('/')[-1]
		episodeName = podcast.entries[i].title_detail.value
		episodeNameItalic = "<i>" + episodeName + "</i>"
		episodePath = homePath + "/Podcasts/" + feedName + "/" + episodeFilename
		newEpisode = "false"


		#Make the path for episodes if it doesn't already exist.
		if not os.path.exists(feedPath):
			os.makedirs(feedPath)

		#Download the latest episode if it hasn't been already
		if not os.path.exists(episodePath):
			urllib.request.urlretrieve(episodeURLString, episodePath)
			newEpisode = "true"

		#Notify user that episode has been downloaded if it's new.
		if newEpisode == "true":
			notify(feedName , episodeNameItalic)


		#In case the user wants to be checking for  more than one episode
		i+=1


def getFeeds():
	feedList = []
	feedListStripped = []


	#Open up the file
	file = open(feeds)


	#Read the lines from the file
	for line in file:
		feedList += [line]


	#Strip the /n from each element in feedList, and put the resulting element in feedListStripped
	for element in feedList:
		newElement = element.strip('\n')
		feedListStripped += [newElement]
	file.close


	#Give us back feedListStripped so that we can use it outside of this def. 
	return feedListStripped


#Get all of our feeds from feeds.txt
feedList = getFeeds()
#Send all of our feeds into downloadEpisodes()
for subscription in feedList:
	feed = feedparser.parse(subscription)
	downloadEpisodes(feed)
