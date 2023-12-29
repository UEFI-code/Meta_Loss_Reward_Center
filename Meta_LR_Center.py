import myGPT_Drv
import json

class Meta_Loss_Reward_Center:
    def __init__(self, apiKey, endpoint, rules = '幸せ！', name='幸せの中枢'):
        self.name = name
        self.gpt = myGPT_Drv.chat_Drv(apiKey=apiKey, endpoint=endpoint)
        self.introdution = f"You are working inside a brain at reward & loss center."
        self.rules = rules
        self.outputFormat = """{"loss": 0 - 1 float value, "reward": 0 - 1 float value, "reason": "..."}"""

    def forward(self, x):
        context = f"{self.introdution}\n" + f"Rules: {self.rules}\n" + f"Event: {x}\n" + f"Output Format: {self.outputFormat}\n"
        response = self.gpt.forward(context)
        return json.loads(response)
    
if __name__ == '__main__':
    jsonparam = json.load(open('gpt3_5token.key', 'r'))
    loss_reward = Meta_Loss_Reward_Center(apiKey=jsonparam['key'], endpoint=jsonparam['endpoint'], rules='幸せ！')
    res = loss_reward.forward('I earned 1 dollars, but I totally have 1 million dollars.')
    print(res)