from views import db
from models import Task
from datetime import date

# Create the database and tables
db.create_all()

# Insert data
db.session.add(Task('Finish this tutorial', date(2015, 03, 06), 10, 1))
db.session.add(Task('Finish this course', date(2015, 04, 06), 10, 1))

# Commit the changes
db.session.commit()

