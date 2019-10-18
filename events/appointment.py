from line_bot_api import *

# import parse_qsl
from urllib.parse import parse_qsl
# import datetime
import datetime


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


# 那這邊會採用ImageCarouselTemplate，讓使用者點選圖片接著進行預約時間的動作
# 這邊要把按鈕改成DatetimePicker
# 那DatetimePicker 的 action 是在 tests/api/test_send_template_message.py裡面
# (line-bot-sdk-python 文件)
def appointment_datetime_event(event):
    # prase_qsl，data字串轉換成字典，並解析 action_data 和 service_data
    data = dict(parse_qsl(event.postback.data))
    action_data = data.get('action')
    service_data = data.get('service')

    # 因為會有初始時間，所以會需要取得現在時間
    # 這時後就要用到datetime 裡面的 dateime.now()
    # 定義現在時間
    now = datetime.datetime.now()
    # 最快只能預約2天後，現在時間再加上2天，然後最遠可以選的區間範圍（9-2）=7天 <---（選填）
    min_date = now + datetime.timedelta(days=2)
    max_date = now + datetime.timedelta(days=9)

    image_carousel_template_message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/0uII70Z.jpg',
                    action=DatetimePickerAction(
                        label="選擇日期時間",
                        # 那這邊的action一樣可以自定義，那當然也是需要把拿到的data字串轉換成字典（app.py有說明）
                        data="action=step3&service={}".format(service_data),
                        # mode有三種，date、time、datetime
                        mode="datetime",
                        # 初始時間、最小時間、最大時間<---3個都是選填
                        # 下面網址是 strftime 文件
                        # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
                        # 初始時間
                        initial=min_date.strftime('%Y-%m-%dT00:00'),
                        # 最小時間
                        min=min_date.strftime('%Y-%m-%dT00:00'),
                        # 最大時間
                        max=max_date.strftime('%Y-%m-%dT23:59')
                    )
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[
            image_carousel_template_message
        ]
    )
