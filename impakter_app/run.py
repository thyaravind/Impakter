import os
from app import create_app, db
from app.models import User, Role

from flask_migrate import Migrate


get_config_mode = 'development'

app = create_app(get_config_mode.capitalize())
migrate = Migrate(app,db)
