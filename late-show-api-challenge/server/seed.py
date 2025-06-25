from models import db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from app import create_app

app = create_app()

with app.app_context():
    print("🌱 Seeding data...")

    # Drop and create all tables
    db.drop_all()
    db.create_all()

    # Users
    u1 = User(username="admin")
    u1.set_password("password")

    # Guests
    g1 = Guest(name="Zendaya", occupation="Actress")
    g2 = Guest(name="Elon Musk", occupation="Entrepreneur")

    # Episodes
    e1 = Episode(date="2025-06-01", number=101)
    e2 = Episode(date="2025-06-02", number=102)

    # Appearances
    a1 = Appearance(rating=5, guest=g1, episode=e1)
    a2 = Appearance(rating=4, guest=g2, episode=e2)

    db.session.add_all([u1, g1, g2, e1, e2, a1, a2])
    db.session.commit()
    print("✅ Done seeding!")
