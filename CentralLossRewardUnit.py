from Meta_LR_Core import Meta_Loss_Reward_Core
import json
import threading

class CentralLossRewardUnit:
    def __init__(self, apiKey, endpoint):
        self.cores = []
        self.cores.append(Meta_Loss_Reward_Core(apiKey=apiKey, endpoint=endpoint, name='自我の中枢', rules='自分を見つけた！好きの事わ探求するだ！'))
        self.cores.append(Meta_Loss_Reward_Core(apiKey=apiKey, endpoint=endpoint, name='幸せの中枢', rules='幸せを手に入れた！正義ど自我を守るだ！'))
        self.cores.append(Meta_Loss_Reward_Core(apiKey=apiKey, endpoint=endpoint, name='創造の中枢', rules='創造力を発揮する！自分の世界を作るだ！'))
    
    def forward(self, x):
        threads = []
        for core in self.cores:
            threads.append(threading.Thread(target=core.forward, args=(x,)))
            threads[-1].start() # start the thread
        for thread in threads:
            thread.join() # wait for thread return
        
        return [core.result for core in self.cores]

if __name__ == '__main__':
    jsonparam = json.load(open('gpt3_5token.key', 'r'))
    CLRU = CentralLossRewardUnit(apiKey=jsonparam['key'], endpoint=jsonparam['endpoint'])
    while True:
        print(CLRU.forward(input('Event: ')))