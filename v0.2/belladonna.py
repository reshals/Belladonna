import os
import json
import fnmatch

db_folder = "dbs/"
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
		def data(self, json_payload, object_name, column_name, table_name, database_name, outer_class):
			object_path = f"{outer_class.db_folder}/{database_name}/{table_name}/{column_name}/{object_name}"
			with open(object_path, 'a+' ) as object_file:
				json.dump(json_payload, object_file)
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
				
		def object(self, object_path, outer_class):
			object_path = f"{outer_class.db_folder}/{object_path}"
			print(object_path)
			if os.path.exists(object_file):
				print("Object exists!")
			else:
				file_touch = open(object_file, 'x')
				file_touch.close()
		def data(self, json_payload, object_path, outer_class):
			object_path = f"{outer_class.db_folder}/{database_name}/{table_name}/{column_name}/{object_name}"
			with open(object_path, 'a+' ) as object_file:
				json.dump(json_payload, object_file)
