# tests/test_task_routes.py
import pytest
from app import create_app
from app.extensions import db
from app.models import TaskManager
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:Twinkle2911@localhost/test_db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_task(client):
    data = {
        "task_name": "Test Task",
        "description": "Test Task Description",
        "status": True,
        "priority": "MEDIUM",
        "assigned_user": "test_user"
    }
    response = client.post('/api/tasks', json=data)
    assert response.status_code == 201
    assert response.json['task_id'] is not None
