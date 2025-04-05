#database queries for task related jobs like get all , get by id , create task



from app.models import TaskManager, db

class TaskRepository:
    @staticmethod
    def get_all_tasks():
        return TaskManager.query.all()

    @staticmethod
    def get_task_by_id(task_id):
        return TaskManager.query.get_or_404(task_id)

    @staticmethod
    def create_task(data):
        task = TaskManager(**data)
        db.session.add(task)
        db.session.commit()
        return task
