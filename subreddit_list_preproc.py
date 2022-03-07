from subreddit_list_rawdata import subreddits_1, subreddits_2, members


def preproc_rawdata(subreddits):
    """
    Takes in raw data of subreddits in form of dictionaries and labels and turns them into a list of subreddits
    """
    subreddits_list = []
    for k in subreddits.keys():
        for i in subreddits[k]:
            subreddits_list.append(i)
    return subreddits_list


all_subreddits = preproc_rawdata(subreddits_1) + preproc_rawdata(subreddits_2)
all_subreddits = map(lambda s: s.lower(), all_subreddits)
all_subreddits = list(set(all_subreddits))

# kinda hacky, if this isn't perfectly divided then it will cause an error in the next block
len_of_chunks = len(all_subreddits) // len(members)

chunks = [
    all_subreddits[x : x + len_of_chunks]
    for x in range(0, len(all_subreddits), len_of_chunks)
]

for i, arr in zip(members, chunks):
    with open(f"{i}.txt", "w") as f:
        for item in arr:
            f.write("%s\n" % item)
