from model import app
from model import baseline


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/predict/<int:state>')
def predict(state):
    preds = baseline.forward(state)
    return f'{preds}'


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
