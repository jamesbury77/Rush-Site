from app import app, db
from app.models import User

users = User.query.all()

for u in users:
    print(u.username)