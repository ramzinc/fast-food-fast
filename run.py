from flask import Flask
#from api.httpapi import app
from api.views.viewhandle import app
if __name__ == '__main__':
    Flask.run(app)
