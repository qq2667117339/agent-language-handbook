# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r".\runs")
from sound_channel_demo import encode, msg
wav = encode(msg)
with open(r".\runs\miaolang_sound_demo.wav", "wb") as f:
    f.write(wav)
print(f"saved: {len(wav)} bytes, message: {msg}")
