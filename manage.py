from flask_script import Manager

from app import app
from commands import fake

manager = Manager(app)

manager.add_command('fake:tags', fake.TagsFakeCommand())

if __name__ == "__main__":
    manager.run()
