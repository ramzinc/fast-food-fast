class Config(object):
     DEBUG = False
     DATABASE_URI= "postgres://postgres@localhost:5432/fast_food_fast_prod"

class developmentConf(Config): 
    DEBUG = True
    DATABASE_URI= "postgres://postgres@localhost:5432/fast_food_fast_testing"


class productionConf(Config):
    DEBUG= False
    DATABASE_URI= "postgres://postgres@localhost:5432/fast_food_fast_prod"