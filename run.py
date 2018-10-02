from flask import Flask
#from api.httpapi import app
from api.controllers.viewhandle import app
if __name__ == '__main__':
    app.run()
