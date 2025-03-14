# 中考倒计时

> [!WARNING]
> 本作大部分代码为`ChatGPT-o3-mini`所作，非常的构式就是了，不是很推荐使用

> [!TIP]
> 建议在希沃的4K环境下使用，后期可能会加入更多的自定义以适配不同场景

想到我只剩100天就要中考了，刚好今天晚上作业写完了无聊，打开 `ChatGPT` 写出了这段代码，稍加修改后就直接投入了qwq

## 开箱即食(推荐)
1. 从[Release](https://github.com/ZeroWolf233/ZhongKaoCountdown/releases)下载最新版
2. 创建`.env`，编辑`TIME=<结束倒计时的时间戳>`
3. 运行

## 自己编译
```bash
git clone https://github.com/ZeroWolf233/ZhongKaoCountdown
cd ZhongKaoCountdown
pip install -r requirements.txt
pyinstaller -F -w -i favicon.ico main.py
```

## 环境变量
| 环境变量   | 必填 | 默认值                             | 说明                           |
|--------|------|---------------------------------|------------------------------|
| TIME   | 是 | https://hk2.l0.ink/api/zhongkao | 倒计时结束的时间，格式应为时间戳，可以用api提供时间戳 |
| LABLE  | 是 | 无                               | 倒计时的内容                       |
| WIDTH  | 是 | 无                               | 窗口的宽度                        |
| HEIGHT | 是 | 无                               | 窗口的高度                        |
| SIZE   | 是 | 无                               | 字体大小                         |

## 鸣谢
- [つきみむみ](https://www.pixiv.net/users/17674896) 图标来源 Pid: [128032053](https://www.pixiv.net/artworks/128032053)