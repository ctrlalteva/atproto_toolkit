# AT Protocol Toolkit

## Overview
Collection of scripts for exploring social networks using the AT Protocol.

## Setup
1. Run `poetry install`
2. Create a .env file in the root of your project using the below template. The default Bluesky url is provided in the example.
```
ATP_USERNAME=
ATP_PASSWORD=
BASE_URL="https://bsky.social"
```
3. Run the top level scripts.

## Using
### common_followers.py
Returns a set of followers that are following all of the target dids.

Input: Create a plain text file containing the dids that the script will target. Script is expecting one did per line.

`poetry run python common_followers.py example_did_file.txt`
