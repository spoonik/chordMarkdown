import consts

class Tune:
  def __init__(self,
               root=consts.ChordMdConsts.C,
               mode=consts.ChordMdConsts.MODE[0],
               time=4,
               bpm=88,
               def_tention=0,
               def_chd_len=None):
    self.root_ = root
    self.mode_ = mode
    self.time_ = time
    self.bpm_ = bpm
    self.def_tention_ = def_tention
    self.def_chd_len_ = def_chd_len if def_chd_len else time

