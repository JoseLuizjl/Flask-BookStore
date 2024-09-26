from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://joseluiz:senha976@localhost:3306/banco_dados")
conn = engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()