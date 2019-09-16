import tweepy
import time
print("this is my tb")
CONSUMER_KEY = "W51UPQ81AcL9zxqoCl4x8jUSq"
CONSUMER_SECRET = "g5oJxdhnpRDNJXqZag0VPWwmLHqDdILHhYS3XLGBOtp1u3ujJw"
ACCESS_KEY = "1112454655601270789-gzz2vSOLp5Yed8Y39WVMMj16GjgVlj"
ACCESS_SECRET = "y2ilqa8XuUPN3Cht7wx7RBUIXbJN0J4BHsT97CYN7bEuR"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
	print("replying to tweets... ")
	last_seen_id = retrieve_last_seen_id(FILE_NAME)
	mentions = api.mentions_timeline(
							last_seen_id,
							tweet_mode = "extended")

	for mention in reversed(mentions):
		print(str(mention.id) + " - " + mention.full_text)
		last_seen_id = mention.id
		store_last_seen_id(last_seen_id, FILE_NAME)
		if "#helloworld" in mention.full_text.lower():
			print("found #helloworld!")
			print("responding back...")
			api.update_status("@" + mention.user.screen_name + "Hello world back to you! JUST TEST 2", mention.id)

while True:
	reply_to_tweets()
	time.sleep(15)


"""

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(
						last_seen_id,
						tweet_mode = "extended")

for mention in reversed(mentions):
	print(str(mention.id) + " - " + mention.full_text)
	last_seen_id = mention.id
	store_last_seen_id(last_seen_id, FILE_NAME)
	if "#helloworld" in mention.full_text.lower():
		print("found #helloworld!")
		print("responding back...")


"""