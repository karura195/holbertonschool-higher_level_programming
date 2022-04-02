#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects
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
    list = session.query(State).join(City).order_by(State.id, City.id).\
        filter(City.state_id == State.id).all()
    for st in list:
        print("{}: {}".format(st.id, st.name))
        for ct in st.cities:
            print("    {}: {}".format(ct.id, ct.name))
    session.close()
