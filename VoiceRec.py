import speech_recognition as sr 
import os
import argparse

from pydub import AudioSegment

def main():
	r = sr.Recognizer() 
	harvard = sr.AudioFile('2.wav')
	with harvard as source:
		audio = r.record(source)

	print( type(audio))
	print(r.recognize_google(audio))

formats_to_convert = ['.m4a']

def convert():
	for (dirpath, dirnames, filenames) in os.walk("./"):
		for filename in filenames:
			if filename.endswith(tuple(formats_to_convert)):

				filepath = dirpath + '/' + filename
				(path, file_extension) = os.path.splitext(filepath)
				file_extension_final = file_extension.replace('.', '')
				try:
					track = AudioSegment.from_file(filepath,
							file_extension_final)
					wav_filename = filename.replace(file_extension_final, 'wav')
					wav_path = dirpath + '/' + wav_filename
					print('CONVERTING: ' + str(filepath))
					file_handle = track.export(wav_path, format='wav')
					os.remove(filepath)
				except:
					print("ERROR CONVERTING " + str(filepath))
convert()
main()					