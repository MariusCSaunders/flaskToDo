from application import db
from application.models import Tasks

db.create_all()

first_task = Tasks(description="Frist task, make a task")

second_task = Tasks(description="Second Task, complete a task", completed=True)

third_task = Tasks(description="Third Task, update a task")

db.session.add(first_task)
db.session.add(second_task)
db.session.add(third_task)
db.session.commit()


