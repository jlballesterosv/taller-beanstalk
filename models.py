from marshmallow import  Schema, fields
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime, timedelta
from uuid import uuid4
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Model():
  id = Column(Integer, primary_key=True)
  createdAt = Column(DateTime)
  updatedAt = Column(DateTime)

  def __init__(self):
    self.createdAt = datetime.now()
    self.updatedAt = datetime.now()

class Email(Model, Base):
  __tablename__ = 'blacklistEmails'

  ip = Column(String)
  email = Column(String)
  blocked_reason = Column(String)
  app_uuid = Column(String)
  

  def __init__(self, ip, email,app_uuid,blocked_reason=''):
    Model.__init__(self)
    self.ip = ip
    self.email = email
    self.app_uuid = app_uuid
    self.blocked_reason = blocked_reason 

    
class EmailSchema(Schema):
  ip = fields.String()
  email = fields.Str()
  blocked_reason= fields.Str()
  app_uuid = fields.Str()
  createdAt = fields.DateTime()
  

