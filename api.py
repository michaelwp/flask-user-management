from app import app
from api_users import View, Register, Update
from api_authoriztion import Login


@app.route("/", methods=["GET"])
def Home():
    return "welcome home", 200


@app.route("/login", methods=["POST"])
def User_login():
    return Login()


@app.route("/users", methods=["GET"])
def User_view():
    return View()


@app.route("/users/register", methods=["POST"])
def User_register():
    return Register()


@app.route("/users/update", methods=["PUT"])
def User_update():
    return Update()
