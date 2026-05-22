import json

class DatabaseModel:
    def __init__(self, schema_name='enterprise_core'):
        self.schema = schema_name
        self.records = {}
        print(f'[MODEL] Structured data layer active: {self.schema}')

    def insert_record(self, record_id, payload):
        if not record_id or not payload:
            return False
        self.records[str(record_id)] = payload
        return True

    def export_to_json(self):
        try:
            return json.dumps(self.records, indent=4)
        except Exception:
            return '{}'

if __name__ == '__main__':
    db = DatabaseModel()
    db.insert_record('1001', {'username': 'admin', 'active': True})