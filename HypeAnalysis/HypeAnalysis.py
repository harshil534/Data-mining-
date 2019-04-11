

#1. Calculate Hype Factor - alpha
#Parameters: num_of_distinct_users : num_of_tweets_all_users
def calculate_hype_factor(num_of_distinct_users, num_of_tweets_all_users):
	"""This function returns the alpha value"""
	alpha = num_of_distinct_users / num_of_tweets_all_users
	return alpha

#2. Calculate Reach Factor - zigma
#Parameters: follower_count : threshold
def calculate_reach_factor(follower_count, threshold):
	"""This function returns the zigma value"""
	zigma = (follower_count - threshold) / follower_count
	return zigma

#3. Calculate Final Hype - hype
#Parameters: alpha : zigma
def calculate_final_hype_every_hour (alpha, zigma):
	"""This function returns the hype value"""
	hype = (alpha + zigma) / 2
	return hype

#4. Calculate Box office Collection - BOC
#Parameters: hype : no_of_shows : avg_ticket_price
def calculate_boc (hype, no_of_shows, avg_ticket_price):
	"""This function returns the boc value"""
	boc = no_of_shows * hype * avg_ticket_price
	return boc
