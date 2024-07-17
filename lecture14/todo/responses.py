from todo.aliases import DictStr, TodoListDict
from typing import NamedTuple

class TodoResponse(NamedTuple):
    todo: DictStr
    error: int

class DBResponse(NamedTuple):
    todo_list: TodoListDict
    error: int
