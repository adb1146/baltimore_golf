import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

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

class TeeTime(Base):
    __tablename__ = 'tee_times'
    
    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)
    tee_time = Column(DateTime, nullable=False)
    available = Column(Boolean, default=True)
    booked_by = Column(String)
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

def generate_tee_times(course_name, date):
    """Generate tee times for a specific course and date"""
    session = Session()
    try:
        # Delete existing tee times for this course and date
        start_of_day = datetime.combine(date, datetime.min.time())
        end_of_day = datetime.combine(date, datetime.max.time())
        session.query(TeeTime).filter(
            TeeTime.course_name == course_name,
            TeeTime.tee_time.between(start_of_day, end_of_day)
        ).delete()
        
        # Generate new tee times from 7 AM to 5 PM with 10-minute intervals
        current_time = datetime.combine(date, datetime.min.time().replace(hour=7))
        end_time = datetime.combine(date, datetime.min.time().replace(hour=17))
        
        while current_time <= end_time:
            tee_time = TeeTime(
                course_name=course_name,
                tee_time=current_time,
                available=True
            )
            session.add(tee_time)
            current_time += timedelta(minutes=10)
        
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False
    finally:
        session.close()

def get_available_tee_times(course_name, date):
    """Get available tee times for a specific course and date"""
    session = Session()
    try:
        start_of_day = datetime.combine(date, datetime.min.time())
        end_of_day = datetime.combine(date, datetime.max.time())
        tee_times = session.query(TeeTime).filter(
            TeeTime.course_name == course_name,
            TeeTime.tee_time.between(start_of_day, end_of_day)
        ).order_by(TeeTime.tee_time).all()
        return tee_times
    finally:
        session.close()

def book_tee_time(tee_time_id, user_name):
    """Book a tee time for a user"""
    session = Session()
    try:
        tee_time = session.query(TeeTime).get(tee_time_id)
        if tee_time and tee_time.available:
            tee_time.available = False
            tee_time.booked_by = user_name
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        return False
    finally:
        session.close()
