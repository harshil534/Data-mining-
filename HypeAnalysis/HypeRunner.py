
import sys
import HypeAnalysis as ha
import csv
import sys
import pandas as pd

arg = sys.argv[1]
name =[]
df = pd.read_csv(arg + ".csv", usecols=[2])
#print  df.nunique()

a = int(filter(str.isdigit, str(df.nunique())))
b = str(a)
distinctCount = b[:-2]

x = int(filter(str.isdigit, str(df.count())))
y = str(x)
tweetCount = y[:-2]

distinctCount = float(distinctCount)
tweetCount = float(tweetCount)

# Test Data
# num_of_distinct_users:(distinct users having an average follower count of 93 which can be taken as the thresh-hold.)
nodu = distinctCount
# num_of_tweets_all_users:(The numbers of relevant tweets per second)
notau = tweetCount
# follower_count: (Considering a user with 114 followers)
fc = 114.0
# threshold: (Average follower count of 93)
th = 100.0
# no_of_shows: (The number of shows per day in all screens together for the weekend)
nos = 1600
# avg_ticket_price: 5000 (The average price of all tickets per screen per show)
atp = 5000
#Box Office Average Amount
boxh = 3000000.00
#Box Office Hit Amount
boxsh = 4000000.00
#Box Office Blockbuster Amount
boxbb = 6000000.00

#OutPut: Distinct Twitter User Count
print("Distinct Twitter User Count : " + str(distinctCount))

#OutPut: Tweets Count
print("Tweets Count : " + str(tweetCount))

#OutPut: Equation 01 - Hype Factor
print("Hype Factor (Alpha) : " + str(ha.calculate_hype_factor(nodu, notau)))

#OutPut: Equation 02 - Reach Factor
print("Reach Factor (Zigma) : " + str(ha.calculate_reach_factor(fc, th)))

#OutPut: Equation 03 - Final Hype
print("Final Hype (Hype) : " + 
str(ha.calculate_final_hype_every_hour(ha.calculate_hype_factor(nodu, notau), ha.calculate_reach_factor(fc, th))))

#OutPut: Equation 04 - Box office Collection
bo_collection = ha.calculate_boc(ha.calculate_final_hype_every_hour(ha.calculate_hype_factor(nodu, notau), 
										ha.calculate_reach_factor(fc, th)), nos, atp)
print("Box Office Collection (BOC) : " + str(bo_collection))

#Movie Success Classification
if ( bo_collection >= boxh and bo_collection < boxsh) : print "This Movie will be AVERAGE"
elif ( bo_collection >= boxsh and bo_collection < boxbb) : print "This Movie will be a HIT"
elif ( bo_collection >= boxbb ) : print "This Movie will be a BLOCKBUSTER"
else : print "This Movie will be a FLOP"

print "++ Hype Analysis Done ++"


