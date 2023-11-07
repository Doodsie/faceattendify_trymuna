from app import app  # Import your Flask app from app.py
from gunicorn.app.base import Application

class FlaskApp(Application):
    def init(self, parser, opts, args):
        pass

    def load(self):
        return app

if __name__ == "__main__":
    FlaskApp().run()
