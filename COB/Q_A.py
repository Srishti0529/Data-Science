import json

# Load the JSON file
def load_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


# MAX Posts
def find_max_posts(all_chunks):
    max = 0
    for chunk in all_chunks:
        if max < chunk["no_of_posts"]:
            max = chunk["no_of_posts"]
            chunk_with_max_post = chunk
    return chunk_with_max_post


# MAX Followers
def find_max_followers(all_chunks):
    max = 0
    for chunk in all_chunks:
        if max < chunk["no_of_followers"]:
            max = chunk["no_of_followers"]
            chunk_with_max_followers = chunk
    return chunk_with_max_followers


# How manay categories
def type_of_categories(all_chunks):
    categories = set()
    for chunk in all_chunks:
        categories.add(chunk["type_of_page"])
    return categories


data = load_data("s.json")

max_posts = find_max_posts(data)
print("User with maximum posts: \n")
print(max_posts)
print("\n")

max_followers = find_max_followers(data)
print("User with maximum followers: \n")
print(max_followers)
print("\n")

categories = type_of_categories(data)
print("All type of categories:\n")
print(categories)
print("All categories:\n")
print(len(categories))
print("\n")
