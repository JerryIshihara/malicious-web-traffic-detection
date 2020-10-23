from flask import Flask
from flask_cors import CORS
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://77efe2bf05f142aaa7383d2764717b05@o465899.ingest.sentry.io/5479436",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

app = Flask(__name__)
CORS(app)

from model import routes
