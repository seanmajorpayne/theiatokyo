class BaseConfig(object):
    DEBUG = False
    CACHE_TYPE = "simple"
    Testing = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
