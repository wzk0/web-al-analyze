## 我的前端学习之网页专辑解析器 NO.0

### 这是啥

我的第一个`完全自己手搓`的前端项目(上一个前端网易云不算数🌚)!

为了做好这个小东西,这几天猛研究`html`和`css`,`js`还在路上.

To sum up,这是我的`前端Hello World`.

### 效果

![李志-首页](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202211041552807.png)

![李志-专辑单页](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202211041552893.png)

> 这个排版有点奇怪...是因为我的`div`有点懵.

**光标触碰到卡片的时候会有一个比较好看的效果!**

### 用法

* 本地

`clone`此仓库,下载`flask`,进入文件夹,终端输入:

```
export FLASK_ENV=development
export FLASK_APP=main
flask run
```

* Demo

或访问此Demo站 >> http://thdbd.pythonanywhere.com

### 制作你的专辑集

只需编辑一个`json`文件,内容格式如下:

```json
[
    {
        "name": "快乐-(LP-version)",
        "al": "浴室-(LP-version)",
        "url": "https://ghproxy.com/https://raw.githubusercontent.com/wzk0/deca/main/songs/浴室-(LP-version)/快乐-(LP-version).mp3",
        "cover": "https://ghproxy.com/https://raw.githubusercontent.com/wzk0/deca/main/songs/浴室-(LP-version)/cover.png"
    },
    {
        "name": "一去不回来-(LP-version)",
        "al": "浴室-(LP-version)",
        "url": "https://ghproxy.com/https://raw.githubusercontent.com/wzk0/deca/main/songs/浴室-(LP-version)/一去不回来-(LP-version).mp3",
        "cover": "https://ghproxy.com/https://raw.githubusercontent.com/wzk0/deca/main/songs/浴室-(LP-version)/cover.png"
    }
]
```

> 大概结构就是一个列表围住一堆字典.

其中,`name`为歌曲名,`al`为此歌曲所在专辑名,`url`为音频直链,`cover`为专辑封面(是专辑的!不是单曲).

> 不要在专辑或歌曲名前后加歌手名!

随后修改`main.py`中,第七行的`文件名`,以及第十行的`ar`变量(歌手名).

基于此规则,我们的热心观众`听话的便当`制作了`Deca Joins`的专辑集 >> `list-decajoins.json`

### 开发

* 本来我想做一个支持`在线解析专辑json`的功能,但是现在有点困就先放弃了.

* 本来想做毛玻璃效果,但是不会,就做了蓝色钴玻璃效果.

* 本来想让首页的这些div能够居中,但是不会,只好整成这样.