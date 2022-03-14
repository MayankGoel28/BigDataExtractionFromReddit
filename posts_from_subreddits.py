"""
To run

python comments_from_subreddits.py assigned_file_name.txt

Creates json files of each subreddit
"""
from pmaw import PushshiftAPI
import json
import sys

threads = 20

api = PushshiftAPI(num_workers=threads, limit_type="backoff", jitter="full")

subreddits_file = sys.argv[1]
f = open(f"{subreddits_file}")
subreddits = f.readlines()

def work(subreddit):
    posts = api.search_submissions(
        subreddit=subreddit, limit=50000, safe_exit=True, mem_safe=True
    )
    post_list = [post for post in posts]
    labels = ["author", "title", "selftext", "created_utc", "score"]
    final_data = []
    for post_data in post_list:
        minimal_data = {k: post_data[k] for k in labels if k in post_data}
        final_data.append(minimal_data)
        print(minimal_data)

    with open(f"{subreddit}.json", "w") as fout:
        json.dump(final_data, fout)

for subreddit in subreddits:
    subreddit = subreddit.strip()
    try:
        work(subreddit)
        with open('failed.txt', 'a') as f:
            f.write(subreddit + '\n')
    except:
        continue
