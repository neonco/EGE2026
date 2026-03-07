resol = 4096 * 2160
i = 24
freq = 60

l = 2 * 60
speed = 10_240_000

chanels = 2
dfreq = 48000
depth = 16

vid1 = i * resol * freq * l
sound1 = depth * dfreq * chanels * l

v1 = vid1 + sound1
t1 = v1 / speed
print(v1, vid1, sound1, t1)

vid2 = 12 * resol * 24 * l
sound2 = 8 * 24000 * chanels * l

v2 = vid2 + sound2
t2 = v2 / speed
print(v2, vid2, sound2, t2)

print(t1 - t2)

# 119452

