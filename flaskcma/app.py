from flask import Flask
from flaskcma.setup import setup
import os


app = Flask(__name__)

app.config.from_object("flaskcma.default_settings")

conf_envvar = "FLASKCMA_SETTINGS"
if conf_envvar in os.environ:
    app.config.from_envvar("FLASKCMA_SETTINGS")


# Import all the documents so that they will be registered
from flaskcma.content.views import mod
app.register_module(mod)

from flaskcma.stories.views import mod
app.register_module(mod)

setup(app)

if  __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001)

