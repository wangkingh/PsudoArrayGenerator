from collections import OrderedDict


class SacHeader(object):
    def __init__(self):
        self.header = OrderedDict({
            "delta": -12345.0, "depmin": -12345.0, "depmax": -12345.0, "scale": 1, "odelta": -12345.0,

            "b": -12345.0, "e": -12345.0, "o": -12345.0, "a": -12345.0, "internal1": -12345.0,

            "t0": -12345.0, "t1": -12345.0, "t2": -12345.0, "t3": -12345.0, "t4": -12345.0,

            "t5": -12345.0, "t6": -12345.0, "t7": -12345.0, "t8": -12345.0, "t9": -12345.0,

            "f": -12345.0, "resp0": -12345.0, "resp1": -12345.0, "resp2": -12345.0, "resp3": -12345.0,

            "resp4": -12345.0, "resp5": -12345.0, "resp6": -12345.0, "resp7": -12345.0, "resp8": -12345.0,

            "resp9": -12345.0, "stla": -12345.0, "stlo": -12345.0, "stel": -12345.0, "stdp": -12345.0,

            "evla": -12345.0, "evlo": -12345.0, "evel": -12345.0, "evdp": -12345.0, "mag": -12345.0,

            "user0": -12345.0, "user1": -12345.0, "user2": -12345.0, "user3": -12345.0, "user4": -12345.0,

            "user5": -12345.0, "user6": -12345.0, "user7": -12345.0, "user8": -12345.0, "user9": -12345.0,

            "dist": -12345.0, "az": -12345.0, "baz": -12345.0, "gcarc": -12345.0, "internal2": -12345.0,

            "internal3": -12345.0, "depmen": -12345.0, "cmpaz": -12345.0, "cmpinc": -12345.0, "xminimum": -12345.0,

            "xmaximum": -12345.0, "yminimum": -12345.0, "ymaximum": -12345.0, "unused1": -12345.0, "unused2": -12345.0,

            "unused3": -12345.0, "unused4": -12345.0, "unused5": -12345.0, "unused6": -12345.0, "unused7": -12345.0,

            "nzyear": -12345, "nzjday": -12345, "nzhour": -12345, "nzmin": -12345, "nzsec": -12345,

            "nzmsec": -12345, "nvhdr": -12345, "norid": -12345, "nevid": -12345, "npts": -12345,

            "internal4": -12345, "nwfid": 0, "nxsize": 0, "nysize": 0, "unused8": 0,

            "iftype": 1, "idep": -12345, "iztype": 1, "unused9": 0, "iinst": 0,

            "istreg": 0, "ievreg": 0, "ievtyp": 0, "iqual": 1, "isynth": 1,

            "imagtyp": 0, "imagsrc": 0, "unused10": 0, "unused11": 0, "unused12": 0,

            "unused13": 0, "unused14": 0, "unused15": 0, "unused16": 0, "unused17": 0,

            "leven": 1, "lpspol": 0, "lovrok": 0, "lcalda": 0, "unused18": 0,

            "kstnm": ' ' * 8, "kevnm": ' ' * 16,

            "khole": ' ' * 8, "ko": ' ' * 8, "ka": ' ' * 8,

            "kt0": ' ' * 8, "kt1": ' ' * 8, "kt2": ' ' * 8,

            "kt3": ' ' * 8, "kt4": ' ' * 8, "kt5": ' ' * 8,

            "kt6": ' ' * 8, "kt7": ' ' * 8, "kt8": ' ' * 8,

            "kt9": ' ' * 8, "kf": ' ' * 8, "kuser0": ' ' * 8,

            "kuser1": ' ' * 8, "kuser2": ' ' * 8, "kcmpnm": ' ' * 8,

            "knetwk": ' ' * 8, "kdatrd": ' ' * 8, "kinst": ' ' * 8
        })
