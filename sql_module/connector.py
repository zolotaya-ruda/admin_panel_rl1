import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

engine = create_engine('mysql+pymysql://root:83Linedip@localhost/rl')
engine.connect()

base = declarative_base()
session = Session(bind=engine)