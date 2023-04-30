#Downdoad s3 object in a range

import boto3 
import PySimpleGUI as sg
import pathlib
import os

def principal():

	sg.theme('BrightColors') 
	layout = [
			  [sg.Text('   ',size=(7,2))],
			  [sg.Text('Valor inicial ',size=(15,1))] + [sg.Input(key='inpini')],
			  [sg.Text('Valor final  ',size=(15,1))] + [sg.Input(key='inpfin')],
			  [sg.Text('   ',size=(7,2))],
	          [sg.Button('Ok', size=(7,2))],
	          [sg.Text('   '),
	          [sg.Text(size=(20,1), key = 'patron_out')] +  
	          [sg.Text(size=(200,1), key = 'xmlout')] +  
	          [sg.Text(size=(200,1), key = 'pdfout')]]]


	window = sg.Window('name', layout,size=(490, 280))
	bucket_name=''
	keypath=''
	while True:
		event, values = window.read() 	
		inpini = values['inpini']
		inpfin = values['inpfin']
		tmp_tipo = str(inpini[0:2])
		tmp_ini = int(inpini[2:8])
		tmp_fin = int(inpfin[2:8])
		tmp_fl = range(tmp_ini,tmp_fin + 1)
		

		if tmp_tipo == "FP":
			folder_name=''
			for interval in tmp_fl:
				patron = "FP00" + str(interval)
				window.refresh()
				s3 = boto3.resource('s3')
				bucket = s3.Bucket(bucket_name)
				s3xml = keypath + patron + ".xml"
				s3pdf = keypath + patron + ".pdf"
				if not os.path.isdir(folder_name):
					os.mkdir(folder_name)
				s3.Bucket(bucket_name).download_file(s3xml,str(folder_name)+patron + ".xml")
				s3.Bucket(bucket_name).download_file(s3pdf,str(folder_name)+patron + ".pdf")
				
				window.refresh()


principal()
