import os

DATABASE_URI = os.getenv("DATABASE_URI", "postgresql://postgres:johnhoward@localhost:5432/late_show_db")


class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret")