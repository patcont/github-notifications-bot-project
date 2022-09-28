# github notifications bot project

github notifications discord bot project

# Installation instructions.

## virtualenv

> python -m venv venv

This instruction will work on POSIX system. ie, in Windows probably won't work

> source venv/bin/activate

This may be different on windows, take a look here https://docs.python.org/3/library/venv.html
Search for "activate" in your browser, and take a look at the table with headers:

Platform | Shell | Command to activate virtual environment

If you are using Windows, take a look at the row that reads "Windows", there 

To read the dependencies and start using the project, run this command:

> pip install -r requirements.txt

I didn't test it. Please remove this last comment if you didn't have any problems. Otherwise, write here what you did to fix the problem

## Environment variables

This project needs two environment variables to work on production

There is an example file called `.env.example`. This file should be copied and renamed as `.env`. .env file is git-ignored. Inside this file, replace the dummy values by the values of your tokens. Here is an explanation about these two tokens:

- Github token, to get your github notifications. Go to [this page](https://github.com/settings/tokens/new) to generate your token. Up until now, all permissions are needed to work. I don't know which are the unnecesary permissions that you can leave unchecked to generate your token. This is a pending issue.
- Discord token. TODO: put the link here to get your discord token, add any explanation necessary to get your token.
