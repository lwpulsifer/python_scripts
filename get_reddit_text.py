import praw

reddit = praw.Reddit("bot1", user_agent="bot1 user agent")

bandnames = reddit.subreddit("BandNames")

with open("bandnames.txt", "w") as names_file:
    for submission in bandnames.hot(limit=100000):
        try:
            names_file.write(submission.title)
            names_file.write("\n")
            print(f"Wrote {submission.title}")
        except UnicodeEncodeError as e:
            print(f"Failed to write {submission.title}")
    