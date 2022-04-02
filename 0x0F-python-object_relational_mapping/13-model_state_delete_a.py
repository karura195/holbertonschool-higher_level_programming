#!/usr/bin/python3
""" Deletes all State objects with a name containing the letter a """
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    sql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql.format(argv[1],
                                      argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    session.query(State).filter(
        State.name.like("%a%")).delete(synchronize_session=False)
    session.commit()
    session.close()
