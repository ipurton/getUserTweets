import tweepy

__author__ = 'ipurton'

# This script runs a search using Twitter's API for a specific hastag within a single user's timeline.
# Found tweets are printed into a text file with date included.
# Isaac Purton, 10/3/2015

# Revision Log:
# 10/3/2015	IP
# Fleshed out script, formatted and commented.

# Define api_file, file from which private Twitter API items are read
api_file = "twitterAccess.txt"

# Read in lines from api_file into a list
with open(api_file) as f:
    api_items = list(f)

# api_items contains: CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

# Above method maintains the /n character, which needs to be removed for later calls
for i in range(3):
    api_items[i] = api_items[i].rstrip()

# Enter application authentication information
CONSUMER_KEY = api_items[0]
CONSUMER_SECRET = api_items[1]
ACCESS_KEY = api_items[2]
ACCESS_SECRET = api_items[3]
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Define the text to search for
user = "ipurton" 
	# specific user timeline to query
hashtag = "songoftheday" 
	# specific hashtag to search for
start_date = "2015-09-29" 
	# script will look at all tweets made after this date; replace with id attributes from Twitter API?
query = "from:" + user + "+#" + hashtag + "+since:" + start_date 
	# define full query

# Run search, returning all found statuses as a list
tweet_list = [status for status in api.search(q = query)]

# Define file name for the outputted text file
file_name = hashtag + "Posts_from" + user + ".txt"

# Write out tweet_list to file_name
with open(file_name, mode="wt", encoding="utf-8") as myfile:
	for tweet in tweet_list:
		text_to_print = str(tweet.text)
			# Pull out text of tweet.
		text_to_print = text_to_print.replace("&amp;", "&") 
			# Ampersands are url-coded, need to be refortmatted
		date_to_print = str(tweet.created_at) 
			# Pull out date/time information for tweet. Characters 0:10 are the date, rest is time
		to_write = date_to_print[0:10] + "\n" + text_to_print + "\n\n"
			# Perform basic formatting, store above into a single string
		myfile.write(to_write)
			# Write string to end of text file
		