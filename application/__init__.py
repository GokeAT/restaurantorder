from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@10.77.80.7/flask_db"

db = SQLAlchemy(app)

from application import routes