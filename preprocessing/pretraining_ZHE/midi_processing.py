# coding: utf-8

# # Import raw data (all midi files) and export pre-test data (single track midi files for guitar, piano or strings)

# ## 1. Import modules and set the path to where the midi files are


from mido import MidiFile
import os
path = r'/Users/dragon/Desktop/Project/MIdi tracks'

print('Numbers counting：')

# ## 2. Scan all files that end with ".mid", and turn them into objects
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
num_total=len(totalfiles)
print('\t'*2,'Total number of midi files:',num_total)


# ## 3. Select those with track name 'guitar'
selectedtracks_guitar = []
for i in totalfiles:
    m = 0
    for j, track in enumerate(i.tracks):
        if ('guitar' in track.name) or ('Guitar' in track.name) or ('acoustic guitar' in track.name) or ('Acoustic Guitar' in track.name) or ('Acoustic guitar' in track.name):
            selectedtracks_guitar.append(track)
#Show how many tracks we got
num_guitar=len(selectedtracks_guitar)
print('\t'*2,'Number of guitar tracks:',num_guitar)


# ## 4. Do the same for 'piano'
selectedtracks_piano = []
for i in totalfiles:
    m = 0
    for j, track in enumerate(i.tracks):
        if ('piano' in track.name) or ('Piano' in track.name) or ('Left piano' in track.name) or ('Right piano' in track.name) or ('Left Piano' in track.name) or ('Right Piano' in track.name):
            selectedtracks_piano.append(track)
#Show how many tracks we got
num_piano=len(selectedtracks_piano)
print('\t'*2,'Number of piano tracks:',num_piano)


# ## 5. Do the same for 'strings'
selectedtracks_strings = []
for i in totalfiles:
    m = 0
    for j, track in enumerate(i.tracks):
        if ('Violin' in track.name) or ('Cuerdas1' in track.name) or ('Cuerdas2' in track.name) or ('Viola' in track.name) or ('Cello' in track.name) or ('Violoncello' in track.name):
            selectedtracks_strings.append(track)
#Show how many tracks we got
num_strings=len(selectedtracks_strings)
print('\t'*2,'Number of strings tracks:',num_strings)


# ## 6. Transfer tracks we exact into midi files
from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
mid.tracks.append(track)


for i in range(0,len(selectedtracks_guitar)):
    mid = MidiFile()
    track = selectedtracks_guitar[i]
    mid.tracks.append(track)
    mid.save('/Users/dragon/Desktop/Project/New midi/Guitar/new_guitar{}.mid'.format(i))
    #Show progress
    print(i if i%5 == 0 else ' ', end = '')

for i in range(0,len(selectedtracks_piano)):
    mid = MidiFile()
    track = selectedtracks_piano[i]
    mid.tracks.append(track)
    mid.save('/Users/dragon/Desktop/Project/New midi/Piano/new_piano{}.mid'.format(i))
    #Show progress
    print(i if i%5 == 0 else ' ', end = '')


for i in range(0,len(selectedtracks_strings)):
    mid = MidiFile()
    track = selectedtracks_strings[i]
    mid.tracks.append(track)
    mid.save('/Users/dragon/Desktop/Project/New midi/Strings/new_strings{}.mid'.format(i))
    #Show progress
    print(i if i%5 == 0 else ' ', end = '')


for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))



