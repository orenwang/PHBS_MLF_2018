
# coding: utf-8

# # Import raw data (all midi files) and export pre-test data (single track midi files for guitar, piano or strings)

# ## 1. Import modules and set the path to where the midi files are

# In[9]:


from mido import MidiFile
import os
path = r'E:\Desktop\MLFproject\MIDI_file\test_select'


# ## 2. Scan all files that end with ".mid", and turn them into objects

# In[10]:


totalfiles = []
for path, dirs, files in os.walk(path):
    for filename in files:
        if (filename.endswith('.MID')) or (filename.endswith('.mid')):
            fullpath = os.path.join(path, filename)
            try:
                mid = MidiFile(fullpath)
                totalfiles.append(mid)
            except:
                continue
#Show how many midi we got
len(totalfiles)


# ## 3. Select those with track name 'guitar' 

# In[11]:


selectedtracks = []
for i in totalfiles:
    m = 0
    for j, track in enumerate(i.tracks):
        if ('guitar' in track.name) or ('Guitar' in track.name) or ('acoustic guitar' in track.name) or ('Acoustic Guitar' in track.name) or ('Acoustic guitar' in track.name):
            selectedtracks.append(track)
#Show how many tracks we got
len(selectedtracks)


# ## 4. Cut every track to a same length, probably 30 seconds. See: https://mido.readthedocs.io/en/latest/midi_files.html

# ## 5. Put each 30s-track in a new midi file, see also: https://mido.readthedocs.io/en/latest/midi_files.html

# ## 6. Do the same for 'piano'

# ## 7. Do the same for 'strings'

# In[ ]:


# #
# totalfiles = []
# for path, dirs, files in os.walk(path):
#     for filename in files:
#         if (filename.endswith('.MID')) or (filename.endswith('.mid')):
#             fullpath = os.path.join(path, filename)
#             try:
#                 mid = MidiFile(fullpath)
#                 totalfiles.append(mid)
#             except:
#                 continue
# #Show how many midi we got
# len(totalfiles)


# In[ ]:


# selectedmidi = []
# for i in totalfiles:
#     m = 0
#     n = 0
#     for j, track in enumerate(i.tracks):
#         if (track.name == 'guitar') or (track.name == 'Guitar') or (track.name == 'acoustic guitar') or (track.name == 'Acoustic Guitar') or (track.name == 'Acoustic guitar'):
#             m = 1
#         if (track.name == 'voice') or (track.name == 'Voice') or (track.name == 'VOICE') or (track.name == 'vocal') or (track.name == 'Vocal') or (track.name == 'VOCAL') :
#             n = 1
#     if (m == 1) and (n == 1):
#         selectedmidi.append(i)


# ## Show messages in the first selected track

# In[12]:


for i in selectedtracks[0:1]:
    for msg in track:
        print(msg)
# print(selectedtracks[0])


# In[1]:


# for i in selectedmidi:
#     for j, track in enumerate(i.tracks):
#         print('Track {}: {}'.format(j, track.name))

