import socket 

import datetime
import time


def log_user(id=None):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    warning = f'Someone may be using a scanner to access unwanted areas.\nInput received: {id}\nIncident time: {st}\n\n'
    with open ('cybergoat/log/access.txt', 'a+') as f:
        f.write(warning)
    f.close()
    return(warning)

