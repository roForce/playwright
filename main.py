from datetime import time
from datetime import datetime
import  time

now = datetime.now() # current date and time
localtime = time.strftime("%F,%H:%M:%S",time.localtime())
print(localtime)