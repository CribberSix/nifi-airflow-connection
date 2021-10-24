from time import time

def pause(secs):
    init_time = time()
    while time() < init_time+secs: pass
