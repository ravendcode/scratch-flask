from flask_script import Command

from app import db
import app.auth.models
import app.posts.models
import app.tags.models


class CreateDb(Command):
    "Create database"

    def run(self):
        db.create_all()
        print('done')
