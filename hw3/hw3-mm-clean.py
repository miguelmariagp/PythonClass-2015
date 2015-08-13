import tweepy
import time

#Get access to API
auth = tweepy.OAuthHandler('ngxu2QDxa4iFaR5FzJEiUgmlx', 'O3jid5dmt3d9LdMn1avLO0Kspnm1uQv1TSi6HL7eKfL0X9YgBX')
auth.set_access_token('3380145005-Jq06sx9qxxpXcDWmPWuuPoHyJIXVRVqen0X9BXA', 'RQZJOL5F5UZHSVSSrNfKWhzzkSSxMefQIA1r7CVogQ1kn')    
api = tweepy.API(auth)

patrick = api.get_user('senecadoane')
#list of his followers
pat_followers=patrick.followers_ids()


#This gives me the names of the most active 
#and most popular of Patrick's followers
max_tweets,max_followers=0,0

for follower in pat_followers:
	follower_user=api.get_user(follower)
	if follower_user.statuses_count>max_tweets:
		active_user=follower_user.screen_name
		max_tweets=follower_user.statuses_count
	if follower_user.followers_count>max_followers:
		pop_user=follower_user.screen_name
		max_followers=follower_user.followers_count
		
#1.1:
active_user
#@BraveLad

#1.2:
pop_user
#@BraveLad


pat_friends=api.friends_ids('senecadoane')
max_tweets_l,max_tweets_e, max_tweets_c,max_followers_l,max_followers_e,max_followers_c=0,0,0,0,0,0
for friend in pat_friends:
	friend_user=api.get_user(friend)
	if friend_user.followers_count<100:
		if friend_user.statuses_count>max_tweets_l:
			active_layman=friend_user.screen_name
			max_tweets_l=friend_user.statuses_count
	if friend_user.followers_count>=100 and friend_user.followers_count<1000:
		if friend_user.statuses_count>max_tweets_e:
			active_expert=friend_user.screen_name
			max_tweets_e=friend_user.statuses_count
	if friend_user.followers_count>1000:
		if friend_user.statuses_count>max_tweets_c:
			active_celebrity=friend_user.screen_name
			max_tweets_c=friend_user.statuses_count
	if friend_user.followers_count<100:
		if friend_user.followers_count>max_followers_l:
			pop_layman=friend_user.screen_name
			max_followers_l=follower_user.followers_count
	if friend_user.followers_count>=100 and friend_user.followers_count<1000:
		if friend_user.followers_count>max_followers_e:
			pop_expert=friend_user.screen_name
			max_followers_e=follower_user.followers_count
	if friend_user.followers_count>1000:
		if friend_user.followers_count>max_followers_c:
			pop_celebrity=friend_user.screen_name
			max_followers_c=follower_user.followers_count


#1.3 and 1.4:			
#Active and Popular friends, by type:
active_layman
#@kevinlig
active_expert
#@steveoslica
active_celebrity
#@dgoold
pop_layman
#@andrewperry87
pop_expert
#@twoodwa1
pop_celebrity
#@joelmchale, who is also the most popular of Patrick's friends.



###########################################
#####Here starts the second order part#####
###########################################

#2.1 - Most active follower (among first and second degrees of separation)
#This should give me the # of tweets made by
#the most active second order follower.
mamax_tweets=0

#list with info about all followers
one_degree=[]
for i in pat_followers:
	follows=api.get_user(i)
	one_degree.append(follows)
	time.sleep(2)
	
two_degrees=[]
#It doesn't work. It says I am not authorized.
for i in one_degree:
	two_degrees=i.followers()
	try:
		for second in two_degrees:
			if second.statuses_count>mamax_tweets:
				acactive_user=second.screen_name
				mamax_tweets=second.statuses_count
	except:
		pass

#Finally, I would only need to compare the number of tweets 
#from the most active first order follower (max_tweets)
#with the number of tweets from the most active second order follower (mamax_tweets)




#2.2 - Most active friend (among first and second degrees of separation)
#This should give me the # of tweets made by
#the most active second order follower.
mamax_tweets=0

#list with info about all followers
one_degree=[]
for i in pat_friends:
	friends=api.get_user(i)
	one_degree.append(friends)
	time.sleep(2)
	
two_degrees=[]
#It doesn't work. It says I am not authorized.
for i in one_degree:
	two_degrees=i.friends()
	try:
		for second in two_degrees:
			if second.statuses_count>mamax_tweets:
				acactive_user=second.screen_name
				mamax_tweets=second.statuses_count
	except:
		pass

#Finally, I would only need to compare the number of tweets 
#from the most active first order friend (max_tweets_c)
#with the number of tweets from the most active second order friend (mamax_tweets)