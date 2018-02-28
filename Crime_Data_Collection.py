import twitter, sys, json

reload(sys)
sys.setdefaultencoding("utf-8")

myApi = twitter.Api(consumer_key='n4yrM11So7LpgymAzOrWNdQNa',
                    consumer_secret='9AsTuUagKegcZ18Bo6YOgURhGD6CXGpBvjr7lfRIWbQf8reFJ2',
                    access_token_key='315734324-hSShwxdTkuyHEPWDJlWnEf92Rh2ObWj23jdrMT3P',
                    access_token_secret='NRkHKggHWKLn3OTMWtrdAtqHGj9Z0cOJrHFT7JIVjZ4KT')


def get_m():
    query = 'traffic OR jam OR congestion OR accident OR car OR bus OR road OR lane OR highway OR crash OR collision OR traffic jammed OR road closed'
    geo = [40.730610, -73.935242, "150mi"]  # New York City

    file1 = open('M_data_user_id.txt', 'w')
    file2 = open('M_data_text.txt', 'w')
    file3 = open('M_data_tweet_id.txt', 'w')

    for it in range(1):  # Retrieve up to 200 tweets
        tweets = myApi.GetSearch(term=query, geocode=geo, count=100, result_type='recent')

        with open('M_data_tweets.txt', 'w') as file4:
            for tweet in tweets:
                file4.write(str(tweet))
        if tweets:
            for tweet in tweets:
                file2.write(str(tweet.text) + '\n')
                file1.write(str(tweet.user.id) + '\n')
                file3.write(str(tweet.id) + '\n')


def get_d():

    f1 = open('D_data_tweets.txt', 'w')
    f2 = open('D_data_tweet_id.txt', 'w')
    f3 = open('D_data_tweet_text.txt', 'w')

    with open('M_data_user_id.txt') as f:
        users = f.read().split('\n')


    for id in users:
            status = myApi.GetUserTimeline(id)
            for tweet in status:
                f1.write(str(tweet) + "\n")
                f2.write(str(tweet.id) + "\n")
                f3.write(str(tweet.text) + "\n")

def main():
    print "\n\n\n************ get_m() ****************\n"
    get_m()

    print "\n\n\n************ get_d() ****************\n"
    get_d()
    print '******************* END of get_d()*********************'
    pass


if __name__ == '__main__':
    main()

"""
Without filtering on location, retrieve tweets that contain the phrase 'road accident'. 
Note that if the query is 'road accident' instead of '"road accident"', then the 
returned queries will match both 'road' and 'accident' but not the phase "road accident"
"""
"""
Retrieve tweets that are related to traffic congestions in the city of Albany 
"""
