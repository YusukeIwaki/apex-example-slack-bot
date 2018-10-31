# [apex](https://github.com/apex/apex)-based slack bot example.

## カスタマイズ方法

functions/exp/exp_router.py に、メッセージのハンドリングするロジックがあります。

```
@router.Route("^(おはよう)$")
def handle_good_morning(event):
  slack.reply(event["channel"], event["ts"], "おはようございます！")
  #
  # ここに、Slackレスポンス、などの各種処理をかく
  #
```

のようなテンプレートでいろいろ書いていきます。

### Slack通知

超簡易的なSlackクライアント(functions/exp/slack_message.py)を内部で持っています。

単純に、メッセージを投稿したい場合は

```
slack.post(event["channel"], "こんにちは")
```

スレッドレスポンスとしてメッセージを投稿したい場合は

```
slack.post(event["channel"], event["ts"], "スレッドレスポンスでこんにちは")
```


## テスト

```
cd functions/exp/
python -m unittest discover
```

※ Python 3.6以上じゃないと多分うごかない


## デプロイ

apexをインストールして、

```
apex deploy \
  --set SLACK_API_TOKEN=xoxb-xxxxxxxxxx-xxxxxxxx-xxxxxxxxx \
  --set SLACK_APP_VERIFICATION_TOKEN=xxxxxxxxxxxx
```