import json
file_period = open('twitter_periods_info.txt', 'w')
file_period.write('twitter start from          end by:                number of twitter: \n')
with open('Twitter_accounts.txt', 'r') as f:
	for files in f.readlines():
		files = files.rstrip('\n')
		filename = 'user_timeline_'+files+'.jsonl'
		with open(filename, 'r') as f1:
			tmp = f1.readlines()
			num_twitter = len(tmp)
			last_twitter_time = json.loads(tmp[0])["created_at"]
			first_twitter_time = json.loads(tmp[num_twitter-1])["created_at"] 
			file_period.write(files+'    '+first_twitter_time+'    '+last_twitter_time+'     '+str(num_twitter)+'\n')
file_period.close()

