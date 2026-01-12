from flask import Flask
from .ext import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Import and register blueprints
    from .routes.auth import auth_bp
    from .routes.dashboard import dashboard_bp
    from .routes.events import events_bp
    from .routes.resources import resources_bp
    from .routes.allocations import allocations_bp
    from .routes.reports import reports_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(resources_bp)
    app.register_blueprint(allocations_bp)
    app.register_blueprint(reports_bp)

    # Create DB tables
    with app.app_context():
        db.create_all()

    return app
