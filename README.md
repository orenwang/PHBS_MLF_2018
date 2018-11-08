# Instrument Classification

> Automatic instrument classification from music

We intend to perform automatic identification of instrument classes from monophonic and polyphonic music audio via machine learning method. We only focus on three different classes of instrument, which are piano, guitar and strings.



## Data Preprocessing

### 1. Extract single tracks from multi-track '.mid' files to new '.mid' files


Midi:
> A kind of file format, containing digital information of music

![](midi_Intro.png)

_Raw data retrived from https://www.reddit.com/r/WeAreTheMusicMakers/comments/3ajwe4/the_largest_midi_collection_on_the_internet/_

### 2. Write scripts to control instruments, making '.mid' files into '.wav' files

Use Reaper 5
> Complete digital audio production application for computers

Use Kontakt 6
> Make inputs like midi generate sound

Generate music
> ~150 single tracks to generate ~1000 30s .wavs files.

![](reaper.png)

### 3. Extract features by frames, and save in a '.csv' file

> I.Slice them by sampling rate = 10000, hop length = 250;

> II. Get mean of MFCCs and their derivatives by seconds;

![](mfcc.png)

> III. Write '.csv' file with labels of three instrument classes;

> IV. Delete silent rows in '.csv' file.

![](silence_detection.png)

### 4. Alibaba Cloud: Run tabular deep learning model with fast.ai based on Pytorch




## Importance

1. Few music database are available for analysis use, mostly in the form of songs. Extracting more information from songs will significantly contribute to the industry.
2. Bands, singers and studios spend tremendous time on making existing music back into scores or midi.
3. A potential for automatic accompaniment generation.

## Tools

Mido - MIDI Objects for Python
librosa
Scikit-learn
fast.ai & Pytorch
```sh
import mido, sklearn, fast.ai, librosa
```

## Group Members

_Wang Haoran_
_1701213100_
_qwerjeff_

_Zhe Wang_
_1791213114_
_dragonwdl_

_Daniel Kwesi Wobil_
_1701213207_
_answob_

_Yizhe Ren_
_1701213087_
_engerous_

