# run.py

# em Migration
# antes de: flask db init
# use este comando: export (set para windows) FLASK_APP=run.py
# https://programmerah.com/flash-cli-encountered-a-keyerror-migrate-how-to-solve-37846/

import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()