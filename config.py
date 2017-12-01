class Config(object):
    """
    Common configurations
    """
    #put any configuration here that are common across all enviroments
class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO=True
class ProductionConfig(Config):
    """
    Production configurations
    
    """
    DEBUG=False
    
app_config= {
    'development': DevelopmentConfig,
    'production': ProductionConfig
    }