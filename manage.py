from flask_script import Manager

from flask_migrate import Migrate,MigrateCommand
from api.Data.models import db
from api import create_app

app=create_app()
migrate = Migrate(app, db)
manager = Manager(app)

# migrations#
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()

@manager.command
def list_routes():
    import urllib

    output = []


    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == '__main__':
    manager.run()

