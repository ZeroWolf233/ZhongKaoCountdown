import sys
import os
import time
import requests
from PyQt5 import QtCore, QtWidgets
from dotenv import load_dotenv


def get_countdown_seconds():
    try:
        load_dotenv()
        url = os.getenv("API")
        response = requests.get(url)
        # 假设API返回的是一个纯文本格式的时间戳（单位：秒）
        timestamp = int(response.text.strip())
        now = int(time.time())
        seconds_left = timestamp - now
        if seconds_left < 0:
            seconds_left = 0
        return seconds_left
    except Exception as e:
        print("获取倒计时失败:", e)
        exit(114514)


class CountdownTimer(QtWidgets.QWidget):
    def __init__(self, countdown_seconds):
        super().__init__()
        # 设置无边框、总在最前、透明背景
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.countdown_seconds = countdown_seconds

        # 使用 QLabel 显示倒计时
        self.label = QtWidgets.QLabel(self)
        self.label.setStyleSheet("font-size: 24px; color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.update_label()

        # 设置窗口大小，并移动到桌面右上角（右上角距离屏幕10px）
        self.resize(200, 100)
        screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
        x = screen_geometry.width() - self.width() - 10
        y = 10
        self.move(x, y)

        # 每秒更新倒计时
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)

    def update_label(self):
        minutes, seconds = divmod(self.countdown_seconds, 60)
        self.label.setText(f"{minutes:02d}:{seconds:02d}")

    def tick(self):
        if self.countdown_seconds > 0:
            self.countdown_seconds -= 1
            self.update_label()
        else:
            self.timer.stop()
            self.label.setText("时间差不多咯~")


if __name__ == "__main__":
    countdown_seconds = get_countdown_seconds()
    app = QtWidgets.QApplication(sys.argv)
    countdown = CountdownTimer(countdown_seconds)
    countdown.show()
    sys.exit(app.exec_())
