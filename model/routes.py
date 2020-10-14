from model import app
from model import baseline


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/predict/<int:state>')
def predict(state):
    preds = baseline.forward(state)
    return f'{preds}'
