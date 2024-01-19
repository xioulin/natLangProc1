import praw
import klucze

reddit=praw.Reddit(
    client_id=klucze.client_id,
    client_secret=klucze.client_secret,
    user_agent="testscript by u/Steelkilt",
    redirect_uri='https://localhost:8081'
)

subreddit= reddit.subreddit('Catholicism')


top_posts= subreddit.top(limit=5)
new_posts= subreddit.new(limit=5)

for posts in top_posts:
    print(posts.title)


post= reddit.submission(id='h0qb82')
print(post.title)
comments= post.comments

for comment in comments[:2]:
    print(comment.body)

# print(reddit.auth.url(scopes=['identity'],state="...d",duration="permanent"))
# code='TCqYNX0uK-SkQO_loAdEaok0kcq0YQ#_'
# print(reddit.auth.authorize(code))
# print(reddit.user.me())