from flask import Flask
from db import db
from routes import routes
import config

app = Flask(__name__)

# Config
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

# Initialize DB
db.init_app(app)

# Register routes
app.register_blueprint(routes)

# Create tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Task Manager API Running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
