#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
"""

from relationship_state import Base, State
from relationship_city import City
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
    add_state = State(name="California")
    session.add(add_state)
    session.commit()
    add_city = City(name="San Francisco", state_id=add_state.id)
    session.add(add_city)
    session.commit()
    session.close()
