class BaseConfig(object):
    """BASE CONFIGURATION"""
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Guz48074$@localhost:3306/my_tests"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    """PRODUCTION CONFIGURATION"""
    DEBUG = False
    PORT = 5004


class DevelopmentConfig(BaseConfig):
    """DEVELOPMENT CONFIGURATION"""
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo'
