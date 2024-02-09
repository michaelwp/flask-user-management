from app import app
import api.apis_users as user
import api.apis_authentication as auth
import api.apis_home as home
import api.apis_error_handler as err_handler
from werkzeug.exceptions import HTTPException
from middleware.middleware_authentication import Token_authentication


@app.errorhandler(HTTPException)
def err_handle_exception(e):
    return err_handler.handle_exception(e)


@app.errorhandler(404)
def err_page_not_found(e):
    return err_handler.page_not_found(e)


@app.route("/", methods=["GET"])
@Token_authentication()
def Api_home():
    return home.Home()


@app.route("/login", methods=["POST"])
def User_login():
    return auth.Login()


@app.route("/users", methods=["GET"])
@Token_authentication()
def User_view():
    return user.View()


@app.route("/users/register", methods=["POST"])
def User_register():
    return user.Register()


@app.route("/users/update", methods=["PUT"])
@Token_authentication()
def User_update():
    return user.Update()
