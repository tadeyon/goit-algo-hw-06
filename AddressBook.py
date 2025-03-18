from collections import UserDict
from Record import Record


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
    
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError('Instance must be a Record type object.')
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if not self.data.pop(name, None):
            raise ValueError('Record not found.')
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())