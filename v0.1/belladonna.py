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
		self.new = self.new_()
		self.new_at = self.new_at_()
		self.read = self.read_()
		self.search = self.search_()
		self.edit = self.edit_()
		self.delete = self.delete_()

	class new_:
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

	class new_at_:
		def database(self, database_path, outer_class):
			database_dir = f"{outer_class.db_folder}/{database_path}"
			if os.path.exists(database_dir):
				print("Database exists!")
			else:
				os.makedirs(database_dir, exist_ok=bypass_exist)

		def table(self, table_path, outer_class):
			table_dir = f"{outer_class.db_folder}/{table_path}"
			if os.path.exists(table_dir):
				print("Table exists!")
			else:
				os.makedirs(table_dir, exist_ok=bypass_exist)

		def column(self, column_path, outer_class):
			column_dir = f"{outer_class.db_folder}/{column_path}"
			if os.path.exists(column_dir):
				print("Column exists!")
			else:
				os.makedirs(column_dir, exist_ok=bypass_exist)

	class read_:
		def database(self, database_name, outer_class):
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
				for dir_table in os.scandir(f"{search_entry}/{dir_db.name}"):
					for dir_column in os.scandir(f"{search_entry}/{dir_db.name}/{dir_table.name}"):
						if(dir_column.is_dir()):
							if(dir_column.name == column_name):
								no_result = False
								return_.append(f"{outer_class.db_folder}/{dir_db.name}/{dir_table.name}/{dir_column.name}")
			if(no_result): return 1
			else: return return_

		def object(self, object_name, outer_class):
			search_entry = f"{outer_class.db_folder}".split("\n")[0]
			no_result = True
			return_ = []
			for dir_db in os.scandir(search_entry):
				for dir_table in os.scandir(f"{search_entry}/{dir_db.name}"):
					for dir_column in os.scandir(f"{search_entry}/{dir_db.name}/{dir_table.name}"):
						for dir_object in os.scandir(f"{search_entry}/{dir_db.name}/{dir_table.name}/{dir_column.name}"):
							if(dir_object.is_file()):
								if(dir_object.name == object_name):
									no_result = False
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

		def data_at(self, data, object_path, outer_class):
			no_result = True
			return_ = []
			if(object_path.is_file()):
				with open(object_path, 'r') as object_file:
					for line in object_file.readlines():
						if data in line:
							no_result = False
							return_.append(line)
							print("debug successfull")
			else: return 1
			if(no_result): return 1
			else: return return_

	class edit_:
		def database(self, new_database_name, database_name, outer_class):
			database_path = f"{outer_class.db_folder}/{database_name}"
			new_database_path = f"{outer_class.db_folder}/{new_database_name}"
			if not os.path.exists(database_path):
				print("Database does not exist!")
				return 1
			elif os.path.exists(new_database_path):
				print("Cant rename, name already taken!")
				return 1
			else:
				print(database_path)
				os.rename(database_path, f"{outer_class.db_folder}/{new_database_name}")
				return 0
				
		def table(self, new_table_path, table_path, outer_class):
			new_table_path = f"{outer_class.db_folder}/{new_table_path}"
			table_path = f"{outer_class.db_folder}/{table_path}"
			print(table_path)
			if not os.path.exists(table_path):
				print("Table does not exist!")
				return 1
			elif os.path.exists(new_table_path):
				print("Cant rename, name already taken!")
				return 1
			else:
				print(new_table_path)
				os.rename(table_path, new_table_path)
				return 0

		def column(self, new_column_path, column_path, outer_class):
			new_column_path = f"{outer_class.db_folder}/{new_column_path}"
			column_path = f"{outer_class.db_folder}/{column_path}"
			if not os.path.exists(column_path):
				print("Column does not exist!")
				return 1
			elif os.path.exists(new_column_path):
				print("Cant rename, name already taken!")
				return 1
			else:
				os.rename(column_path, new_column_path)
				return 0

		def object(self, new_object_path, object_path, outer_class):
			new_object_path = f"{outer_class.db_folder}/{new_object_path}"
			object_path = f"{outer_class.db_folder}/{object_path}"
			if not os.path.exists(object_path):
				print("Object does not exist!")
				return 1
			elif os.path.exists(new_object_path):
				print("Cant rename, name already taken!")
				return 1
			else:
				os.rename(object_path, new_object_path)
				return 0

		def data(self, value, field, object_path, outer_class):
			object_path = f"{outer_class.db_folder}/{object_path}"
			found = False
			with open(object_path, 'r') as object_file:
				lines = object_file.readlines()
			with open(object_path, 'w') as object_file:
				for line in lines:
					if field in line:
						found = True
						object_file.write(f"{field} = {value}\n")
					else:
						object_file.write(line)
			if(found): return 0
			else: return 1

	class delete_:
		def database(self, database_name, outer_class):
			database_path = f"{outer_class.db_folder}/{database_name}"
			if not os.path.exists(database_path):
				print("Database not found!")
				return 1
			else:
				os.system(f"rm -rf {database_path}")
				return 0

		def table(self, table_path, outer_class):
			print(table_path)
			if not os.path.exists(table_path):
				print("Table not found!")
				return 1
			else:
				print("Else condition")
				os.system(f"rm -rf {table_path}")
				return 0

		def column(self, column_path, outer_class):
			if not os.path.exists(column_path):
				print("Column not found!")
				return 1
			else:
				sure = input(f"sure to delete the following path? [Y/N] -> {column_path} <- $ ")
				if(sure == "Y"): os.system(f"rm -rf {column_path}")
				return 0


#example usage 
if __name__ == "__main__":
	db = belladonna("~/belladonna/dbs/test")
	
	db.add.database("test", db)
	db.add.table("test_table", "teste", db)
	db.add.column("test_column", "test_table", "test", db)
	db.add.object("test_object", "test_column", "test_table", "test", db)
	db.add.data("super duper cool payload", "test_object", "test_column", "test_table", "test", db)
	db.read.database("test", db)
	print(db.search.database("test", db))
	print(db.search.table("test_table", db))
	print(db.search.column("test_column", db))
	print(db.search.object("test_object", db))
	print(db.search.data("payload", db))
	print(db.search.data_at("payload", "~/belladonna/dbs/test/test_table/test_column/test_object", db))
