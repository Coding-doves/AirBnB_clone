'''storage will be used to call filestorage'''
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
