from flask_script import Manager
from flask_script.commands import Server

from app import create_app

manager = Manager(create_app)
manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()