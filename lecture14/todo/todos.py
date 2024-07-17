from todo.model import Todo
from todo.db_handler import DBHandler
from todo import DB_READ_ERROR
from pathlib import Path

import datetime

from todo.responses import TodoResponse, DBResponse

class TodoList:

    def __init__(self, db_path: Path) -> None:
        self._db_handler = DBHandler(db_path)

    def add(self, task: str, category:str) -> TodoResponse:
        """Add a new todo to the database"""
        
        todo = Todo(task, category)

        reader = self._db_handler.read_todos()
        
        if reader.error  == DB_READ_ERROR:
            return TodoResponse(todo.to_dict(), reader.error)
        
        count = len(reader.todo_list)
        todo._position = count if count else 0

        reader.todo_list.append(todo.to_dict())

        writer = self._db_handler.write_todos(reader.todo_list)

        return TodoResponse(todo.to_dict(), writer.error)



    def get_todo(self) -> DBResponse:
        """Return todo list"""

        reader = self._db_handler.read_todos()
        return DBResponse(reader.todo_list, reader.error)
    
    def complete(self, position:int) -> DBResponse:

        reader = self._db_handler.read_todos()
        reader.todo_list[position - 1]['status'] = 2
        reader.todo_list[position - 1]['completed_at'] = datetime.datetime.now().isoformat()

        writer = self._db_handler.write_todos(reader.todo_list)

        return DBResponse(writer.todo_list, writer.error)
