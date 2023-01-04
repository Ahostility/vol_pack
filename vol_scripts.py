import subprocess as sp
import sys
import uuid
from vol_tech.dirs import DIR_VOL
from datetime import datetime


class Volatility:
	def __init__(self, file_path, result_path):
		self.file_path = file_path
		self.result_path = result_path
		self.plugins = [
                		'windows.info', # time 0:00:00.936504.00
				#'windows.pslist', # time 0:00:01.378474.00
				#'windows.pstree', # time 0:00:01.574978.00
				###'windows.psscan', # time 0:00:32.391601.00
				###'windows.filescan.FileScan', # time 0:00:48.872228.00
				#'windows.privileges', # time 0:00:02.345223.00
				#'windows.registry.printkey', # time 0:00:02.640681.00
				#'windows.registry.hivelist', # time 0:00:01.103278.00
				#'windows.registry.hivescan', # time 0:00:11.857060.00
				#'windows.cmdline', # time 0:00:01.754820.00
				#'windows.envars.Envars', # time 0:00:05.398817.00
				#'windows.lsadump.Lsadump',
				##'windows.svcscan.SvcScan',
				##'windows.malfind', # time 0:00:18.553562.00
				###'windows.statistics', # time 0:00:02.0527683696.48
				###'windows.netscan.NetScan' # time 0:01:11.257590.00
				###'windows.verinfo.VerInfo',
				]

	# Running commands in sequence

	def vol_write(self):
		with open(str(self.result_path) + str(uuid.uuid4()) + '.txt', 'w') as out_file:
			for plugin in self.plugins:
				res = sp.run(['python', DIR_VOL, '-f', self.file_path, plugin],
					stdout=sp.PIPE,
					encoding='utf-8'
					)
				out_file.write('=====================' + plugin + '=====================\n' + res.stdout + '\n')
		out_file.close()


if __name__ == '__main__':
	start_time = datetime.now()
	obj = Volatility(sys.argv[1], sys.argv[2])
	obj.vol_write()
	print(datetime.now() - start_time)
