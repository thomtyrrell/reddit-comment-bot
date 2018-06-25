import RedditBot

recovery_bot = RedditBot.RedditBot("Recovery Bot")

# get submissions from last 24 hours
recent_posts = recovery_bot.subreddit.top(time_filter="day")

# aggregate comments
comments = []
for submission in recent_posts:
    submission.comments.replace_more(limit=0)
    comments += list(filter(recovery_bot.should_respond, submission.comments.list()))
    recovery_bot.console_log("Gathering comments from submission \"" + submission.title + "\"")

if comments:
    recovery_bot.scan(comments)