import myGPT_Drv
import json
import time

class Meta_Loss_Reward_Center:
    def __init__(self, apiKey, endpoint, rules = '幸せ！', name='幸せの中枢', maxTry=5):
        self.name = name
        self.gpt = myGPT_Drv.chat_Drv(apiKey=apiKey, endpoint=endpoint)
        self.introdution = f"You are working inside a brain at reward & loss center."
        self.rules = rules
        self.outputFormat = """{"loss": 0 - 1 float value, "reward": 0 - 1 float value, "reason": "..."}"""
        self.maxTry = maxTry

    def forward(self, x):
        context = f"{self.introdution}\n" + f"Rules: {self.rules}\n" + f"Event: {x}\n" + f"Output Format: {self.outputFormat}, Do not output extar text!\n"
        for _ in range(self.maxTry):
            try:
                response = self.gpt.forward(context)
                return json.loads(response)
            except Exception as e:
                print(f'Bad luck: GPT response error {e}, retrying...')
                time.sleep(5)
        return {'loss': 0, 'reward': 0, 'reason': 'No feeling.'}
    
if __name__ == '__main__':
    jsonparam = json.load(open('gpt3_5token.key', 'r'))
    loss_reward = Meta_Loss_Reward_Center(apiKey=jsonparam['key'], endpoint=jsonparam['endpoint'])
    while True:
        print(loss_reward.forward(input('Event: ')))