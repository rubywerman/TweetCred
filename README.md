# TweetCred
Crowdsource credibility scores for tweets

Twitter is great for reporting major news events and emergency situations. However, the social media site is also plauged by misinformation, leading to confusion, chaos, and sometimes even violence. Users generally question false information more than truthful information. 

In a study about tweets relating to a 2010 earthquake in Chile, the authors suggested that **social media favors valid information over fake news** [(“Information Credibility on Twitter | Proceedings of the 20th International Conference on World Wide Web” 2011)](https://dl.acm.org/doi/pdf/10.1145/1963405.1963500?casa_token=fT-mCQxJdmgAAAAA:3u5H1wE3wewb12eUMCkKnKiMOyDe2KgfCNneZv8Xh0Xk2KMpPjynEvhbvUfKGOd36Xp9vxFW1FFz). 

So, let's crowdsource! There are many great papers and projects aimed at analyzing the credibility of tweets. I'd rather like to explore how one might build a crowdsourcing forum that enables users to assess tweets for credibility.  

My steps:
* Retreive tweets from Twitter using the Twitter API and tweepy
* Create a project in Pybossa and add tasks using the Twitter Task importer
* Design a custom HTML script to prompt users with tweets and questions 
* ☆ﾟ.*･｡ﾟ credibility scoring ✧･ﾟ: *✧･ﾟ:* 
* World peace

## How I (tried) to do it 
* I installed Pybossa and configured a PostgreSQL database and `redis-server` and `redis-sentinel` instance using the Pybossa documentation 
* I experimented with a few different ways to gather tweets; for simplicity and time sake I used a script that pulls tweets by username, but if I had more time I would write a script that retrieved tweets off of key words and location
* I created a project in Pybossa and then edited the task HTML script to design what a task might look like to a user

<img src="https://i.imgur.com/cFvGBjR.png" data-canonical-src="https://i.imgur.com/cFvGBjR.png" width="400" height="200" />




Credits:
* I used the paper sited above (“Information Credibility on Twitter | Proceedings of the 20th International Conference on World Wide Web”) to help format what a task might look like
* I used @anku255's [gist](https://gist.github.com/anku255/0cebd75cce675f2b56de1ef48ec06575) to scrape tweets by a given username 

