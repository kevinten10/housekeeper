from wxpy import *


class WeChat(object):
    bot: Bot

    def __init__(self):
        pass

    def login(self):
        self.bot = Bot()
        return self.bot

    def test_send(self):
        self.bot.file_helper.send("hello")


if __name__ == '__main__':
    wechat = WeChat()
    wechat.login()
    wechat.test_send()
