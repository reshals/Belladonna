#database like engine for python scripts wrote by ~ reshals
#v0.1 PROTOTYPE
#engine meant for simple file and dir based information storaging

import os
from config import db_folder

#debug var
bypass_exist = True

class belladonna:
	def __init__(self, db_path):
		self.db_folder = db_folder
		self.db_path = db_path
		self.db = self.db_path.split("/")[-1]
		self.add = self.add_()
		#DEBUG
		#print(self.db)
		#print(self.db_path)

	class add_:
		def database(self, database_name, outer_class):
			database_dir = f"{outer_class.db_folder}/{database_name}"
			if os.path.exists(database_dir):
				print("Database exists!")
			else:
				os.makedirs(database_dir, exist_ok=bypass_exist)
				
		def table(self, table_name, database_name, outer_class):
			table_dir = f"{outer_class.db_folder}/{database_name}/{table_name}"
			if os.path.exists(table_dir):
				print("Table exists!")
			else:
				os.makedirs(table_dir, exist_ok=bypass_exist)
				
		def column(self, column_name, table_name, database_name, outer_class):
			column_dir = f"{outer_class.db_folder}/{database_name}/{table_name}/{column_name}"
			if os.path.exists(column_dir):
				print("Column exists!")
			else:
				os.makedirs(column_dir, exist_ok=bypass_exist)
				
		def object(self, object_name, column_name, table_name, database_name, outer_class):
			object_file = f"{outer_class.db_folder}/{database_name}/{table_name}/{column_name}/{object_name}"
			if os.path.exists(object_file):
				print("Object exists!")
			else:
				file_touch = open(object_file, 'x')
				file_touch.close()
				
		def data(self, payload, object_name, column_name, table_name, database_name, outer_class):
			object_file = f"{outer_class.db_folder}/{database_name}/{table_name}/{column_name}/{object_name}"
			with open(object_file, 'a+' ) as column_file:
				column_file.writelines(f"{payload}\n")

	class read_:
		def database(self, database_name, outer_class):
			print("teste2")
			database_dir = f"{outer_class.db_folder}/{database_name}"
			if not os.path.exists(database_dir):
				print("Database does not exist!")
			else:
				print("teste3")
				tables = os.listdir(database_dir)
			for table in tables:
				print(table)
				
		def table(self, table_name, database_name, outer_class):
			table_dir = f"{outer_class.db_folder}/{database_name}/{table_name}"
			if not os.path.exists(table_dir):
				print("Table does not exist!")
				return 1
			else:
				columns = os.listdir(table_dir)
			for column in columns:
				print(column)
				
		def column(self, column_name, table_name, database_name, outer_class):
			column_dir = f"{outer_class.db_folder}/{database_name}/{table_name}/{column_name}"
			if not os.path.exists(column_dir):
				print("Column does not exist!")
				return 1
			else:
				objects = os.listdir(column_dir)
			for object_ in objects:
				print(object_)

		def object(self, object_name, column_name, table_name, database_name, outer_class):
			object_file = f"{outer_class.db_folder}/{database_name}/{table_name}/{column_name}/{object_name}"
			if not os.path.exists(object_file):
				print("Object does not exist!")
				return 1
			else:
				with open(object_file, 'r') as object_file:
					print(object_file.read())

	class retrieve_:
		def database(self, database_name, outer_class):
			database_dir = f"{outer_class.db_folder}/{database_name}"
			if not os.path.exists(database_dir):
				print("Database does not exist!")
				return 1
			else:
				tables = os.listdir(database_dir)
			return tables

		def table(self, table_name, database_name, outer_class):
			table_dir = f"{outer_class.db_folder}/{database_name}/{table_name}"
			if not os.path.exists(table_dir):
				print("Table does not exist!")
				return 1
			else:
				columns = os.listdir(table_dir)
			return columns


#example usage 
if __name__ == "__main__":
	db = belladonna("~/belladonna/dbs/test")
	
	db.add.database("test", db)
	db.add.table("test_table", "teste", db)
	db.add.column("test_column", "test_table", "test", db)
	db.add.object("test_object", "test_column", "test_table", "test", db)
	db.add.data("super duper cool payload", "test_object", "test_column", "test_table", "test", db)
	
	db.read.database("test", db)
