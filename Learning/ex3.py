import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, msg):
       super().append(msg)
       self.log(msg)
    
loggable_list = LoggableList()
loggable_list.append(1)  
loggable_list.append('test')  