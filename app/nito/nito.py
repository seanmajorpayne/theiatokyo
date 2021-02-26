from app.client.client import Client

class Nito(Client):
    def __init__(self):
        super().__init__()
        self.channel_id = "UCVWDm8aMhKc6cZSFLVV7I3g"
        self.video_ids = ["pu9Ty9fxTHE"]

    def get_views(self):
        try:
            return super().get_views()
        except:
            return "5,000,000"
