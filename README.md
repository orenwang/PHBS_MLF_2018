# Instrument Classification
> Automatic instrument classification from music

We intend to perform automatic identification of instrument classes from monophonic and polyphonic music audio via machine learning method. We only focus on three different classes of instrument, which are piano, guitar and strings.



## Database

We build our own audio database based on a selection from 130,000 midi files from public website as follows: 
1. We select midi files that have been already labeled by one of the three instruments above.
2. We then extract and saperate them either into single-track midi files (monophonic) or into multi-track midi files (polyphonic). 
3. We use instrument sounds sampler, such as Kontakt 5, to render midi files into music.
4. We label our data during the music generation process.

Midi:
> A kind of file format, containing digital information of music

![](midi_Intro.png)

Instrument sampler
> Make inputs like midi generate sound


## Importance

1. Few music database are available for analysis use, mostly in the form of songs. Extracting more information from songs will significantly contribute to the industry.
2. Bands, singers and studios spend tremendous time on making existing music back into scores or midi.
3. A potential for automatic accompaniment generation.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Python Modules

Mido

```sh
import mido
```

