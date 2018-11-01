#from reaper_python import *
import pynput

#RPR_Main_OnCommand(40023, 0)
#pynput.keyboard.Key.press('n')
#pynput.keyboard.release('n')
#RPR_Main_OnCommand(40001, 0)
#RPR_Main_OnCommand(40886, 0)
#RPR_Main_openProject('E:\Desktop\midi_ready\mrender01.rpp')
#RPR_InsertMedia('E:\Desktop\midi_ready\house_of_the_rising_sunguit_singletrack01.mid', 0)
#RPR_Main_SaveProject(0, False)

RPR_RenderFileSection('E:\Desktop\midi_ready\mrender01.rpp', 'E:\Desktop\midi_ready\mtest.wav', 0, 1, 1)
