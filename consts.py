class ChordMdConsts:

  # MIDI NUMBER MID ROOT
  MIDI_C3 = 60

  # Tone Names
  C =   'C'
  C_S = 'C#'
  D_F = 'Db'
  D =   'D'
  D_S = 'D#'
  E_F = 'Eb'
  E =   'E'
  F =   'F'
  F_S = 'F#'
  G_F = 'Gb'
  G =   'G'
  G_S = 'G#'
  A_F = 'Ab'
  A =   'A'
  A_S = 'A#'
  B_F = 'Bb'
  B =   'B'

  # Offsets from Root for each Mode
  IONIAN_SEQ = [0, 2, 4, 5, 7, 9, 11]
  DORIAN_SEQ = [0, 2, 3, 5, 7, 9, 10]
  PHRYGIAN_SEQ = [0, 1, 3, 5, 7, 8, 10]
  LYDIAN_SEQ = [0, 2, 4, 6, 7, 9, 11]
  MIXOLYDIAN_SEQ = [0, 2, 4, 5, 7, 9, 10]
  AEOLIAN_SEQ = [0, 2, 3, 5, 7, 8, 10]
  HARMONIC_MINOR_SEQ = [0, 2, 3, 5, 7, 9, 11]

  # Mode Name
  MODE = ['IONIAN',
          'DORIAN',
          'PHRYGIAN',
          'LYDIAN',
          'MIXOLYDIAN',
          'AEOLIAN',
          'HARMONIC_MINOR']

  # Mode Dictionary
  MODE_SEQS = {
    MODE[0]: IONIAN_SEQ,
    MODE[1]: DORIAN_SEQ,
    MODE[2]: PHRYGIAN_SEQ,
    MODE[3]: LYDIAN_SEQ,
    MODE[4]: MIXOLYDIAN_SEQ,
    MODE[5]: AEOLIAN_SEQ,
    MODE[6]: HARMONIC_MINOR_SEQ
  }

  @staticmethod
  def get_diatonic_chord(mode, root_step, tension) -> [int]:
    """Get Basic Chord Tone Distances from its Mode's root."""
    chord = []
    mode_idx = ChordMdConsts.MODE.index(mode)
    mode_name = ChordMdConsts.MODE[mode_idx]
    mode_seq = ChordMdConsts.MODE_SEQS[mode_name]
    __tone_num = min(5, 3 + tension)

    for i in range(__tone_num):
      scalepos = (i * 2) % len(mode_seq)
      tonepos = mode_seq[scalepos]
      if (i * 2) >= len(mode_seq):
        tonepos += 12
      chord.append(tonepos)
    return chord

  @staticmethod
  def get_chord_midi_nums(chord_intervals, root) -> [int]:
    """Convert intervals to MIDI key numbers array."""
    midi_nums = []
    midi_root = ChordMdConsts.MIDI_C3 + root # [TODO]
    for i in chord_intervals:
      scalepos = (i * 2) % 7   # [TODO] Magic Number
      if (i * 2) >= 7:
        scalepos += 12
      midi_nums.append(midi_root + scalepos)
      
    return midi_nums

