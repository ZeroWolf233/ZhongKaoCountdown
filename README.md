# 中考倒计时

> [!WARNING]
> 本作大部分代码为`ChatGPT-o3-mini`所作，非常的构式就是了，不是很推荐使用

想到我只剩100天就要中考了，刚好今天晚上作业写完了无聊，打开 `ChatGPT` 写出了这段代码，稍加修改后就直接投入了qwq

## 开箱即食(推荐)
1. 从[Release](https://github.com/ZeroWolf233/ZhongKaoCountdown/releases)下载最新版
2. 创建`.env`，编辑`API=<您的api>`，API返回值应为倒计时结束的时间戳

## 自己编译
```bash
git clone https://github.com/ZeroWolf233/ZhongKaoCountdown
cd ZhongKaoCountdown
pyinstaller -F -w -i favicon.ico main.py
```

## 鸣谢
- [つきみむみ](https://www.pixiv.net/users/17674896) 图表来源 Pid: [128032053](https://www.pixiv.net/artworks/128032053)