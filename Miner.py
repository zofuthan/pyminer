#! /usr/bin/env python
#coding=utf-8
from Configure import Configure
from coin import BitCoin
from rpc import GetWork

class Miner:
    
    def __init__(self, cfg):
        self.cfg = cfg
        
    def mining(self):
        rpc = GetWork(1, 1)
        for i in range(3):
            coin = BitCoin(i, rpc)
            coin.start()
    
if __name__ == '__main__':
    cfg = Configure().configure()
    minerd = Miner(cfg)
    minerd.mining()