from google_api import GoogleApiConnect
import locale

class Client:
    def __init__(self):
        """
        Clients have testimonial pages which require views,
        subscribers, and other client data to populate page
        information.
        """
        self.name = None
        self.video_ids = None           # list of Strings
        self.channel_id = None          # String
        self.views = 0
        self.subscribers = 0
        self.api = GoogleApiConnect()
        locale.setlocale(locale.LC_ALL, 'en_US')

    def get_views(self):
        """ Returns client views as Int"""
        return self.views

    def get_subscribers(self):
        """ Returns client subscribers as Int"""
        return self.subscribers

    def get_views(self):
        """
        Queries Google API for the client's video views
        :returns views (ex. "1,240,340")
        """
        self.views = self.api.get_video_views(self.video_ids)
        views_as_string = self.format_views()
        return views_as_string

    def format_views(self):
        """
        :Returns views in comma separated string format
        """
        return locale.format_string("%d", self.views, grouping=True)

    def get_subscribers(self):
        """
        Queries Google API for the client's subscriber views
        :returns subscribers (ex. "1,240,340")
        """
        subscribers_as_string = self.format_subscribers()
        return self.subscribers


    def format_subscribers(self):
        """
        :Returns subscribers in comma separated string format
        """
        return locale.format_string("%d", self.subscribers, grouping=True)