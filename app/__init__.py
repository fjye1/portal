from flask import Flask
from .extensions import db, login_manager
from app.utils.gravatar import gravatar_url
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from app.context_injectors import inject_urls
# 1. Instantiate extensions outside the factory
csrf = CSRFProtect()
migrate = Migrate()

def create_app():
    # 2. Define the app instance FIRST
    app = Flask(
        __name__,
        static_folder='../static',
        template_folder='../templates'
    )
    app.config.from_object("config.Config")



    # 3. Import models so SQLAlchemy/Alembic knows they exist
    from . import models

    # 4. Initialize extensions with the app
    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)  # Connects Migrate to App and DB
    login_manager.init_app(app)
    
    # 5. Setup Jinja and Login Manager settings
    app.jinja_env.filters['gravatar'] = gravatar_url
    login_manager.login_view = "auth.login" # type: ignore
    login_manager.login_message_category = "info"

    # 6. Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.proxy import proxy_bp
    from app.routes.home import home_bp
    from app.routes.admin import admin_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(proxy_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(admin_bp)

    app.context_processor(inject_urls)

    return app