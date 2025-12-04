# A simple script to practice fetching data from Reddit API
# for educational purposes.
import praw

def get_latest_titles():
    # Read-only instance
    reddit = praw.Reddit(...)
    print("Fetching titles for data analysis practice...")
    # Just printing titles to console
    for submission in reddit.subreddit("learnpython").hot(limit=5):
        print(submission.title)

if __name__ == "__main__":
    get_latest_titles()
