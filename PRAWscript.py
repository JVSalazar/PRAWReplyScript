import praw
import re

username = raw_input('Enter username: ')
password = raw_input('Enter password: ')
subreddit = raw_input('Enter subreddit: ')


# username = 'JohnPRAWtest'
# password = 'johnprawtest****'
# subreddit = 'test'


r = praw.Reddit(user_agent='Test Script by /u/JohnPRAWtest')

r.login(username, password, disable_warning=True)

submissions = r.get_subreddit(subreddit).get_hot(limit=10)


pattern = raw_input('Enter regular expression to search: ')
reply = raw_input('Enter reply: ')

already_done = set()
for submission in submissions:
	flat_comments = praw.helpers.flatten_tree(submission.comments)
	for comment in flat_comments:
		matchFound = re.search(pattern, comment.body)
		if matchFound and comment.id not in already_done:
			comment.reply(reply)