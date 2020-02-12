# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery
import json

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    developer_key = "AIzaSyDNomfOyRprmwTJzaQOYzNgWQY1PtQ7PGs"

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developer_key)

    request = youtube.playlists().list(
        part="id,snippet,contentDetails",
        channelId="UCtjFs76rnGY2AKH17iRoWww",
        maxResults=1,
        pageToken=2
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()