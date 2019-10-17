from line_bot_api import *


def appointment_event(event):
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/zTbh6K1.jpg',
                    title='選單一',
                    text='我是小火龍',
                    actions=[
                        # data參數可以自定義（這邊定義步驟和服務）
                        PostbackAction(
                            label='服務一',
                            display_text='服務一',
                            data='action=step2&service=服務一'
                        ),
                        PostbackAction(
                            label='服務二',
                            display_text='服務二',
                            data='action=step2&service=服務二'
                        ),
                        PostbackAction(
                            label='服務三',
                            display_text='服務三',
                            data='action=step2&service=服務三'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/w6uEE5d.jpg',
                    title='選單二',
                    text='我是傑尼龜',
                    actions=[
                        # data參數可以自定義（這邊定義步驟和服務）
                        PostbackAction(
                            label='服務一',
                            display_text='服務一',
                            data='action=step2&service=服務一'
                        ),
                        PostbackAction(
                            label='服務二',
                            display_text='服務二',
                            data='action=step2&service=服務二'
                        ),
                        PostbackAction(
                            label='服務三',
                            display_text='服務三',
                            data='action=step2&service=服務三'
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[
            TextSendMessage(text='您想要選什麼服務？'),
            carousel_template_message
        ]
    )
