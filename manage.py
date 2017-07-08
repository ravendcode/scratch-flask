from flask_script import Manager

from app import app
from commands import fake, translate

manager = Manager(app)

manager.add_command('fake:tags', fake.TagsFakeCommand())
manager.add_command('trans', translate.TranslateCommand())

if __name__ == "__main__":
    manager.run()
