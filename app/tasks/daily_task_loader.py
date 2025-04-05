
from celery import Celery
from app.models import TaskManager, TaskLogger, db
from datetime import datetime

celery = Celery(__name__, broker='redis://localhost:6379/0')

@celery.task
def load_daily_tasks():
    active_tasks = TaskManager.query.filter_by(status=True).all()
    for task in active_tasks:
        existing_log = TaskLogger.query.filter_by(task_manager_id=task.id, log_date=datetime.utcnow().date()).first()
        if not existing_log:
            task_log = TaskLogger(task_manager_id=task.id, log_date=datetime.utcnow().date())
            db.session.add(task_log)
    db.session.commit()
