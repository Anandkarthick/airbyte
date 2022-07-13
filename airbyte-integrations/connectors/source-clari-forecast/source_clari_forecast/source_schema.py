import json
from .schemas import source_schema
from airbyte_cdk.logger import AirbyteLogger

def get_schema():
    return source_schema()


class ClariSchemas:

    def __init__(self) -> None:
        self.tables = get_schema().keys()
        self.schemas = {}
        self.logger = AirbyteLogger()

    def __fetch_schema__(self):
        all_schemas = get_schema()
        for table in self.tables:
            _schema = all_schemas[table]
            self.schemas.update({table : _schema})

    def get_schemas(self):
        self.logger.info(f"fetching schemas for tables {self.tables}")
        self.__fetch_schema__()
        self.logger.info(f"Schemas fetched successfully")
        return self.schemas
