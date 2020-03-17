import hashlib
import json
import os.path
import textwrap
from datetime import datetime


class Task():
    """
    Stores information about a Task and provides utility methods for
    serialization, deserialization and console output formatting.
    """
    def __init__(self, name, deadline, description, task_hash=None):
        self.name = name
        self.deadline = deadline
        self.description = description

        # Hash is generated using task's content, current timestamp is added
        # to avoid duplicated hashes in case of creating identical tasks
        if task_hash is None:
            content_hash = hashlib.md5((
                name +
                str(deadline) +
                str(description) +
                str(datetime.now().timestamp())
                ).encode())
            self.hash = content_hash.hexdigest()
        else:
            self.hash = task_hash

    @property
    def formatted_string(self):
        """
        Returns task content as string, formatted for display in console
        """
        formatted_task = '-' * 80 + "\n{:20} | {:19} | {:32}\n".format(
            self.name,
            str(self.deadline) if self.deadline else "",
            self.hash
        )
        if self.description:
            wrapped_desc = textwrap.wrap(self.description, 80)
            formatted_task += '\n'
            for line in wrapped_desc:
                formatted_task += line + '\n'
        return formatted_task

    @classmethod
    def as_dict(cls, task):
        # Custom method used because of datetime to string cast
        return {
            'hash': task.hash,
            'name': task.name,
            'deadline': str(task.deadline),
            'description': task.description}

    @classmethod
    def from_dict(cls, task_dict):
        if task_dict['deadline'] == 'None':
            deadline = None
        else:
            deadline = datetime.fromisoformat(task_dict['deadline'])
        return cls(
            task_dict['name'],
            deadline, task_dict['description'],
            task_dict['hash'])


class TaskManager():
    """
    Provides methods to create/update/delete/list tasks.
    Also handles task storage in external file.
    """
    def __init__(self):
        if os.path.exists('task_storage.json'):
            with open('task_storage.json', 'r') as f:
                tasks = json.load(f)
                self.tasks = [Task.from_dict(task) for task in tasks]
        else:
            self.tasks = []

    def __del__(self):
        if self.tasks:
            self.save_tasks()
        else:
            try:
                os.remove('task_storage.json')
            except OSError:
                pass

    def add_task(self, name, deadline, description):
        """ Creates new task and adds it to self.tasks list."""
        self.tasks.append(Task(name, deadline, description))

    def update_task(self, task_hash, name, deadline, description):
        """
        Updates task from self.tasks based on passed hash value.
        If parameter's value is None, corresponding field is left unchanged.
        """
        task = self.get_task(task_hash)
        if task:
            if name:
                task.name = name
            if deadline:
                task.deadline = deadline
            if description:
                task.description = description

    def delete_task(self, task_hash):
        """ Deletes task from self.tasks based on passed hash value."""
        task = self.get_task(task_hash)
        if task:
            self.tasks.remove(task)

    def list_tasks(self, mode):
        """
        Prints tasks to the console.
        If mode == 'all' prints all of the tasks.
        If mode == 'today' prints tasks with current day as deadline.
        """
        if len(self.tasks) == 0:
            print('No tasks currently.')
            return

        if mode == "all":
            for task in self.tasks:
                print(task.formatted_string)
            print('-' * 80)
        elif mode == "today":
            today = datetime.today().date()
            todays_tasks = list(filter(
                lambda t: t.deadline and t.deadline.date() == today,
                self.tasks))
            if todays_tasks:
                for task in todays_tasks:
                    print(task.formatted_string)
                print('-' * 80)
            else:
                print('No tasks for today.')

    def get_task(self, task_hash):
        """ Returns task with given hash."""
        for task in self.tasks:
            if task_hash == task.hash:
                return task
        print('Task with given hash not found.')
        return None

    def save_tasks(self):
        with open('task_storage.json', 'w') as f:
                json.dump(self.tasks, f, default=Task.as_dict)
