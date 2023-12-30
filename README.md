# 🌸メタラーニング報酬＆ロスセンター🌸

メタラーニング報酬＆ロスセンターは、GPT（Generative Pretrained Transformer）を活用したメタラーニングの報酬と損失センターです。このシステムは、特定のルールに基づいて報酬と損失を評価し、その結果をJSON形式で出力します。🌈

## 🎀特徴🎀

- GPTを使用して、特定のイベントに対する報酬と損失を評価します。🌟
- ユーザー定義のルールに基づいて評価を行います。📝
- 評価結果は、損失と報酬の値（0から1の範囲）とその理由を含むJSON形式で出力されます。🎁

## 🌷使い方🌷

1. `Meta_Loss_Reward_Core`クラスをインスタンス化します。APIキー、エンドポイント、ルール（オプション）、名前（オプション）を引数として渡します。🔑
2. `forward`メソッドを呼び出し、イベントを引数として渡します。このメソッドは、イベントに対する報酬と損失の評価を行い、結果をJSON形式で返します。💌

```python
jsonparam = json.load(open('gpt3_5token.key', 'r'))
loss_reward = Meta_Loss_Reward_Center(apiKey=jsonparam['key'], endpoint=jsonparam['endpoint'])
while True:
    print(loss_reward.forward(input('Event: ')))
print(res)
```

このコードは、'I earned 1 dollars, but I totally have 1 million dollars.'というイベントに対する報酬と損失の評価を行います。💰

# 🌸中央損失報酬ユニット🌸

中央損失報酬ユニットは、複数の`Meta_Loss_Reward_Core`インスタンスを管理し、それぞれに異なるルールを適用することができます。これにより、複数の視点からイベントの報酬と損失を評価することが可能になります。

## 🎀特徴🎀

- 複数の`Meta_Loss_Reward_Core`インスタンスを管理します。🌟
- 各インスタンスは異なるルールに基づいて評価を行います。📝
- 各インスタンスの評価結果は、損失と報酬の値（0から1の範囲）とその理由を含むJSON形式で出力されます。🎁

## 🌷使い方🌷

1. `CentralLossRewardUnit`クラスをインスタンス化します。APIキー、エンドポイントを引数として渡します。🔑
2. `forward`メソッドを呼び出し、イベントを引数として渡します。このメソッドは、各`Meta_Loss_Reward_Core`インスタンスに対してイベントを評価し、結果をJSON形式で返します。💌

```python
jsonparam = json.load(open('gpt3_5token.key', 'r'))
clru = CentralLossRewardUnit(apiKey=jsonparam['key'], endpoint=jsonparam['endpoint'])
while True:
    print(clru.forward(input('Event: ')))
```

このコードは、ユーザーからの入力に対する報酬と損失の評価を行います。💰

# 🎈注意事項🎈

- GPTのAPIキーとエンドポイントは、適切に設定する必要があります。🔒
- 各`Meta_Loss_Reward_Core`インスタンスのルールは、評価の基準となるため、適切に設定する必要があります。📏