import os
from dotenv import load_dotenv
from atproto import Client
from utils.follower_utils import get_follower_dids


def get_common_followers(filename):
    # load and set up env variables
    load_dotenv()
    username = os.getenv("ATP_USERNAME")
    password = os.getenv("ATP_PASSWORD")
    base_url = os.getenv("BASE_URL")

    # create client
    client = Client(base_url)
    client.login(username, password)

    # load target dids from file
    target_dids = []
    with open(filename) as file:
        target_dids = file.read().splitlines()

    # get followers for each did
    followers = []
    for target_did in target_dids:
        follower = get_follower_dids(target_did, client)
        followers.append(follower)

    # identify common followers among target dids
    common_followers = set.intersection(*[set(list) for list in followers])

    # print results
    for follower in common_followers:
        follower = follower + (client.get_profile(follower[0]).follows_count,)
        print(follower)
    print(len(common_followers))

if __name__ == "__main__":
    from sys import argv
    get_common_followers(argv[1])