from flask_script import Command, Option
from faker import Faker

from app import db
from app.tags.models import Tag

fake = Faker()

class TagsFakeCommand(Command):
    "Populate tag table"

    def __init__(self, count=10):
        self.count = count

    def get_options(self):
        return [
            Option('-c', '--count', dest='count', default=self.count),
        ]

    def run(self, count):
        int_count = count if type(count) == int else int(count)
        for _ in range(int_count):
            tag = Tag(fake.sentence())
            db.session.add(tag)
            db.session.commit()
        print('done')
