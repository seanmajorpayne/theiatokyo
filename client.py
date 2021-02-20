from google_api import GoogleApiConnect

class Client:
    self.name = None
    self.video_ids = None
    self.channel_id = None
    self.views = None
    self.subscribers = None
    self.api = GoogleApiConnect()

    def get_views(self):
        return self.views

    def get_subscribers(self):
        return self.subscribers

    def format_views(self):
        return format_int(self.views)

    def format_subscribers(self):
        return format_int(self.subscribers)

    def format_int(self, i):
        return locale.format_string("%d", i, grouping=True)

    def get_views(self):
        self.views = self.api.get_video_views(video_ids)
        views_as_string = self.format_views()
        return views_as_string

    def get_subscribers(self):
        subscribers_as_string = self.format_subscribers()
        return self.subscribers
