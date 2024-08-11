import machine, time
p=machine.Pin(2, machine.Pin.OUT)
while 1:
    p.on()
    time.sleep_ms(500)
    p.off()
    time.sleep_ms(500)
