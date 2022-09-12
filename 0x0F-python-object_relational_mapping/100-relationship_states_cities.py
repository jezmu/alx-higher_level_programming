#!/usr/bin/python3
"""
creates state "California" with city attribute "San Francisco"
"""

from sys import argv
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from sqlalchemy import create_engine


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, db),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_s = State(name="California")
    new_c = City(name="San Francisco")
    new_s.cities.append(new_c)

    session.add(new_s)
    session.add(new_c)

    session.commit()
    session.close()
