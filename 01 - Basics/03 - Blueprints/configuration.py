class BaseConfig(object):
    """BASE CONFIGURATION"""
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False


class ProductionConfig(BaseConfig):
    """PRODUCTION CONFIGURATION"""
    DEBUG = False
    PORT = 5004


class DevelopmentConfig(BaseConfig):
    """DEVELOPMENT CONFIGURATION"""
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo'
