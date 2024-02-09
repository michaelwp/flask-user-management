from app import app, db
import model.models_users

with app.app_context():
    db.create_all()
