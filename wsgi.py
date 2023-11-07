from gunicorn.app.base import Application
from main import app  # Import your Flask app from main.py (or the appropriate file)

class FlaskApp(Application):
    def init(self, parser, opts, args):
        pass

    def load(self):
        return app

if __name__ == "__main__":
    FlaskApp().run()
