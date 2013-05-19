#! /usr/bin/env python
#coding=utf-8
import threading
import time

class BitCoin(threading.Thread):
    
    def __init__(self, id, rpc):
        threading.Thread.__init__(self)
        self.id = id
        self.rpc = rpc
        
        
    def run(self):
        work = self.rpc.getWork()
        if work is None:
            time.sleep(1)
        print self.id
        pass
    
    def calc(self):
        pass
    
class LiteCoin(threading.Thread):
    
    def __init__(self):
        self.rpc = None
        
    def run(self):
        pass
