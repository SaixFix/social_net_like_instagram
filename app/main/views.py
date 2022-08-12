from flask import Blueprint, request, render_template
import logging

#создаем блюпринт
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    """
    Главная страница
    """
    return render_template('index.html')