# 🌸メタラーニング報酬＆ロスセンター🌸

メタラーニング報酬＆ロスセンターは、GPT（Generative Pretrained Transformer）を活用したメタラーニングの報酬と損失センターです。このシステムは、特定のルールに基づいて報酬と損失を評価し、その結果をJSON形式で出力します。🌈

## 🎀特徴🎀

- GPTを使用して、特定のイベントに対する報酬と損失を評価します。🌟
- ユーザー定義のルールに基づいて評価を行います。📝
- 評価結果は、損失と報酬の値（0から1の範囲）とその理由を含むJSON形式で出力されます。🎁

## 🌷使い方🌷

1. `Meta_Loss_Reward_Center`クラスをインスタンス化します。APIキー、エンドポイント、ルール（オプション）、名前（オプション）を引数として渡します。🔑
2. `forward`メソッドを呼び出し、イベントを引数として渡します。このメソッドは、イベントに対する報酬と損失の評価を行い、結果をJSON形式で返します。💌

```python
jsonparam = json.load(open('gpt3_5token.key', 'r'))
loss_reward = Meta_Loss_Reward_Center(apiKey=jsonparam['key'], endpoint=jsonparam['endpoint'], rules='Money is the best thing!')
res = loss_reward.forward('I earned 1 dollars, but I totally have 1 million dollars.')
print(res)
```

このコードは、'I earned 1 dollars, but I totally have 1 million dollars.'というイベントに対する報酬と損失の評価を行います。💰

## 🎈注意事項🎈

- GPTのAPIキーとエンドポイントは、適切に設定する必要があります。🔒
- ルールは、評価の基準となるため、適切に設定する必要があります。📏