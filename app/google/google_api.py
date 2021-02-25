import os
import json

# from dotenv import load_dotenv    MOVE TO INIT FILE
# load_dotenv()

import google_auth_oauthlib.flow
from googleapiclient.discovery import build
import googleapiclient.errors


class GoogleApiConnect:
    def __init__(self):
        """
        Creates a Google API Connection which is used to pull Youtube data.
        The data contains statistics for Theia Tokyo produced Youtube videos.
        """
        self.youtube = None  # Build object to connect to API
        self.channel_data = None  # JSON
        self.video_data = None  # JSON
        self.views = 0
        self.subscribers = 0
        self.build_service()

    def build_service(self):
        """
        Creates a build object which informs google which service
        and account data to access.

        :return: None
        """
        api_service_name = "youtube"
        api_version = "v3"
        api_key = os.environ.get("API_KEY")
        self.youtube = build(
            api_service_name,
            api_version,
            developerKey=api_key,
        )

    def request_channels(self, url_id):
        """
        Sends an API request to Google to request Youtube
        Channel data

        :param url_id: String identifier for a YT Channel
        :returns json response if found
        """
        try:
            request = self.youtube.channels().list(
                part="statistics",
                id=url_id,
            )
            return request.execute()

        except errors.HttpError as err:
            print("Error requesting channels from Google API with id: ", url_id)
            print(err._get_reason())
            return None

    def get_client_counts(self, clients):
        """
        Calculates the views and subscribers all clients have earned
        from Theia Tokyo produced videos.

        :param clients: Dictionary of clients & their channel IDs
        :return: None
        """
        self.channel_data = self.request_channels(
            ",".join([id for channel, id in clients.items()])
        )
        for i in range(len(clients)):
            self.views += int(self.channel_data["items"][i]["statistics"]["viewCount"])
            self.subscribers += int(
                self.channel_data["items"][i]["statistics"]["subscriberCount"]
            )

    def request_videos(self, url_id):
        """
        Sends an API request to Google to request Youtube
        video data.

        :param url_id: String identifier for a YT Video
        :returns json response if found
        """
        try:
            request = self.youtube.videos().list(
                part="statistics",
                id=url_id,
            )
            return request.execute()

        except errors.HttpError as err:
            print("Error requesting videos from Google API with id: ", url_id)
            print(err._get_reason())
            return None

    def get_video_views(self, videos):
        """
        Calculates the views and subscribers for a list of videos
        that Theia Tokyo has produced.

        :param videos:
        :return:
        """
        self.video_data = self.request_videos(",".join([video for video in videos]))
        for i in range(len(videos)):
            self.views += int(self.video_data["items"][i]["statistics"]["viewCount"])

        return self.views
