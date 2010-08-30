import settings
from os import path
import site

site.addsitedir(path.join(path.dirname(__file__), "../"))
from flaskcma.app import app
app.config.from_object(settings)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)
