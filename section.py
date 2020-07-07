import consts
import playMidi

class Section:
  def __init__(self, tune):
    self.tune_ = tune
    self.root_shift_ = 0
    self.mode_ = tune.mode_
    self.chords_ = []

  def transpose(self, interval, mode):
    self.root_shift_ = tune.root_ + interval
    self.mode_ = mode

  def add_chord(self, index, len=None, tention=None):
    if not len:
      len = self.tune_.def_chd_len_
    if not tention:
      tention = self.tune_.def_tention_

    c = consts.ChordMdConsts.get_diatonic_chord(self.mode_, index, tention)
    self.chords_.append([c, len])

  def play(self, repeat=1):
    for i in range(repeat):
      for c in self.chords_:
        midi_c = consts.ChordMdConsts.get_chord_midi_nums(c[0], self.root_shift_)
        playMidi.PlayMidi.play_chord_midi(midi_c, self.tune_.bpm_, c[1])

