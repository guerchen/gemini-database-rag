import os

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)

def import_data():
    with SessionLocal() as session:
        drop_old_query = "DROP TABLE users"
        session.execute(drop_old_query)
        create_table_query = """CREATE TABLE users (
                                id SERIAL,
                                firstname VARCHAR(50),
                                lastname VARCHAR(50),
                                gender VARCHAR(50),
                                email VARCHAR(255),
                                ip_address VARCHAR(50),
                                PRIMARY KEY (id)
                                );
                                """
        session.execute(create_table_query)
        import_query = """COPY users(id, firstname, lastname, gender, email, ip_address)
                          FROM '/shared_data/example.csv'
                          DELIMITER ','
                          CSV HEADER;
                        """
        session.execute(import_query)
        session.commit()


def query_db(sql_query):
    with SessionLocal() as session:
        cursor = session.execute(sql_query)
        results = cursor.fetchall()
        return str(results)