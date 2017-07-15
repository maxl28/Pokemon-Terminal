import os
import shlex

from adapter.base import TerminalAdapterInterface

class Urxvt(TerminalAdapterInterface):
	command = 'printf "\\e]20;{};\a"'

	@staticmethod
	def is_available():
		return True # Local change only, so I didn't even bother adding a check

	def set_image_file_path(self, image_file_path):
		os.system(self.command.format(image_file_path))

	def clear(self):
		return False
