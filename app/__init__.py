"""
Bean Counter - Track Your Coffee!
Copyright (C) 2014  BouncyNudibranch (bouncynudibranch@gmail.com)

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import markdown
import bleach
from app.util import seconds_to_timestring

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

bleach.ALLOWED_TAGS.append('p')  # Allow markdown to use paragraphs

app.jinja_env.filters['sec_to_time'] = seconds_to_timestring
app.jinja_env.filters['markdown'] = markdown.markdown
app.jinja_env.filters['bleach_clean'] = bleach.clean

from app import models, views