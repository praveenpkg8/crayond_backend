from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from models import database
manager = Manager(app)
migrate = Migrate(app, database)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

