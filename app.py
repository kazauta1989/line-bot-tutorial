# import 所需套件
from flask import Flask, request, abort
# import
from urllib.parse import parse_qsl

import os

# 從 events.about_us import about_us_event 到 app.py
# 從 line_bot_api import 全部到 app.py
# 後面一樣

from line_bot_api import *
from events.about_us import about_us_event
from events.location import location_event
from events.contact import contact_event
from events.appointment import appointment_event, appointment_datetime_event, appointment_completed_event
from events.quick_reply import quick_reply_event
from database import db_session, init_db

app = Flask(__name__)


# 在第一次接觸到請求之後，就會初始資料庫
@app.before_first_request
def init():
    init_db()


# 這個function可以讓我們在flask每一次request結束之後，或是server關閉之後，能夠正確的關閉database的連結
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# 監聽所有來自 /callback 的 Post Request
# /callback路徑，到時候line所傳送的資料到WebhookUrl就會視為從這裡進來的
# 所以他會取得signature 和 body
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    # 接著把signature 和 body 丟給handler去做處理
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 當handler接受到訊息之後，他會呼叫handle_message這個函式
# 並把event這個物件給丟進來
# 這event物件裡面包含token ： 是哪一個使用者傳送的訊息，以及傳送什麼訊息，都會在event物件裡面

# 透過line_bot_api去回傳event物件裡面的token以及文字訊息
# 擷取event的message.text訊息回傳給使用者
# 簡單說 handle_message(event)這個函式，做的就是使用者傳hi，機器人就回傳一樣的字
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 當接收到訊息的時候，會先將訊息變換成小寫
    message_text = str(event.message.text).lower()
    # 當message_text等同於'＠關於我們'時，會回傳line_bot_api.reply_message(）裡的值
    # 另外，當有用到TextSendMessage、ImageSendMessage、VideoSendMessage、等等...
    # 多個Message objects時，要記得用成陣列，才會一次訊息同時送出
    if message_text == '關於我們':
        about_us_event(event)
    elif message_text == '地址':
        location_event(event)
    elif message_text == '聯絡我們':
        contact_event(event)
    elif message_text == '立即預訂':
        appointment_event(event)
    elif message_text == 'test':
        quick_reply_event(event)


# 前面的@handler.add主要是處理MessageEvent，接收純文字訊息
# 那現在預約功能會需要接收使用者所選的服務項目，所以需要用另外一個@handler，用postback這個@handler，
# 因為我們在appointment.py裡是使用PostbackAction，我們要取得其裡面的data
@handler.add(PostbackEvent)
def handler_postback(event):
    # 我們需要把拿到的data字串轉換成字典，那我們會使用urllib裡的prase_qsl
    # prase_qsl可以解析一個query字串把它轉換成一個list
    # 那list如果要轉換成字典，在前面加上dict即可
    # 有了字典就可以針對action和server去取得資料（action和server是自定義宣告的，可以做更換）
    data = dict(parse_qsl(event.postback.data))
    action_data = data.get('action')
    service_data = data.get('service')

    # 接著就是做判斷，判斷我們的action等於什麼，然後做什麼事
    # 那我們這邊判斷如果等於step2，我們就做預約的動作
    if action_data == 'step2':
        appointment_datetime_event(event)
    elif action_data == 'step3':
        appointment_completed_event(event)
    elif action_data == 'step4':
        appointment_datetime_event(event)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
