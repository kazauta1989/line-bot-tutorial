# Line Bot 

本教程介紹如何使用 Python LINE Bot SDK 在 Heroku 上架設一個機器人。
<!--more-->
如果您想以另一種語言架設範例 bot，請參閱以下  LINE Bot SDK repositories。
- [PHP](https://github.com/line/line-bot-sdk-php)
- [Go](https://github.com/line/line-bot-sdk-go)
- [Perl](https://github.com/line/line-bot-sdk-perl)
- [Ruby](https://github.com/line/line-bot-sdk-ruby)
- [Python](https://github.com/line/line-bot-sdk-python)
- [Node.js](https://github.com/line/line-bot-sdk-nodejs)

## 進階操作
[官方文件](https://github.com/line/line-bot-sdk-python#api)
### 回覆訊息
只有當有訊息傳來，才能回覆訊息
```python
line_bot_api.reply_message(reply_token, 訊息物件)
```
### 主動傳送訊息
Bot 需要有開啟 push 功能才可以做，否則程式會出錯
```python
line_bot_api.push_message(push_token, 訊息物件)
```

## 訊息物件分類

[官方文件](https://developers.line.me/en/docs/messaging-api/message-types/)

修改範例程式碼中， handle_message() 方法內的程式碼，可實現多種功能

### TextSendMessage （文字訊息）
![](https://i.imgur.com/LieCFAb.png =250x)
```python
message = TextSendMessage(text='Hello, world')
line_bot_api.reply_message(event.reply_token, message)
```

### ImageSendMessage（圖片訊息）
![](https://i.imgur.com/RaH7gqo.png =250x)
```python
message = ImageSendMessage(
    original_content_url='https://example.com/original.jpg',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```

### VideoSendMessage（影片訊息）
![](https://i.imgur.com/o6cvf3o.png =250x)
```python
message = VideoSendMessage(
    original_content_url='https://example.com/original.mp4',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```

### AudioSendMessage（音訊訊息）
![](https://i.imgur.com/w5szZag.png =250x)
```python
message = AudioSendMessage(
    original_content_url='https://example.com/original.m4a',
    duration=240000
)
line_bot_api.reply_message(event.reply_token, message)
```

### LocationSendMessage（位置訊息）
![](https://i.imgur.com/tXE7Aus.png =250x)
```python
message = LocationSendMessage(
    title='my location',
    address='Tokyo',
    latitude=35.65910807942215,
    longitude=139.70372892916203
)
line_bot_api.reply_message(event.reply_token, message)
```

### StickerSendMessage（貼圖訊息）
![](https://i.imgur.com/7x0mgK1.png =250x)
```python
message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
)
line_bot_api.reply_message(event.reply_token, message)
```

### ImagemapSendMessage （組圖訊息）
![](https://i.imgur.com/MoSf2D6.png =250x)
```python
message = ImagemapSendMessage(
    base_url='https://example.com/base',
    alt_text='this is an imagemap',
    base_size=BaseSize(height=1040, width=1040),
    actions=[
        URIImagemapAction(
            link_uri='https://example.com/',
            area=ImagemapArea(
                x=0, y=0, width=520, height=1040
            )
        ),
        MessageImagemapAction(
            text='hello',
            area=ImagemapArea(
                x=520, y=0, width=520, height=1040
            )
        )
    ]
)
line_bot_api.reply_message(event.reply_token, message)
```

### TemplateSendMessage - ButtonsTemplate （按鈕介面訊息）
![](https://i.imgur.com/41lXWjP.png =250x)
```python
message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://example.com/image.jpg',
        title='Menu',
        text='Please select',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            ),
            URITemplateAction(
                label='uri',
                uri='http://example.com/'
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

### TemplateSendMessage - ConfirmTemplate（確認介面訊息）
![](https://i.imgur.com/U8NDhrt.png =250x)
```python
message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='Are you sure?',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

### TemplateSendMessage - CarouselTemplate
![](https://i.imgur.com/982Glgo.png =250x)
```python
message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://example.com/item1.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackTemplateAction(
                        label='postback1',
                        text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message1',
                        text='message text1'
                    ),
                    URITemplateAction(
                        label='uri1',
                        uri='http://example.com/1'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://example.com/item2.jpg',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='uri2',
                        uri='http://example.com/2'
                    )
                ]
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

### TemplateSendMessage - ImageCarouselTemplate
![](https://i.imgur.com/2ys1qqc.png =250x)
```python
message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='postback1',
                    text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item2.jpg',
                action=PostbackTemplateAction(
                    label='postback2',
                    text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```
