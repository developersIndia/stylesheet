import praw
import requests
import os

# Reddit API credentials
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
USER_AGENT = 'CSS update script'  
SUBREDDIT_NAME = 'developersIndia'

# GitHub CSS file URL
GITHUB_CSS_URL = 'https://raw.githubusercontent.com/developersIndia/stylesheet/main/src/main.css'

def download_css_from_github():
    response = requests.get(GITHUB_CSS_URL)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to download CSS file from GitHub: {response.status_code}")
        return None

def update_css_on_reddit(css_content):
    # Authenticate with Reddit
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         username=USERNAME,
                         password=PASSWORD,
                         user_agent=USER_AGENT)


    subreddit = reddit.subreddit(SUBREDDIT_NAME)


    try:
        subreddit.stylesheet.update(css_content)
        print("CSS updated successfully on Reddit")
    except Exception as e:
        print(f"Failed to update CSS on Reddit: {e}")

def main():

    css_content = download_css_from_github()
    if css_content:

        update_css_on_reddit(css_content)
    else:
        print("Failed to update CSS on Reddit")

if __name__ == "__main__":
    main()
