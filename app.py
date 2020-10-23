"""Sphinx Flask Environment
"""
from model import app
from dotenv import load_dotenv

if __name__ == '__main__':
    app.run(port=os.getenv('PORT'), debug=bool(os.getenv('DEBUG')))
