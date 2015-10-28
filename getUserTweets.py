import tweepy

__author__ = 'ipurton'

# This script runs a search using Twitter's API for a specific hashtag within
# a single user's timeline.
# Found tweets are printed into a text file with date included.
# Isaac Purton, 10/3/2015

# Revision Log:
# 10/27/2015    IP
# Revamped/reformatted script. Added ID elements, noted Search API limits.
# 10/3/2015	IP
# Fleshed out script, formatted and commented.

# Define api_file, file from which private Twitter API items are read
api_file = "twitterAccess.txt"

# Read in lines from api_file into a list
with open(api_file) as f:
    api_items = list(f)

# api_items contains: CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

# Above method maintains the /n character, which needs to be removed for
# later calls
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
file_name = hashtag + "Posts_from" + user + ".txt"
    # Define file name for the outputted text file

# This script outputs the ID of the most recent tweet found by a search to a
# txt file, file_name. This reads the ID outputted by the last session, and
# uses it to define the first tweet that this script should look at.
with open(file_name) as f:
    try:
        since_id = f.readline()
        print(since_id)
        since_id = since.id.rstrip()
    except:
        since_id = "655896169256611840"
            # Fallback ID if the above fails

query_items = [user, hashtag, since_id]
query = "from:{}+#{}+since_id:{}".format(*query_items)
    # define full query

# Run search, returning all found statuses as a list
# Twitter's public API only searches through tweets made in the past ~10 days.
tweet_list = [status for status in api.search(q = query)]

# Pull the ID of the most recent tweet as a string
max_id = tweet_list[0].id_str + "\n\n"

# Write out tweet_list to file_name
with open(file_name, mode="wt", encoding="utf-8") as myfile:
    myfile.write(max_id)
    for tweet in tweet_list:
        text_to_print = str(tweet.text)
            # Pull out text of tweet.
        text_to_print = text_to_print.replace("&amp;", "&") 
	    # Ampersands are url-coded, need to be reformatted
        date = tweet.created_at # this is a datetime object
        date_to_print = date.strftime("%B %d, %Y")
            # print month, day, and year in a formatted string
            # The day returned by this is one day ahead???
        to_write = text_to_print + ": " + date_to_print + "\n\n"
            # Perform basic formatting, store above into a single string
        myfile.write(to_write)
            # Write string to end of text file
