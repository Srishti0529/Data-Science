import json

# Open the initial raw data and read it
# After completion of collection of data we use final data
with open(
    "finaldata.txt", encoding="utf-8"
) as f:  # encoding='utf-8' ensures all characters (emoji, Hindi text, symbols) are read safely.
    data = f.read()

# Split each ID and if there are min 3 parts in the chunk then split it
chunks = data.split("\n\n")
chunks = [c for c in chunks if len(c) > 3]
# Some chunks may be empty (like "")
# This keeps only chunks that have more than 3 characters.


# Converted the whole data to a dictionary
def parse_chunk(chunk):
    chunk = chunk.strip()
    sep_chunk = chunk.split("\n")
    username = sep_chunk[0]
    no_of_posts = int(sep_chunk[1].split(" post")[0].replace(",", ""))
    no_of_followers = float(
        sep_chunk[2]
        .split(" follower")[0]
        .replace(",", "")
        .replace("K", "")
        .replace("M", "")
    )
    if "K" in sep_chunk[2]:
        no_of_followers = int(no_of_followers * 1000)
    elif "M" in sep_chunk[2]:
        no_of_followers = int(no_of_followers * 1000000)
    else:
        no_of_followers = int(no_of_followers)

    no_of_following = float(
        sep_chunk[3]
        .split(" following")[0]
        .replace(",", "")
        .replace("K", "")
        .replace("M", "")
    )
    if "K" in sep_chunk[3]:
        no_of_following = int(no_of_following * 1000)
    elif "M" in sep_chunk[3]:
        no_of_following = int(no_of_following * 1000000)
    else:
        no_of_following = int(no_of_following)

    name = sep_chunk[4]
    if len(sep_chunk) > 5:
        type_of_page = sep_chunk[5]
        bio = "\n".join(sep_chunk[6:])
    else:
        type_of_page = "Unknown"
        bio = ""
    # print(username, no_of_posts, no_of_followers, no_of_following, name, type_of_page, bio, sep="\n")
    return {
        "username": username,
        "no_of_posts": no_of_posts,
        "no_of_followers": no_of_followers,
        "no_of_following": no_of_following,
        "name": name,
        "type_of_page": type_of_page,
        "bio": bio,
    }


# Stored it in a list
all_chunks = []
for chunk in chunks:
    parsed_chunk = parse_chunk(chunk)
    all_chunks.append(parsed_chunk)

# Created a json file for the data
with open("s.json", "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, indent=4)
