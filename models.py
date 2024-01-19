from app import app, db
import models_users

with app.app_context():
    db.create_all()
