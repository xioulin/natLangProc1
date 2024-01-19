import praw
import klucze

reddit=praw.Reddit(
    client_id=klucze.client_id,
    client_secret=klucze.client_secret,
    user_agent="testscript by u/Steelkilt",
    redirect_uri='https://localhost:8081'
)

subreddit= reddit.subreddit('ManchesterUnited')


# top_posts= subreddit.top(limit=10)
new_posts= subreddit.new(limit=10)
# hot_posts=subreddit.hot(limit=10)


# for posts in new_posts:
#     print("Title",posts.title)
#     print("id", posts.id)
#     print('score',posts.score)
#     print('num_comments',posts.num_comments)
#     print('\n')



post= reddit.submission(id='199t2pp')
comments= post.comments

import csv
with open('ten_hag.csv','w',newline='') as csvfile:
    filewriter= csv.writer(csvfile,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['author', 'comment'])
    for comment in comments:
        filewriter.writerow([comment.author,comment.body])


