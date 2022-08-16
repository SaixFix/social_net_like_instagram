from flask import Blueprint


error_blueprint = Blueprint('error_blueprint', __name__)


@error_blueprint.app_errorhandler(404)
def not_found_error(error):
    """
    вьюшка возвращает текст при ошибке 404
    """
    return "404 ОМГ! Страница не найдена! Вызывайте ищеек!"


@error_blueprint.app_errorhandler(500)
def not_found_error(error):
    """
    вьюшка возвращает текст при ошибке 500
    """
    return "500 Что тут происходит?! Требуется экзорцист! (.)(.) - это просто глаза смотрят вниз от стыда!"

