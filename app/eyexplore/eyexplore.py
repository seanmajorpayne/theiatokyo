from app.client.client import Client

class Eyexplore(Client):

    def __init__(self):
        super().__init__()
        self.channel_id = "UC4T6TqCs8MD3fE32ROVjEsg"
        self.video_ids = [
            "JK-lDGYBK2k",      # Better Street Photos
            "-DwLO7cb1F0",      # Silhouette
            "d_P3DI0P41c",      # Learn from Master
            "j0juegm9jFA",      # Panning
            "ElH3MeBN42w",      # Stick it in
            "biPkaaqyl_Q",      # Negative Space
            "t-_PlUJvU1s",      # Zoom Blur
            "QFMUcSmJn1Y",      # Smart Camera
            "nSVVASoaroM",      # Long Exposure
            "Bo5s9zgNTOw",      # Halloween
            "q5dZZG43ayc",      # Exposure Comp
            "BC7Zyu-zr1Q",      # Read Histogram
            "eSNCeOmHKkA",      # Autofocus
            "1mOXirhofM8",      # Manual Focus
            "20HtSDYsfXo",      # Street Photo Settings
            "q5dZZG43ayc",      # Exposure & f-stops
            "XGVWrlmx07E",      # Depth of Field
            "BcWc1QxHBqM",      # Architecture Nakagin
            "FZOQNf_VVXo",      # Zone Focus
            "5oPZZEXibjo",      # Love Camera
            "6JDTmWEZam4",      # Metering Mode
            "McSsT3MgaEQ",      # Best Autofocus
            "2GNnQZUfBBw",      # Work the Scene
            "RlbuxY78P94",      # Street Photo Ideas
            "6D2CbQdVAgE",      # Japan Photo Tips
            "KSnWHWqDZ2k",      # Geisha Interview
            "GlC6jI8FM4Y",      # Geisha Photo Shoot
        ]

    def get_subscribers(self):
        """
        Eyexplore's subscribers can't be pulled from video data,
        so using an approximation based on YT graphs for now.

        :returns subscriber count as String
        """
        return "9,400"

    def get_views(self):
        """
        Gets Eyexplore View Count in format "XXX,XXX,XXX"

        :returns views as String
        """
        try:
            return super().get_views()
        except:
            return "216,827"    # Last known value


