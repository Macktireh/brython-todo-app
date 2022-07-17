import uuid
from browser import window, document, html


tasks = [
    {
        'id': str(uuid.uuid4()).replace('-', '')[:16],
        'name': 'Faire les courses',
        'completed': True,
    },
    {
        'id': str(uuid.uuid4()).replace('-', '')[:16],
        'name': 'Faire le ménage',
        'completed': False,
    },
    {
        'id': str(uuid.uuid4()).replace('-', '')[:16],
        'name': 'Faire la cuisine',
        'completed': False,
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
        )
        
        img_delete = html.IMG(
            src="./assets/del.svg",
            id=f"{task.get('id')}"
        ).bind('click', handelDelete)
        
        task_element = html.DIV(
            checkbox + span + img_delete,
            id=f"task-{task.get('id')}",
            Class='task'
        )
        listContainer <= task_element

def handleAdd(e):
    if input.value != '':
        new_task = {
            'id': str(uuid.uuid4()).replace('-', '')[:16],
            'name': input.value,
            'completed': False,
        }
        tasks.append(new_task)
        showTasks([new_task])
        input.value = ''
        h3.text = f"Tâche à faire : {count_tasks_not_completed()}"

def handleCompleted(e):
    for task in tasks:
        if task.get('id') == e.target.id:
            task['completed'] = e.target.checked
    h3.text = f"Tâche à faire : {count_tasks_not_completed()}"

def handelDelete(e):
    if window.confirm("Vous voulez supprimer !"):
        global tasks
        tasks = list(filter(lambda task: task.get('id') != e.target.id, tasks))
        document[f'task-{e.target.id}'].remove()
        h3.text = f"Tâche à faire : {count_tasks_not_completed()}"


root = document['root']

h1 = html.H1("Python dans le navigateur")
h3 = html.H3(f"Tâche à faire : {count_tasks_not_completed()}")
root <= h1 + h3

input = html.INPUT(type='text', placeholder="Entrer une tache", id='input')
btn = html.BUTTON('Ajouter').bind("click", handleAdd)

formContainer = html.DIV(Class="formContainer")
formContainer <= input + btn
root <= formContainer

listContainer = html.DIV(Class="listContainer")

showTasks(tasks)

root <= listContainer