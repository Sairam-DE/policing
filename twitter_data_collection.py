#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tweepy


# In[ ]:


def printtweetdata(n, ith_tweet):
        print()
        print(f"Tweet {n}:")
        print(f"Username:{ith_tweet[0]}")
        print(f"Description:{ith_tweet[1]}")
        print(f"Location:{ith_tweet[2]}")
        print(f"Following Count:{ith_tweet[3]}")
        print(f"Follower Count:{ith_tweet[4]}")
        print(f"Total Tweets:{ith_tweet[5]}")
        print(f"Retweet Count:{ith_tweet[6]}")
        print(f"Tweet Text:{ith_tweet[7]}")
        print(f"Hashtags Used:{ith_tweet[8]}")


# In[ ]:


def scrape(words, date_since, numtweet):
        # Creating DataFrame using pandas
        db = pd.DataFrame(columns=['username',
                                   'description',
                                   'location',
                                   'following',
                                   'followers',
                                   'totaltweets',
                                   'retweetcount',
                                   'text',
                                   'hashtags'])

        tweets = tweepy.Cursor(api.search_tweets,conda install -n notebook_env nb_conda_kernels

                               since_id=date_since,
                               tweet_mode='extended').items(numtweet)

        list_tweets = [tweet for tweet in tweets]

        i = 1

        for tweet in list_tweets:
                username = tweet.user.screen_name
                description = tweet.user.description
                location = tweet.user.location
                following = tweet.user.friends_count
                followers = tweet.user.followers_count
                totaltweets = tweet.user.statuses_count
                retweetcount = tweet.retweet_count
                hashtags = tweet.entities['hashtags']
                
                try:
                        text = tweet.retweeted_status.full_text
                except AttributeError:
                        text = tweet.full_text
                hashtext = list()
                for j in range(0, len(hashtags)):
                        hashtext.append(hashtags[j]['text'])
                
                ith_tweet = [username, description,
                             location, following,
                             followers, totaltweets,
                             retweetcount, text, hashtext]
                # tweet_dict.append({"Username" : username, "Description" : description, "Location" : location, "Following" : following, "Followers" : followers, "TotalTweets" : totaltweets, "Retweets" : retweetcount, "Hashtags" :  })
                db.loc[len(db)] = ith_tweet
                # printtweetdata(i, ith_tweet)
                i = i+1

        return db


# In[ ]:





if __name__ == '__main__':
        #initialise keys here

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        words = 'bjp national executive committee meeting'
        date_since = '2021-01-01'
        numtweet = 100
        db = scrape(words, date_since, numtweet)
#         db.to_csv('tweets.csv')


# In[ ]:


db.head()


# In[ ]:


unique_db = db.drop_duplicates(subset=['username'])
location_db = unique_db.groupby(['location'])['location'].size().reset_index(name='counts')
location_db['location'].replace('', np.nan, inplace=True)
location_db.dropna(subset=['location'], inplace=True)


# In[ ]:


location_db.plot(kind = 'bar',
        x = 'location',
        y = 'counts',
        color = 'green')
  
# set the title
plt.title('Unique users vs Location')
  
# show the plot
plt.show()


# In[ ]:




