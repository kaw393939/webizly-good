from os import getenv
import datetime
from application.bp.authentication.forms import LoginForm
from config import Config

def utility_text_processors():
    message = "hello world"
    form = LoginForm()

    def deployment_environment():
        return Config.DEPLOYMENT

    def current_year():
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        return year

    def format_price(amount, currency="$"):
        return f"{currency}{amount:.2f}"

    return dict(
        form=form,
        mymessage=message,
        deployment_environment=deployment_environment(),
        year=current_year(),
        format_price=format_price
    )