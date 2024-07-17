"""Class model"""
import datetime
from typing import List, Union, Any

from todo.aliases import StrList, ListUnion, DictStr, TodoListDict

class Todo():

    DONE:str = chr(9989)
    PENDING: str = chr(10060)


    COLORS: DictStr = {
        'Learn': 'yellow',
        'Work': 'red',
        'Sports': 'cyan',
        'Study': 'green'
    }

    # keys: List[str] = ['name', 'style', 'width', 'min_width', 'justify']
    keys: StrList = ['name', 'style', 'width', 'min_width', 'justify']

    # values: List[List[Union[str, int, None]]] = [
    values: ListUnion = [
        ["#", "dim", 6, None, "left"],
        ["Todo", None, None, 20, "left"],
        ["Category", None, None, 12, "right"],
        ["Done", None, None, 12, "right"],
    ]

    @staticmethod
    def make_header() -> TodoListDict:
        headers = []
        for v in Todo.values:
            d = dict(zip(Todo.keys, v))
            headers.append(d)
        return headers
    
    @staticmethod
    def get_category_color(category: str) -> Any:
        if category in Todo.COLORS:
            return Todo.COLORS[category]
        return 'white'
    
    @classmethod
    def endwith_sentence(cls, task: str) -> str:
        if not task.endswith("."):
            task += "."
        return task

    def __init__(self, task:str, category:str, 
                 added_at:Any|None=None,
                 completed_at:Any|None= None,
                 status:int|None=None,
                 position:int|None=None
                 ) -> None:

        self._task = Todo.endwith_sentence(task)
        self._category = category
        self._added_at = added_at if added_at is not None else datetime.datetime.now().isoformat()
        self._completed_at = completed_at if completed_at is not NameError else None
        self._status = status if status is not None else 1 # 1 - open
        self._position = position if position is not None else None

    # def __repr__(self) -> str:
    #     return f"({self._task}, {self._category}, {self._added_at}, {self._completed}, {self._status}, {self._position})"

    def to_dict(self) -> Any:
        return {
                'task': self._task,
                'category': self._category,
                'added_at': self._added_at,
                'completed_at': self._completed_at,
                'status': self._status,
                'position': self._position
        }
    
    # def __repr__(self) -> str:
    #     self.__setitem__('task', self._task)
    #     self.__setitem__('category', self._category)
    #     self.__setitem__('added_at', self._added_at)
    #     self.__setitem__('completed_at', self._completed_at)
    #     self.__setitem__('status', self._status)
    #     self.__setitem__('position', self._position)
    #     return super().__repr__()
    
    def __repr__(self) -> str:    
        return str(self.to_dict())
