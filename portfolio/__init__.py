import os

from flask import Flask
from flask_mail import Mail


mail = Mail()


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=***REMOVED***,
        DATABASE=os.path.join(app.instance_path, 'portfolio.sqlite'),
    )

    app.config['MAIL_SERVER'] = 'mail.privateemail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'michael@michaelkistler.net'
    app.config['MAIL_PASSWORD'] = ***REMOVED***
    mail.init_app(app)

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import contact
    app.register_blueprint(contact.bp)
    app.add_url_rule('/', endpoint='index')

    return app
