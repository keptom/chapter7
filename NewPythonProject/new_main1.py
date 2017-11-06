import threading
import time
from itertools import islice
def f():
    with open("E-Mail-Liste.txt", "r") as myfile:
       
       head = list(islice(myfile, 3))

# always remember, use files in a with statement
    with open("output.txt", "a+") as f2:
        
        for item in head:
            
            f2.write(item)
            
    print("hello worl")
    with open('E-Mail-Liste.txt', 'r') as fin:        
        
        data = fin.read().splitlines(True)
    with open('E-Mail-Liste.txt', 'w') as fout:
                
                fout.writelines(data[3:])
    threading.Timer(3, f).start()
    
if __name__ == '__main__':
    f()    
    time.sleep(20)