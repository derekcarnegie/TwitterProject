from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "781246716930514944-N8KzCm2w1HRoE8vEQFohkI7P3AgqJ9b"
access_token_secret = "HVlN35yqpEp0OYfweQ8Y38FJublbHaRGAsZPOWzk3KsuS"
consumer_key = "HC7WVi5tfl6abMZoBUMGKgkix"
consumer_secret = "zRNCqejkGrookAlRZ9KQhqs5cBq1OVbynY5Pkq872GaBO4MnTf"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])

































