import ctypes
import os
import random
from time import sleep

def ler_arquivos():
	"""
	Ler os Arquivos da pasta

	:return list: com os arquivos
	"""
	files = os.listdir(os.getcwd())
	image_files = [i for i in files if i.endswith('.gif') or i.endswith('.jpg') or \
		       i.endswith('.jpeg') or i.endswith('.png')]
	return image_files
	

##PROGRAMA PRINCIPAL
if __name__ == '__main__':
	SPI_SETDESKWALLPAPER = 20
	SPIF_UPDATEINIFILE = 1
	TEMPO = 10

	while 1:
		image_files = ler_arquivos()
		
		print(image_files)
		random.shuffle(image_files)
		for image in image_files:
			print("Setting the wallpaper")
			
			ctypes.windll.user32.SystemParametersInfoW(
				SPI_SETDESKWALLPAPER,
				0,
				os.path.abspath(image),
				SPIF_UPDATEINIFILE
			)
			sleep(TEMPO)
