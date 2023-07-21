from typing import Dict
from sac_header import SacHeader
from datetime import datetime


def generate_header(kstnm: str, start_time: datetime, channel: str, coordinate: Dict[str, float],
                    sample_rate: float, seg_length: float):
    # Initialize the header
    header = SacHeader().header

    # Write the header defined from inputs
    header['kstnm'] = kstnm.ljust(8)
    header['kcmpnm'] = str(channel).ljust(8)
    header['stla'] = coordinate['stla']
    header['stlo'] = coordinate['stlo']
    header['stel'] = coordinate['stel']
    header['delta'] = 1 / sample_rate
    header['npts'] = int(sample_rate * seg_length)

    # Write time header info
    header['nzyear'] = start_time.year
    header['nzjday'] = start_time.timetuple().tm_yday
    header['nzhour'] = start_time.hour
    header['nzmin'] = start_time.minute
    header['nzsec'] = start_time.second
    header['b'] = 0

    # Write necessary header info
    header['iftype'] = 1
    header['leven'] = 1
    header['lovrok'] = True
    header['iftype'] = 1
    header['isynth'] = 1
    header['nwfid'] = 5
    header['nvhdr'] = 6

    return header
