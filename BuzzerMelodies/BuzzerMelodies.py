from machine import Pin,PWM
import time

tempo=2
tones={
    'c':262,
    'd':294,
    'e':330,
    'f':349,
    'g':392,
    'a':440,
    'b':494,
    'C':523,
    ' ':0,
}

beep=PWM(Pin(4),freq=440,duty=512)
melody = 'cdefgabC'
rhythm=[8,8,8,8,8,8,8,8]
while True:
    for tone, length in zip(melody,rhythm):
        beep.freq(tones[tone])
        time.sleep(tempo/length)
