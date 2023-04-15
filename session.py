from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

class SessionConfig():
  def __init__(self):
    print('')

  def url(self):
    return 'sqlite:///blacklist.db'

session_config = SessionConfig()
engine = create_engine('sqlite:///blacklist.db')
Session = sessionmaker(bind=engine)