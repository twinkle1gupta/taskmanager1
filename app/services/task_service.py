#create task , uopdate task , delete task , show all tasks

from app.models import TaskManager, db
from app.repositories.task_repo import TaskRepository

class TaskService:
    @staticmethod
    def create_task(data):
        task_data = {
            "task_name": data['task_name'],
            "description": data['description'],
            "status": data['status'],
            "priority": data['priority'],
            "assigned_user": data['assigned_user']
        }
        task = TaskRepository.create_task(task_data)
        return task

    @staticmethod
    def update_task(task_id, data):
        task = TaskRepository.get_task_by_id(task_id)
        task.task_name = data.get('task_name', task.task_name)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        task.priority = data.get('priority', task.priority)
        db.session.commit()
        return task

    @staticmethod
    def delete_task(task_id):
        task = TaskRepository.get_task_by_id(task_id)
        task.status = False  # Soft delete by marking as inactive
        db.session.commit()

    @staticmethod
    def get_all_tasks():
        return TaskRepository.get_all_tasks()
