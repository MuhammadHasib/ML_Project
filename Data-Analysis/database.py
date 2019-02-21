from os import path

from sqlalchemy import (create_engine, Column, String, Integer, Boolean, Table, ForeignKey)

from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

database_filename = 'twitter.sqlite3'

directory  = path.abspath(path.dirname(__file__))
databse_filepath = path.join(directory, database_filename)

engine_url = 'sqlite:///{}'.format(database_filepath)

engine = create_engine(engine_url)

#out databse class objects are going to inherit from 
# this class
Base = declarative_base(bind=engine)

# Create a configuration "Session" class
Session = sessionmaker(bind=engine, autoflush=False)

# Create a session
session = Session()

hashtag_tweet = Table('hashtag_tweet', Base.metadata, 
	Column('hashtag_id', Integer, ForeignKey('hashtags.id'), nullable=False), 
	Column('tweet_id', Integer, ForeignKey('tweet.id'),nullable=False))

class Tweet(Base):
	__tablename__ = 'tweets'
	id = Column(Integer, primary_key=True)
	tid = Column(String(100), nullable=False)
	tweet = Column(String(300),nullable=False)
	user_id = Column(Integer, ForeignKey('users.id'), nullable=Flase)
	coordinates = Column(String(50), nullable=True)
	user = relationship('User', backref='tweets')
	created_at = Column(string(100), nullable=False)
	favorite_count = Column(Integer)
	in_reply_to_screen_name = Column(String)
	in_reply_to_status_id = Column(Integer)
	in_reply_to_user_id = Column(Integer)
	lang = Column(string)
	quoted_status_id = Column(Integer)
	retweed_count = Column(Integer)
	source = Column(String)
	is_retweet = Column(String)
	hashtags = relationship('Hashtag', secondary='hashtag_tweet',back_populates='tweets')
