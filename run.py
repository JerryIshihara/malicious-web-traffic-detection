"""Sphinx Flask Environment
"""
from model import app

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
