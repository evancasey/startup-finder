from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy import (Column,
                        Integer,
                        String,
                        Boolean,
                        DateTime,
                        MetaData,
                        )

# set up our local DB to store the tweets
db = create_engine('sqlite:///companies.db')
Base = declarative_base(bind=db)
Session = scoped_session(sessionmaker(db))
db.echo = False

class CrunchBase(Base):
  
  __tablename__ = 'crunchbase'

  id = Column(String, primary_key=True)
  name = Column(String)
  homepage_url = Column(String)
  description = Column(String)
  founded_on = Column(String)
  websites = Column(String)
  total_funding = Column(Integer)
  categories = Column(String)
  logo_path = Column(String)
  founders = Column(String)
  headquarters = Column(String)  
  news = Column(String)

class Github(Base):

  __tablename__ = 'github'

  id = Column(String, primary_key=True)
  organization = Column(String)
  repos = Column(String)

# create our db
Base.metadata.create_all(db)
