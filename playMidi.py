#! python2

from midiutil.MidiFile import MIDIFile
import sound, time
import threading


class PlayMidiThread(threading.Thread):
  def __init__(self, n, t):
    super(PlayMidiThread, self).__init__()
    self.n = n
    self.t = t

  def run(self):
    sound.stop_all_effects()
    player = sound.MIDIPlayer('output.mid')
    player.play()
    time.sleep(1)


class PlayMidi:
  @staticmethod
  def play_chord_midi(midi_nums, bpm, duration):
    track = len(midi_nums)
    midi = MIDIFile(5)
    midi.addTempo(0, 0, bpm)
    midi.addProgramChange(0, 0, 0, 1)
    
    for i in range(len(midi_nums)):
      # track, channel, pitch, time, duration, volume
      midi.addNote(i, 0, midi_nums[i], 0, duration, 100)
    
    with open('output.mid', 'w') as f:
      midi.writeFile(f)

    midi_thread = PlayMidiThread(len(midi_nums), len(midi_nums))
    midi_thread.start()
