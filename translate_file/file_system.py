from googletrans import Translator

from typing import List
import json
from pprint import pprint


class My_file():
	"""Родительский класс, что бы получить file_name файл"""
	file_name: str
	file_path: str
	

	def __init__(self, file_name, file_path):
		self.file_name = file_name
		self.file_path = file_path


	def __str__(self) -> str:
		return 'file name is {} path {}'.format(self.file_name, self.file_path)
	

class Triple_file_extension(My_file):
	translate_second_file_name:str = 'ru_RU'

	list_extensions: List 
	first_file_name:str
	second_file_name:str
	last_file_name:str
	
	# не используется заготовка если понадобится узнать путь

	def __init__(self,file_name, file_path):
		super().__init__(file_name, file_path)
		self.list_extensions = file_name.split('.')
		self._get_all_extensions()
	

	def create_file(self):
		new_name_path_file = str()
		translate_lines = list()
		
		if len(self.list_extensions) == 3:
			self._create_all_translate_lines(translate_lines=translate_lines)

			new_name_path_file = self._get_new_path_name()
			self._creating_a_new_file(new_name_path_file=new_name_path_file, translate_lines=translate_lines)


	# должны ли мы указывать что возвращаем если????
	def _create_all_translate_lines(self, translate_lines: List):
		lang_out = 'ru'
		lang_input = 'en'
		tr = Translator()

		with open(self.file_path +'/'+ self.file_name, 'r') as file:
				lines = file.readlines()
				for line in lines:
					tr_line = tr.translate(text=line, dest=lang_out)
					translate_lines.append(tr_line.text)


	def _creating_a_new_file(self, new_name_path_file, translate_lines):
		with open(new_name_path_file, 'a+', encoding='utf8') as file:
			for line in translate_lines:
				file.write(line+'\n')


	def _get_new_path_name(self)-> str:
		file = self.first_file_name +'.'+ \
			 self.translate_second_file_name +'.'+ \
				 self.last_file_name
		print(self.file_path + file)
		return str(self.file_path + '/' + file)


	def _get_all_extensions(self):
		self.first_file_name = self.list_extensions[-3]
		self.second_file_name = self.list_extensions[-2]
		self.last_file_name = self.list_extensions[-1]


	def __str__(self):
		return super().__str__() + ('file first {} second {} last {}'.format(self.first_file_name,\
		 self.second_file_name,\
		  self.last_file_name))


