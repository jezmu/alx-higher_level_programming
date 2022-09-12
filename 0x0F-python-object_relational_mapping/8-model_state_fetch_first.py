#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

    first_obj = session.query(State).order_by(State.id).first()
    if first_obj:
        print("{:d}: {:s}".format(first_obj.id, first_obj.name))
    else:
        print("Nothing")
    session.close()
