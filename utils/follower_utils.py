from atproto import Client

def get_follower_dids(target_did: str, client: Client):
    followers = []
    cursor = None
    while True:
        data = client.get_followers(actor=target_did, cursor=cursor, limit=100)
        for account in data.followers:
            followers.append((account.did, account.handle))
        if not data.cursor:
            break
        cursor = data.cursor

    return followers

if __name__ == "__main__":
    raise SystemExit(0)