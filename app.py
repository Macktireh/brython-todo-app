import uuid
from browser import window, document, html


tasks = [
    {
        'id': str(uuid.uuid4()).replace('-', '')[:16],
        'name': 'Faire les courses',
        'completed': True,
        'isUpdateing': False,
    },
    {
        'id': str(uuid.uuid4()).replace('-', '')[:16],
        'name': 'Faire le ménage',
        'completed': False,
        'isUpdateing': False,
    },
    {
        'id': str(uuid.uuid4()).replace('-', '')[:16],
        'name': 'Faire la cuisine',
        'completed': False,
        'isUpdateing': False,
    }
]

def count_tasks_not_completed():
    return len([task for task in tasks if not task.get('completed')])

def showTasks(tasks):
    for task in tasks:
        checkbox = html.INPUT(
            type="checkbox", 
            checked=task.get('completed'), 
            id=f"{task.get('id')}"
        ).bind('change', handleCompleted)
        
        span = html.SPAN(
            task.get('name'), 
            id=f"span-{task.get('id')}"
        ) if not task.get('isUpdateing') else editing(task)
        
        img_edit = html.IMG(
            src="./assets/edit.svg",
            id=f"{task.get('id')}"
        ).bind('click', handleIsEditing)
        
        img_delete = html.IMG(
            src="./assets/del.svg",
            id=f"{task.get('id')}"
        ).bind('click', handleDelete)
        
        task_element = html.DIV(
            checkbox + span + img_edit + img_delete,
            id=f"task-{task.get('id')}",
            Class=f"task task-{task.get('id')}"
        )
        listContainer <= task_element

def handleAdd(e):
    def add():
        if input.value != '':
            new_task = {
                'id': str(uuid.uuid4()).replace('-', '')[:16],
                'name': input.value,
                'completed': False,
                'isUpdateing': False,
            }
            tasks.append(new_task)
            showTasks([new_task])
            input.value = ''
            h3.text = f"Tâche à faire : {count_tasks_not_completed()}"
    if e.type == 'keydown' and e.key == 'Enter':
        add()
    if e.type == 'click':
        add()

def handleCompleted(e):
    for task in tasks:
        if task.get('id') == e.target.id:
            task['completed'] = e.target.checked
    h3.text = f"Tâche à faire : {count_tasks_not_completed()}"

def editing(task):
    input_edit = html.INPUT(
        type='text',
        value=task.get('name'), 
        id=f"input_edit-{task.get('id')}",
        autofocus=True
    ).bind('keydown', handleUpdate)
    btn_edit = html.BUTTON('Valider', id=f"{task.get('id')}").bind('click', handleUpdate)
    div_edit = html.DIV(Class="editing")
    div_edit <= input_edit + btn_edit
    
    return div_edit

def handleIsEditing(e):
    for task in tasks:
        if task.get('id') == e.target.id:
            if task['isUpdateing']:
                task['isUpdateing'] = False
            else:
                task['isUpdateing'] = True
            listContainer.html = ""
            showTasks(tasks)

def handleUpdate(e):
    def update():
        id = e.target.id.split('-')[-1]
        value = document[f"input_edit-{id}"].value
        for task in tasks:
            if task.get('id') == id:
                task['name'] = value
                task['isUpdateing'] = False
                listContainer.html = ""
                showTasks(tasks)
    if e.type == 'keydown' and e.key == 'Enter':
        update()
    if e.type == 'click':
        update()

def handleDelete(e):
#     if window.confirm("Vous voulez supprimer !"):
    global tasks
    tasks = list(filter(lambda task: task.get('id') != e.target.id, tasks))
    document[f'task-{e.target.id}'].remove()
    h3.text = f"Tâche à faire : {count_tasks_not_completed()}"


root = document['root']

h1 = html.H1("Python dans le navigateur")
h3 = html.H3(f"Tâche à faire : {count_tasks_not_completed()}")
root <= h1 + h3

input = html.INPUT(type='text', placeholder="Entrer une tache", id='input').bind('keydown', handleAdd)
btn = html.BUTTON('Ajouter').bind('click', handleAdd)

formContainer = html.DIV(Class="formContainer")
formContainer <= input + btn
root <= formContainer

listContainer = html.DIV(Class="listContainer", id="listContainer")

showTasks(tasks)

root <= listContainer
