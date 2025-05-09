from db_handler import DataBaseHandler
from db_config import *

db = DataBaseHandler(PostgresConfig)
db.connect()
print(db.select_all("users"))
