# Generate a synthetic noise trace
import os

from header_generator import generate_header
from signal_generator import generate_random, generate_from_spectrum
from datetime import datetime
from typing import Dict
import struct


class Trace:
    def __init__(self, kstnm: str, start_time: datetime, channel: str, coordinate: Dict[str, float], sample_rate,
                 seg_length: float, sac_path: str):
        self.kstnm = kstnm
        self.start_time = start_time
        self.channel = channel
        self.coordinate = coordinate
        self.sample_rate = sample_rate
        self.seg_length = seg_length
        self.sac_path = sac_path

    def gen(self, spectrum=None):
        header = generate_header(self.kstnm, self.start_time, self.channel, self.coordinate, self.sample_rate,
                                 self.seg_length)
        if spectrum is None:
            data = generate_random(int(self.sample_rate * self.seg_length))
        else:
            data = generate_from_spectrum(spectrum, int(self.sample_rate * self.seg_length))

        # Writing in to sac file
        sac_dir = os.path.dirname(self.sac_path)
        os.makedirs(sac_dir, exist_ok=True)

        with open(self.sac_path, 'wb') as f:
            for key, value in header.items():
                if isinstance(value, int):
                    f.write(struct.pack('>i', value))  # Write integer
                elif isinstance(value, float):
                    f.write(struct.pack('>f', value))  # Write float
                elif isinstance(value, str):
                    f.write(value.encode())  # Write string
                else:
                    raise ValueError(f'Unsupported data type: {type(value)} for key: {key}')
            data.tofile(f)
