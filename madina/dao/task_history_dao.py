from datetime import datetime
from dao.BaseDao import Dao
import sys

sys.path.append("/nursezim/classes")
from classes.task_history import Task_History

class TaskHistoryDAO(Dao):
    def __init__(self, db_path):
        super().__init__(db_path)

    def insert(self, task_history: Task_History):
        query = """
            INSERT INTO task_history (task_description, date_added, tag, operation, user_id)
            VALUES (?, ?, ?, ?, ?)
        """
        date_added = task_history.get_date_added() or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.execute_query(query, (
            task_history.get_task_description(),
            date_added,
            task_history.get_tag(),
            task_history.get_operation(),
            task_history.get_user_id()
        ))
        task_history.set_id(self._cursor.lastrowid)
        return task_history

    def get_all_history(self):
        query = """
            SELECT id, task_description, date_added, tag, operation, user_id
            FROM task_history
            ORDER BY date_added DESC
        """
        rows = self.fetch_all(query)
        return [self._map_row_to_task_history(row) for row in rows]

    def get_history_by_user_id(self, user_id):
        query = """
            SELECT id, task_description, date_added, tag, operation, user_id
            FROM task_history
            WHERE user_id = ?
            ORDER BY date_added DESC
        """
        rows = self.fetch_all(query, (user_id,))
        return [self._map_row_to_task_history(row) for row in rows]

    def delete_history_by_id(self, history_id):
        query = "DELETE FROM task_history WHERE id = ?"
        self.execute_query(query, (history_id,))

    def _map_row_to_task_history(self, row):
        return Task_History(
            task_description=row[1],
            date_added=row[2],
            tag=row[3],
            operation=row[4],
            user_id=row[5],
            id=row[0]
        )