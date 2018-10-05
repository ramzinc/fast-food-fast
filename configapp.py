class Config(object):
     DEBUG = False
     DATABASE_URI= "fast_food_fast_testing"

class developmentConf(Config): 
    DEBUG = True
    DATABASE_URI= "fast_food_fast_testing"


class productionConf(Config):
    DEBUG= False
    DATABASE_URI= "fast_food_fast_prod"