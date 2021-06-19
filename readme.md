**Description:**
This is python script I made to post on twitter as crypto from Apex legends.

**How it works:**
I have a txt file with a list of quotes that Crypto uses in the game.
(If you wanted to do the same thing for a different fictional character or other use case you could replace all the text in the txt file 
with random quotes you want posted).
I then have hashtags hardcoded that gets added to the randomly selected quote. 
After the quote and hashtag gets combined it gets posted to twitter with tweepy.

**How to use:**
Sign up for a developer account with twiiter and supply your API credentials to under the def twitterPost() function.
Replace the hashtags with ones you'd like added to the end of your post.
Replace the quotes.txt file with quotes you'd like posted. 
You will need to define the file path one line 6 where it has 'quotes.txt' should be replaced with something similiar to 'c://user/downloads/quotes.txt' 
You can run manually whenever you like or use cronjobs or task-scheduler to have it run as often as you'd like.

To follow the acccount I made this for: https://twitter.com/Crypto30446239
