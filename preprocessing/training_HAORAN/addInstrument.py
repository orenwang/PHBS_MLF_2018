import os
path = r'E:\Desktop\midi_ready\midifiles'


for path, dirs, files in os.walk(path):
  i = 0
  for filename in files:
    fullpath = os.path.join(path, filename)
    try:
      RPR_InsertMedia(fullpath, 3)
      for j in range(5):
        
        ### Unmute one track
        MediaTrack = RPR_GetSelectedTrack(0, j)
        RPR_SetMediaTrackInfo_Value(MediaTrack, 'B_MUTE', 0)  #0:unMute; 1:Mute;
        RPR_Main_SaveProject(0, False)
        
        ### Render
        RPR_RenderFileSection('E:\Desktop\midi_ready\mrender01.rpp', 'E:\Desktop\midi_ready\mtrain\mtrain_{}{}.wav'.format(str(i),str(j)), 0, 1, 1)
        
        ### Mute again
        MediaTrack = RPR_GetSelectedTrack(0, j)
        RPR_SetMediaTrackInfo_Value(MediaTrack, 'B_MUTE', 1)  #0:unMute; 1:Mute;
    except:
      continue
    i += 1

RPR_Main_OnCommand(40341, 0) #Mute all tracks
RPR_Main_SaveProject(0, False)


### Insert midi
#RPR_InsertMedia('E:\Desktop\midi_ready\midifiles\house_of_the_rising_sunguit_singletrack02.mid', 3)

#for i in range(5):
#  MediaTrack = RPR_GetSelectedTrack(0, i)
#  Boolean = RPR_SetMediaTrackInfo_Value(MediaTrack, 'B_MUTE', 0)  #0:unmute; 1:mute;
#  RPR_Main_SaveProject(0, False)

### Render
#  RPR_RenderFileSection('E:\Desktop\midi_ready\mrender01.rpp', 'E:\Desktop\midi_ready\mtrain\mtrain_2{}.wav'.format(str(i)), 0, 1, 1)

#  MediaTrack = RPR_GetSelectedTrack(0, i)
#  Boolean = RPR_SetMediaTrackInfo_Value(MediaTrack, 'B_MUTE', 1)  #0:unmute; 1:mute;





#from reaper_python import *
#import pynput


#RPR_Main_openProject('E:\Desktop\midi_ready\mrender01.rpp')
#RPR_GetSelectedTrack(0, 2)
#RPR_SetCursorContext(0, 0)
#RPR_SetEditCurPos(100, 0, 0)
#MediaItem = RPR_GetMediaItem(0, 0)
#keyboard = pynput.keyboard.Controller()
#item = RPR_MoveMediaItemToTrack(MediaItem, MediaTrack)
#RPR_Main_OnCommand(40005, 0) #Remove tracks
#RPR_Main_OnCommand(40023, 0)  #New project
#RPR_Main_OnCommand(40001, 0) #Insert new track
#RPR_Main_OnCommand(40886, 0) #Close all projects
#keyboard.press('n')
#keyboard.release('n')
