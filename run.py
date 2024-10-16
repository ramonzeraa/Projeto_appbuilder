from app import app, db, appbuilder
import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA


logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

from app import views



app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":
    app.run(debug=True)
