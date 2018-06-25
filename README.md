# reddit-bot

RedditBot is a starter class.  To build your own reddit bot write a new class that inherits it.  Your
bot...

...must call the parent constructor and provide your own reddit instance (see https://www.reddit.com/wiki/api for instructions).

...also must overload the response() and should_respond() methods in the child class.

Once you've done that, create an object of your child class, call its scan() method, sit back, and let your bot run wild
all over (a sub)reddit!

As an example I've included recovery-bot.py, which constructs a bot instance and scans comments in the bot's defined subreddit for the last 24 hours.  I've also included tag_parser.py, which can detect pairs of delimiters {} and {{}} in a comment and return their contents (use get_tagged_articles(comment)).

