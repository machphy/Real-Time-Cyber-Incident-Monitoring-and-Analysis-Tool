from flask import Flask
from api.incidents.views import incidents_blueprint
from api.ml.views import ml_blueprint
from utils.database import initialize_db

app = Flask(__name__)

app.config.from_object('config.config.Config')

initialize_db(app)

app.register_blueprint(incidents_blueprint, url_prefix='/api/incidents')
app.register_blueprint(ml_blueprint, url_prefix='/api/ml')

if __name__ == '__main__':
    app.run(debug=True)
