"""
    CLI for TaskManager class
"""
import argparse
from datetime import datetime

from taskmanager import TaskManager


def valid_date(date):
    """ Checks if passed value is valid date in isoformat. """
    try:
        return datetime.fromisoformat(date)
    except ValueError:
        msg = f'Not a valid date: "{date}".'
        raise argparse.ArgumentTypeError(msg)

def valid_name(name):
    """ Checks if task's name is not longer than 20 characters. """
    if len(name) > 20:
        raise argparse.ArgumentTypeError("Maximum length is 20 characters.")
    return name


def main():
    # top-level parser
    parser = argparse.ArgumentParser(
        epilog='Multi-word values'
        ' must be encased in quotes, like "that".')
    subparsers = parser.add_subparsers()

    # subparser for the "add" command
    create_parser = subparsers.add_parser('add', help='create new task')
    create_parser.set_defaults(action='add')
    create_parser.add_argument(
        '--name',
        type=valid_name,
        required=True,
        help='name of the task (required, max. 20 characters)',
        metavar='')
    create_parser.add_argument(
        '--deadline',
        type=valid_date,
        help='task\'s deadline in ISO format (yyyy-mm-dd)',
        metavar='')
    create_parser.add_argument(
        '--description',
        type=str,
        help='description of the task',
        metavar='')

    # subparser for the "update" command
    update_parser = subparsers.add_parser('update', help='update task')
    update_parser.set_defaults(action='update')
    update_parser.add_argument('TASK_HASH', help='Task identifier')
    update_parser.add_argument(
        '--name',
        type=str,
        help='name of the task',
        metavar='')
    update_parser.add_argument(
        '--deadline',
        type=valid_date,
        help='task\'s deadline  in ISO format (yyyy-mm-dd)',
        metavar='')
    update_parser.add_argument(
        '--description',
        type=str,
        help='description of the task',
        metavar='')

    # subparser for the "delete" command
    delete_parser = subparsers.add_parser('delete', help='delete task')
    delete_parser.set_defaults(action='delete')
    delete_parser.add_argument('TASK_HASH', type=str, help='Task identifier')

    # subparser for the "list" command
    list_parser = subparsers.add_parser('list', help='list tasks')
    list_parser.set_defaults(action='list')
    list_group = list_parser.add_mutually_exclusive_group(required=True)
    list_group.add_argument('--all', action='store_true')
    list_group.add_argument('--today', action='store_true')

    args = parser.parse_args()

    task_manager = TaskManager()

    if args.action == "add":
        task_manager.add_task(args.name, args.deadline, args.description)
    elif args.action == "update":
        task_manager.update_task(
            args.TASK_HASH,
            args.name,
            args.deadline,
            args.description)
    elif args.action == "delete":
        task_manager.delete_task(args.TASK_HASH)
    elif args.action == "list":
        if args.all:
            task_manager.list_tasks('all')
        else:
            task_manager.list_tasks('today')


if __name__ == '__main__':
    main()
