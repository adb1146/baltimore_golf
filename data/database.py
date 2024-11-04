import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Create database engine
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
engine = create_engine(DATABASE_URL)

# Create declarative base
Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    comment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(engine)

# Create session factory
Session = sessionmaker(bind=engine)

def add_review(course_name, user_name, rating, comment):
    session = Session()
    try:
        review = Review(
            course_name=course_name,
            user_name=user_name,
            rating=rating,
            comment=comment
        )
        session.add(review)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False
    finally:
        session.close()

def get_course_reviews(course_name):
    session = Session()
    try:
        reviews = session.query(Review).filter(Review.course_name == course_name).all()
        return reviews
    finally:
        session.close()

def get_course_average_rating(course_name):
    session = Session()
    try:
        reviews = session.query(Review).filter(Review.course_name == course_name).all()
        if not reviews:
            return None
        return sum(review.rating for review in reviews) / len(reviews)
    finally:
        session.close()
