from sqlalchemy import create_engine

#SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://jlapazac:Jose++301090@192.168.18.4:3306/cocinamama'
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://admin:sKleHy5wYcG1SlakiFWp@db:3306/cocinamama'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

conn = engine.connect()