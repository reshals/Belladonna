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

		def column(self, column_name, table_name, database_name, outer_class):
			column_dir = f"{outer_class.db_folder}/{database_name}/{table_name}/{column_name}"
			if not os.path.exists(column_dir):
				print("Column does not exist!")
				return 1
			else:
				objects = os.listdir(column_dir)
			return objects

		def object(self, object_name, column_name, table_name, database_name, outer_class):
			object_file = f"{outer_class.db_folder}/{database_name}/{table_name}/{column_name}/{object_name}"
			if not os.path.exists(object_file):
				print("Object does not exist!")
				return 1
			else:
				with open(object_file, 'r') as object_file:
					return object_file.read()

		def data(self, data, object_name, column_name, table_name, database_name, outer_class):
			object_file = f"{outer_class.db_folder}/{database_name}/{table_name}/{column_name}/{object_name}"
			with open(object_file, 'r') as object_file:
				for line in object_file.readlines():
					if data in line:
						return line

	class search_:
		def database(self, database_name, outer_class):
			search_entry = f"{outer_class.db_folder}".split("\n")[0]
			no_result = True
			for dir_ in os.scandir(search_entry):
				if(dir_.is_dir()):
					if(dir_.name == database_name):
						no_result = False
						print(f"{outer_class.db_folder}/{database_name}")
						return f"{outer_class.db_folder}/{database_name}"
			if(no_result): return 1

		def table(self, table_name, outer_class):
			search_entry = f"{outer_class.db_folder}".split("\n")[0]
			no_result = True
			return_ = []
			for dir_db in os.scandir(search_entry):
				for dir_table in os.scandir(f"{search_entry}/{dir_db.name}"):
					if(dir_table.is_dir()):
						if(dir_table.name == table_name):
							no_result = False
							return_.append(f"{outer_class.db_folder}/{dir_db.name}/{dir_table.name}")
			if(no_result): return 1
			else: return return_
				
		def column(self, column_name, outer_class):
			search_entry = f"{outer_class.db_folder}".split("\n")[0]
			no_result = True
			return_ = []
			for dir_db in os.scandir(search_entry):
				#print(dir_db.name)
				for dir_table in os.scandir(f"{search_entry}/{dir_db.name}"):
					#print(dir_table.name)
					for dir_column in os.scandir(f"{search_entry}/{dir_db.name}/{dir_table.name}"):
						if(dir_column.is_dir()):
							if(dir_column.name == column_name):
								no_result = False
								#print(f"{outer_class.db_folder}/{dir_db.name}/{dir_table.name}/{dir_column.name}")
								return_.append(f"{outer_class.db_folder}/{dir_db.name}/{dir_table.name}/{dir_column.name}")
			if(no_result): return 1
			else: return return_

		def object(self, object_name, outer_class):
			search_entry = f"{outer_class.db_folder}".split("\n")[0]
			no_result = True
			return_ = []
			for dir_db in os.scandir(search_entry):
				#print(dir_db.name)
				for dir_table in os.scandir(f"{search_entry}/{dir_db.name}"):
					#print(dir_table.name)
					for dir_column in os.scandir(f"{search_entry}/{dir_db.name}/{dir_table.name}"):
						#print(dir_column.name)
						for dir_object in os.scandir(f"{search_entry}/{dir_db.name}/{dir_table.name}/{dir_column.name}"):
							if(dir_object.is_file()):
								if(dir_object.name == object_name):
									no_result = False
									#print(f"{outer_class.db_folder}/{dir_db.name}/{dir_table.name}/{dir_column.name}/{dir_object.name}")
									return_.append(f"{outer_class.db_folder}/{dir_db.name}/{dir_table.name}/{dir_column.name}/{dir_object.name}")
			if(no_result): return 1
			else: return return_
				
		def data(self, data, outer_class):
			search_entry = f"{outer_class.db_folder}".split("\n")[0]
			no_result = True
			return_ = []
			for dir_db in os.scandir(search_entry):
				#print(dir_db.name)
				for dir_table in os.scandir(f"{search_entry}/{dir_db.name}"):
					#print(dir_table.name)
					for dir_column in os.scandir(f"{search_entry}/{dir_db.name}/{dir_table.name}"):
						#print(dir_column.name)
						for dir_object in os.scandir(f"{search_entry}/{dir_db.name}/{dir_table.name}/{dir_column.name}"):
							if(dir_object.is_file()):
								with open(f"{search_entry}/{dir_db.name}/{dir_table.name}/{dir_column.name}/{dir_object.name}", 'r') as object_file:
									for line in object_file.readlines():
										if data in line:
											no_result = False
											#print(line)
											return_.append(line)
			if(no_result): return 1
			else: return return_


#example usage 
if __name__ == "__main__":
	db = belladonna("~/belladonna/dbs/test")
	
	db.add.database("test", db)
	db.add.table("test_table", "teste", db)
	db.add.column("test_column", "test_table", "test", db)
	db.add.object("test_object", "test_column", "test_table", "test", db)
	db.add.data("super duper cool payload", "test_object", "test_column", "test_table", "test", db)
	
	db.read.database("test", db)
