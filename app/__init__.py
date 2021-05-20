from sanic import Sanic

from .routes import blueprints

def createApp():
    app = Sanic(__name__)

    for i in blueprints:
        app.blueprint(i)

    return app