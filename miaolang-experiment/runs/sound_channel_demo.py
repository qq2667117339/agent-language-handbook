# -*- coding: utf-8 -*-
"""MiaoLang 声音通道演示 — FSK 调制/解调（ggwave 原理的纯 Python 最小实现）
文本 → 字节 → 比特流 → 音调序列(1=1200Hz, 0=800Hz) → wav → 解码 → 文本还原
手册第6章方向的最小可行验证。"""
import wave, struct, io, sys

SAMPLE_RATE = 44100
BIT_MS = 10                     # 每比特 10ms
F1, F0 = 1200, 800              # bit1 / bit0 频率
msg = "[LIST:@LAB\\runs|mch=*.md]=>[FIND|whr=FAIL]=>[CNT]=>[SUMM|len=2]=>[Ω]"

def bits_of(data: bytes):
    for b in data:
        for i in range(7, -1, -1):
            yield (b >> i) & 1

def tone(freq, ms):
    n = int(SAMPLE_RATE * ms / 1000)
    import math
    return [int(12000 * math.sin(2 * math.pi * freq * i / SAMPLE_RATE)) for i in range(n)]

def encode(text: str) -> bytes:
    data = text.encode("utf-8")
    samples = tone(F1, 40) + tone(F0, 40)          # 前导码
    for bit in bits_of(data):
        samples += tone(F1 if bit else F0, BIT_MS)
    samples += tone(F1, 40) + tone(F0, 40)          # 结束码
    buf = io.BytesIO()
    w = wave.open(buf, "wb")
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SAMPLE_RATE)
    w.writeframes(struct.pack(f"<{len(samples)}h", *samples))
    w.close()
    return buf.getvalue()

def decode(wav_bytes: bytes) -> str:
    w = wave.open(io.BytesIO(wav_bytes), "rb")
    frames = struct.unpack(f"<{w.getnframes()}h", w.readframes(w.getnframes()))
    w.close()
    chunk = int(SAMPLE_RATE * BIT_MS / 1000)
    def freq_of(seg):
        zero_cross = sum(1 for i in range(1, len(seg)) if seg[i-1] < 0 <= seg[i])
        dur = len(seg) / SAMPLE_RATE
        return zero_cross / dur if dur > 0 else 0   # 上穿过零每周期1次，不除2
    total_blocks = len(frames) // chunk
    preamble_blocks = (40 + 40) // BIT_MS   # 前导码 40ms F1 + 40ms F0 = 8 块
    tail_blocks = preamble_blocks            # 结束码同长
    data_blocks = total_blocks - preamble_blocks - tail_blocks
    bits = []
    for b in range(preamble_blocks, preamble_blocks + data_blocks):
        f = freq_of(frames[b*chunk:(b+1)*chunk])
        bits.append(1 if f > 1000 else 0)
    out = bytearray()
    for i in range(0, len(bits) - 7, 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | bits[i+j]
        out.append(byte)
    return out.decode("utf-8", errors="replace")

wav = encode(msg)
decoded = decode(wav)
match = decoded == msg
print(f"原文长度: {len(msg)} chars -> wav {len(wav)} bytes")
print(f"解码还原: {'== 完全一致 ==' if match else 'MISMATCH!'}")
if not match:
    print("原文:", msg); print("还原:", decoded)
print("SOUND_CHANNEL_PASS=" + ("YES" if match else "NO"))
