import consts
import tune
from section import Section

def main():
  t = tune.Tune(root=consts.ChordMdConsts.C,
              mode=consts.ChordMdConsts.MODE[0],
              time=4,
              bpm=88,
              def_chd_len=4,
              def_tention=1)

  # Section A (A-melo)
  a = Section(t)
  a.add_chord(0)
  a.add_chord(1, len=2, tention=2)
  a.add_chord(4, len=2, tention=2)
  a.play(repeat=4)

  # Section B (B-melo)
  b = Section(t)
  b.transpose(interval=0, mode=MODE[6])
  a.add_chord(0)
  a.add_chord(1, len=2, tention=2)
  a.add_chord(4, len=2, tention=2)
  a.play(repeat=2)

  # Section C (C-melo = sabi)
  c = Section(t)
  c.transpose(interval=4, mode=MODE[5])
  c.add_chord(4, len=8)
  c.add_chord(0, len=8, tention=2)
  c.add_chord(1, len=8, tention=2)
  c.transpose(mode=MODE[0])
  c.add_chord(1, len=4, tention=2)
  c.add_chord(1, len=5, tention=2)
  c.play(repeat=2)


if __name__ == "__main__":
  main()
