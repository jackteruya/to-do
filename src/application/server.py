from flask import Blueprint, Flask
from flask_restx import Api

from src.application.rest.health_check import health
from src.application.rest.todo import todo_api

from src.commons.config import settings


class ServeApplication:

    def __init__(self):
        self.app = Flask(__name__)
        self._blueprint = Blueprint("api", __name__, url_prefix=f"{settings.url_prefix}")

    def _init_blueprints(self, app):
        api = Api(
            self._blueprint,
            title="To-Do",
            version="0.0.1",
            doc="/docs",
        )

        api.add_namespace(health)
        api.add_namespace(todo_api)
        app.register_blueprint(self._blueprint)

    def create_app(self):
        # self.app.wsgi_app = ProxyFix(self.app.wsgi_app)

        self._init_blueprints(self.app)

        return self.app


app = ServeApplication().create_app()
