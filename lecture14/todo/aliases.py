from typing import List, Union, TypeAlias, Dict, Any

# List[str]
# StrList = List[str]
StrList: TypeAlias = List[str]

# List[List[Union[strTypeAlias, int, None]]]
ListUnion: TypeAlias = List[List[Union[str, int, None]]]

#  List[Dict[str, Any]]
TodoListDict: TypeAlias = List[Dict[str, Any]]

# DictStr
DictStr: TypeAlias = Dict[str, Any]
