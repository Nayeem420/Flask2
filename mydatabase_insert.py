from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mydatabase import USER, Base, SESSIONS

engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine



DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
# Insert a Person in the person table
new_name = USER(name='new name')
new_email = USER(email='new email')
new_password = USER(password='new password')
session.add(new_name)
session.add(new_email)
session.add(new_password)
session.commit()

# Insert an Address in the address table
new_login = SESSIONS(logintime='logintime', user=new_email)
new_logout = SESSIONS(logouttime='logouttime', user=new_email)
session.add(new_login)
session.add(new_logout)
session.commit()
