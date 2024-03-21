import praw

from keys import CLIENT_ID, CLIENT_SECRET, USER_AGENT

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
)

subreddit = reddit.subreddit("python")

top_posts = subreddit.top(limit=10)
new_post = subreddit.new(limit=10)

for post in top_posts:
    print("post_id: ", post.id)
    print("Author: ", post.author)
    print("image: ", post.url)
    print("Score: ", post.score)
    print("Comment count: ", post.num_comments)
    print("\n")
    post = reddit.submission(id=post.id)
    comments = post.comments
    for comment in comments[:2]:
        print("printing comment: ")
        print("Comment body: ", comment.body)
        print("Author: ", comment.author)
        print("\n")
