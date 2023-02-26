import winsound
import random
notes = {'C': 262, 'D': 294, 'E': 330, 'F': 349, 'G': 392, 'A': 440, 'B': 494}
duration = {'1': 1000, '2': 500, '4': 250}
scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
chords = ['C2 E2 G2', 'D2 F2 A2', 'E2 G2 B2', 'F2 A2 C4', 
          'G2 B2 D4', 'A2 C4 E4', 'B2 D4 F4']
melody = ""
for i in range(8):
    note = random.choice(scale)
    length = random.choice(['1','1','1','1','1','1','1','1',
                            '2','2','4'])
    melody += note + length + " "
melody += "| "
for i in range(8):
    chord = random.choice(chords)
    length = random.choice(['1','1','1','1',
                            '2'])
    melody += chord + length + " "
print(melody)
for note in melody.split():
    if note == '|':
        continue
    if len(note) == 3:
        pitch = notes[note[0]]
        length = duration[note[1]]
        winsound.Beep(pitch,length)
    elif len(note) == 5:
        pitch_1 = notes[note[0]]
        pitch_2 = notes[note[3]]
        pitch_3 = notes[note[4]]
        length = duration[note[6]]
        winsound.Beep(pitch_1,length//3)
        winsound.Beep(pitch_3,length//3)
        winsound.Beep(pitch_3,length//3)