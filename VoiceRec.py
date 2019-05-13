import speech_recognition as sr 
import os
import argparse
import pyaudio
import wave
from pydub import AudioSegment

def main():
	r = sr.Recognizer() 
	harvard = sr.AudioFile('voice.wav')
	with harvard as source:
		audio = r.record(source)

	print( type(audio))
	#,language="zh-CN"
	print(r.recognize_google(audio)

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
					#wav_path = dirpath + '/' + wav_filename
					wav_path = dirpath + '/' + "voice.wav"
					print('CONVERTING: ' + str(filepath))
					file_handle = track.export(wav_path, format='wav')
					os.remove(filepath)
				except:
					print("ERROR CONVERTING " + str(filepath))

def record(): 
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	CHUNK = 512
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "recordedFile.wav"
	device_index = 2
	audio = pyaudio.PyAudio()

	print("----------------------record device list---------------------")
	info = audio.get_host_api_info_by_index(0)
	numdevices = info.get('deviceCount')
	for i in range(0, numdevices):
			if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
				print ("Input Device id ", i, " - ", audio.get_device_info_by_host_api_device_index(0, i).get('name'))

	print("-------------------------------------------------------------")

	index = int(input())
	print("recording via index "+str(index))

	stream = audio.open(format=FORMAT, channels=CHANNELS,
					rate=RATE, input=True,input_device_index = index,
					frames_per_buffer=CHUNK)
	print ("recording started")
	Recordframes = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		Recordframes.append(data)
	print ("recording stopped")

	stream.stop_stream()
	stream.close()
	audio.terminate()

	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(Recordframes))
	waveFile.close()

#record()
convert()
#main()					