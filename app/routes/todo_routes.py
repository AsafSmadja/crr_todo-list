from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.models import Todo

bp = Blueprint('todo', __name__)

@bp.route('/')
def index():
    todos = Todo.query.filter_by(deleted=False).all()
    completed_tasks = Todo.query.filter_by(completed=True, deleted=False).count()
    in_progress_tasks = Todo.query.filter_by(started=True, completed=False, deleted=False).count()
    not_started_tasks = Todo.query.filter_by(started=False, completed=False, deleted=False).count()
    deleted_tasks = Todo.query.filter_by(deleted=True).count()

    return render_template('index.html', todos=todos, completed_tasks=completed_tasks,
                           in_progress_tasks=in_progress_tasks, not_started_tasks=not_started_tasks,
                           deleted_tasks=deleted_tasks)



@bp.route('/add', methods=['POST'])
def add():
    task_content = request.form.get('todo')
    if task_content:
        new_task = Todo(task=task_content)
        db.session.add(new_task)
        db.session.commit()
        flash('New task added!', 'success')
    return redirect(url_for('todo.index'))

@bp.route('/complete/<int:todo_id>')
def complete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('todo.index'))

@bp.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.deleted = True
    db.session.commit()
    return redirect(url_for('todo.index'))

@bp.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if request.method == 'POST':
        todo.task = request.form['content']
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('edit.html', todo=todo)

@bp.route('/start/<int:todo_id>')
def start_task(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if not todo.started:
        todo.started = True
        db.session.commit()
        flash('Task started!', 'info')
    return redirect(url_for('todo.index'))
