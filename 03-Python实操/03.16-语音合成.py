#系统客户端
import time
import win32.com.client

dehua = win32.com.client.Dispatch("SAPI.SPVOICE")


while 1:
        time.sleep(10)
        dehua.speak("sunck is a good man")


































