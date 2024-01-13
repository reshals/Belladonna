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
		print(self.db)
		print(self.db_path)

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

teste = belladonna(f"{db_folder}/teste")
teste.add.database("teste", teste)
teste.add.table("teste_table", "teste", teste)
teste.add.column("teste_column", "teste_table", "teste", teste)
teste.add.object("teste_object", "teste_column", "teste_table", "teste", teste)
teste.add.data("super duper cool payload", "teste_object", "teste_column", "teste_table", "teste", teste)