######################
#COPYRIGHT OF MEOWNET#
######################

import time


def bar(s):
    print("[----------] ", s*10, " seconds left")
    time.sleep(s)
    print("[#---------] ", s*9, " seconds left")
    time.sleep(s)
    print("[##--------] ", s*8, " seconds left")
    time.sleep(s)
    print("[###-------] ", s*7, " seconds left")
    time.sleep(s)
    print("[####------] ", s*6, " seconds left")
    time.sleep(s)
    print("[#####-----] ", s*5, " seconds left")
    time.sleep(s)
    print("[######----] ", s*4, " seconds left")
    time.sleep(s)
    print("[#######---] ", s*3, " seconds left")
    time.sleep(s)
    print("[########--] ", s*2, " seconds left")
    time.sleep(s)
    print("[#########-] ", s, " seconds left")
    time.sleep(s)
    print("[##########] ", "0 seconds left")
    

        
