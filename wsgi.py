from app import app
import os

host = os.environ.get("FLASK_HOST")
port = os.environ.get("FLASK_PORT")

if __name__ == '__main__':
    app.run(host=host, port=port, debug=False)
