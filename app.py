import sqlite3
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DB_PATH = 'metro.db'

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'todo',
                priority TEXT DEFAULT 'medium',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    with get_db() as conn:
        tasks = conn.execute('SELECT * FROM tasks ORDER BY created_at DESC').fetchall()
        return jsonify([dict(t) for t in tasks])

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    with get_db() as conn:
        cursor = conn.execute(
            'INSERT INTO tasks (title, description, priority, status) VALUES (?, ?, ?, ?)',
            (data['title'], data.get('description', ''), data.get('priority', 'medium'), data.get('status', 'todo'))
        )
        conn.commit()
        return jsonify({'id': cursor.lastrowid}), 201

@app.route('/api/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    with get_db() as conn:
        conn.execute(
            'UPDATE tasks SET title = ?, description = ?, status = ?, priority = ? WHERE id = ?',
            (data['title'], data['description'], data['status'], data['priority'], id)
        )
        conn.commit()
        return jsonify({'status': 'updated'})

@app.route('/api/tasks/<int:id>/status', methods=['PATCH'])
def update_status(id):
    data = request.json
    with get_db() as conn:
        conn.execute('UPDATE tasks SET status = ? WHERE id = ?', (data['status'], id))
        conn.commit()
        return jsonify({'status': 'moved'})

@app.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    with get_db() as conn:
        conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
        conn.commit()
        return jsonify({'status': 'deleted'})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
