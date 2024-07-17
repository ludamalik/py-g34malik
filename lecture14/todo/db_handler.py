"""This module provides the To-Do database functionality."""

from pathlib import Path
import json
from todo import DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR, SUCCESS

from todo.responses import DBResponse
from todo.aliases import TodoListDict
import logging

class DBHandler:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path
        self.logger = logging.getLogger(__name__)

        self.logger.setLevel(logging.INFO)

        self.stream_handler = logging.StreamHandler()
        self.database_handler = logging.FileHandler('database_logging.log') 
        
        self.stream_handler.setLevel(logging.WARNING) 
        self.database_handler.setLevel(logging.INFO) 

        # Create formatters and add it to handlers
        self.stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        self.database_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.stream_handler.setFormatter(self.stream_format)
        self.database_handler.setFormatter(self.database_format)


        self.logger.addHandler(self.stream_handler)
        self.logger.addHandler(self.database_handler)


    def write_todos(self, todo_list:TodoListDict) -> DBResponse:
        try:
            with self._db_path.open("w") as db:
                json.dump(todo_list, db, indent=4)
            return DBResponse(todo_list, SUCCESS)
            
        except OSError: # Catch file IO problems
            logging.exception(f"Exception {DB_WRITE_ERROR} occurred")
            return DBResponse(todo_list, DB_WRITE_ERROR)
        
    

    def read_todos(self) -> DBResponse:
        try:
            with self._db_path.open("r") as db:
                try:
                    self.logger.warning(f'Opened database {self._db_path} for tasks reading')
                    # print('Database was read successfully!')
                    self.logger.info('Database was read successfully!') 
                    
                    return DBResponse(json.load(db), SUCCESS)
                except json.JSONDecodeError: # Catch wrong JSON format
                    logging.exception(f"Exception {JSON_ERROR} occurred")
                    return DBResponse([], JSON_ERROR)
        except OSError: # Catch file IO problems
            logging.exception(f"Exception {DB_READ_ERROR} occurred")
            return DBResponse([], DB_READ_ERROR)
