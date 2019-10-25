# Simple-Tweet-Sentiment-Analyzer
Author: Xavier Puspus
Organization: For the Women Foundation
Data Agency: Zero Six Research

# Description

This repository serves as a guide in building and hosting web apps with ml backend into a web server. In this case, we can serve it on [Heroku](heroku.com) which provides a free (up to some extent) and easy to use platform for deployment.

For this example, we use a simple tweet analyzer by pulling live tweets using `tweepy` and analyzing sentiment (positive, neutral, or negative) using `vaderSentiment`. Below details how its made.

# Directory

- *setup.sh*: Contains the shell script needed to deploy the web app in a web server (in our case, Heroku).
- *Procfile*: Contains the shell script needed to run the `tweet_analyzer_app.py` which loads the web app.
- *requirements.txt*: Has all the packages needed to install using `pip install -r requirements.txt`
- *tweet_analyzer_app.py*: Contains the code to extract tweets, execute sentiment analyzer and build the web app.
- *runtime.txt*: Stores the python version to run. Maintaining the same python version everytime the hosted web app is run is important for stability.
- *config.yml*: json file that contains your twitter developer token. For obvious reasons, I didn't push my configs to this repo but you can request from one through this [link](https://developer.twitter.com/en/apply-for-access.html). You will get 4 keys. Example is detailed below. In the same format, write it into your own `config.yml` file.

```
{
 "CONSUMER_KEY" : "someconsumerkey",
"CONSUMER_SECRET" : "someconsumersecretkey",
"ACCESS_TOKEN" : "someaccesstoken",
"ACCESS_TOKEN_SECRET" : "someaccesstokensecret"
}
```

# Local Hosting

In order to host the web app locally (in your computer), fork this repository into your computer, `cd` into the repo's directory, open a terminal and run:

```console
foo@bar:~$ streamlit run tweet_analyzer_app.py
```

# Display

The web app should look something like this:

![Sample image of the tweet sentiment analyzer web application.](sample_image.png)
