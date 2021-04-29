import PySimpleGUI as sg
import vlc



sg.theme("DarkAmber")


layout = [[sg.In() ,sg.FileBrowse(file_types=(("Audio Files", "*.mp3 *.flac"), ("Video File", "*mp4 *.mkv")), key="-IN-")],
          [sg.Button('Read'), sg.Button('Play'),sg.Button('Stop')],
          [sg.Slider(range=(0, 100), size=(15, 10), orientation='h', default_value='50', key="-vol-"), sg.Button('Volume Set')],
          ]


window=sg.Window("Test", layout, grab_anywhere=False)

p = vlc.MediaPlayer("capa.mp3")
# v = values["-vol-"]
# p.audio_set_volume(int(v))

while True:
  event, values=window.read()
  vol = int(values['-vol-'])
  print (vol)
  print(event, values)
  if event==sg.WIN_CLOSED:
    break
#  elif event=="Volume Set":
#    p.audio_set_volume(int(v))
#    print(v)
  elif event=="Read":
    p.stop()
    file = values["-IN-"]
    p = vlc.MediaPlayer(file)
  elif event=="Play":
    p.play()
  elif event=="Stop":
    p.stop()
window.close()