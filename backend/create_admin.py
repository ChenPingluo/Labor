from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()

with app.app_context():
    if User.query.filter_by(username='admin').first():
        print("User 'admin' already exists.")
    else:
        user = User(username='admin', role='admin')
        user.set_password('admin')
        db.session.add(user)
        db.session.commit()
        print("User 'admin' created with password 'admin'.")
