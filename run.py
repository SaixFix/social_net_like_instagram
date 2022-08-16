from flask import Flask
from app.main.views import main_blueprint
from app.error.views import error_blueprint
from app.api_endpoint.views import endpoint_blueprint

app = Flask(__name__)
#регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(error_blueprint)
app.register_blueprint(endpoint_blueprint)


if __name__ == "__main__":
    app.run()


