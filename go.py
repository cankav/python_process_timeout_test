import time
from multiprocessing import Process

# test join without timeout

def x(t):
    print('x start')
    time.sleep(t)
    print('x done')

def y():
    print('\ny start')
    p=Process(target=x, args=(5,))
    p.start()
    print('y joins')
    p.join()
    print('p exitcode %s' %p.exitcode)
    print('y ends')

y()

def z():
    print('\nz start')
    p=Process(target=x, args=(5,), daemon=True)
    p.start()
    print('z joins')
    p.join(2)
    print('p exitcode %s' %p.exitcode)
    print('z ends')

z()
print('done')
