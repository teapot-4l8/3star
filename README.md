# 运行
1. 用抓包工具抓包。教程：https://www.bilibili.com/video/BV1vM4y1V78M/
2. 把 `uid` 换成你自己的
3. 运行脚本 [完整挂机脚本](完整挂机脚本.py)

脚本可脱机运行，运行时关闭小程序

# 已完成：
- 每日签到
- 任务·看视频x5
- 任务·打开小程序x2
- 任务·抽奖x6
- 每日上限钻石拉满并存入xyl星球 13秒就能获得钻石，不需要等30秒啦~


# 以下是原理记录，可以不看
# 调试，环境配置

微信开发者打开，提示`用户异常`，怀疑是ua或uid的关系。

抓正常的包，发现uid是有值的，用python,只替换掉uid，请求成功返回正确值。


```json
{"status":200,"data":{"massage":{"id":199012,"nickName":"","avatarUrl":"http:\/\/xcx.cdn.vipxufan.com\/dynamic\/171\/uploads\/7740581754f9f09cb99dceebca95bde6\/1729217878.jpg?sign=1729250708-1729250708-0-54ba2cb19fd1e7e41e5669c1d7a26d82","valid_num":57,"succession":1,"vip_end_date":null,"play_num":121,"vip_id":0,"kid_hit":1},"notice":0,"tanchu":0,"noticed":0,"is_show":0,"vip_img":[{"img":"http:\/\/xcx.cdn.vipxufan.com\/static\/171\/vip\/vip-1.png?sign=1729250708-1729250708-0-cff6ae29bb954e6568754aa23d412b9c","status":0,"name":"周会员","money":"28.00","money_vip":"58","msg":"回复\"6\""},{"img":"http:\/\/xcx.cdn.vipxufan.com\/dynamic\/171\/vip\/vip-2.png?sign=1729250708-1729250708-0-973f55ae56d45e110d01776cc9e82bed","status":0,"name":"月会员","money":"98.00","money_vip":"218","msg":"回复\"6\""},{"img":"http:\/\/xcx.cdn.vipxufan.com\/dynamic\/171\/vip\/vip-4.png?sign=1729250708-1729250708-0-3258e1c57f2b15f9032803984f2cd555","status":0,"name":"年会员","money":"528.00","money_vip":"1328","msg":"回复\"6\""}]},"msg":"ok","err":null}
```

观察返回值，发现id是正常的用户id。

微信开发者工具里的并没有成功登陆，不知道为什么，总是提示code不合法

# 静态分析

## 登陆

打开调试台，发现报错

![image-20241018193438575](README.assets/image-20241018193438575.png)

感觉有点可疑

可发现登陆接口

```javascript
    function s(t, n) {
        wx.login({
            success: function(o) {
                console.log(o);
                var a = o.code;
                wx.showLoading({
                    title: "加载中",
                    mask: !0
                });
                var s = wx.getStorageSync("user");
                s.uid ? t.uid = s.uid : s = {},
                t.code = a,
                t.xid = 171,
                i("https://xcx.vipxufan.com/star/apix171/login", "POST", t, function(i) {
                    if (wx.hideLoading(),
                    "no" == i || 0 == i.status) {
                        var o = "登录失败,请稍后再试!";
                        i.msg && (o = i.msg),
                        wx.showModal({
                            title: "提示",
                            content: o,
                            showCancel: !1,
                            success: function(t) {}
                        });
                    } else
                        t.uinfo ? (s = JSON.parse(t.uinfo)).uid = i.data.uid : s.uid = i.data.uid,
                        wx.setStorageSync("user", s),
                        wx.setStorageSync("isLogin", "1"),
                        e(n) && n(i);
                }, function() {
                    wx.hideLoading();
                }, function() {});
            },
            fail: function() {
                wx.hideLoading();
            },
            complete: {}
        });
    }
```

```javascript
    function i(t, n, i, a, s, u) {
        "" == n && (n = "GET");
        var c = "application/json";
        "POST" == n && (c = "application/x-www-form-urlencoded"),
        wx.request({
            url: t,
            data: i,
            dataType: "json",
            method: n,
            header: {
                "Content-Type": c
            },
            success: function(n) {
                200 == n.statusCode ? e(a) && a(n.data) : (o(t, i, n),
                e(s) && s());
            },
            fail: function(n) {
                console.log("error"),
                o(t, i, n),
                e(s) && s();
            },
            complete: function() {
                e(u) && u();
            }
        });
    }
```

data是i,post请求

然后找network，发现原来是code出问题了

![image-20241018194225630](README.assets/image-20241018194225630.png)

https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html

这是官方给的接口，code是官方返回的，那没办法了。。。暂时没想到解决思路，先放放



## 点击钻石

直接repeat会返回用户异常

接着上面，附近这块儿代码像加密的地方

```javascript
    function a() {
        var t = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
          , i = Math.floor(Math.random() * t.length) > t.length - 9 ? t.length - 9 : Math.floor(Math.random() * t.length)
          , o = t.slice(i, i + 8)
          , a = Math.ceil(new Date().valueOf())
          , e = n.hex_md5(a + o + "meida123456" + wx.getStorageSync("user").uid);
        e = n.hex_md5(e);
        var s = {};
        return s.timeStamp = a,
        s.randomStr = o,
        s.signature = e,
        s;
    }
```

它有三个地方可以点，我发现点了其中一个，然后点最小化让它挂在后台，再刷新，三个地方的数量会重新刷新，这貌似是个bug

点开抓包的地方，发现它的数量貌似是记录在前端的

![image-20241018201551165](README.assets/image-20241018201551165.png)


搜索`validNum`

![image-20241018204807637](README.assets/image-20241018204807637.png)

点进a，跳转到原先猜测的地方，说明加密位置就在那里。

写python函数

```python
def a(uid):
    t = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    i = random.randint(0, len(t))
    if i > len(t) - 9:
        i = len(t) - 9
    o = t[i:i + 8]
    a = time.time() * 1000
    # 假设存在一个函数计算 MD5 的十六进制值，这里只是模拟
    def hex_md5(data):
        m = hashlib.md5()
        m.update(data.encode())
        return m.hexdigest()
    s = str(int(a)) + o + "meida123456" + uid
    # s = "1729254984360XYZ01234meida1234567740581754f9f09cb99dceebca95bde6"
    e = hex_md5(s)
    e = hex_md5(e)
    return a, o, e
```

遗憾的是，一个用户靠这种方法获得的钻石一天内有上限，超过了会提示用户异常

```json
{"status":200,"data":null,"msg":200,"err":"今日已产满"}
```

正常情况

```json
{"status":200,"data":1,"msg":null,"err":"返回成功"}
```

## 看视频

抓到包后直接repeat，居然能增加钻石个数，看来每个接口的校验严格程度都不一样啊！

视频一天只能看五次

```json
{
	"status": 200,
	"data": {
		"is_view": 1,
		"num": 5,
		"rank": 1,
		"total_num": 5,
		"msg": "ok"
	},
	"msg": "ok",
	"err": null
}
```

奇怪的是，昨天的脚本可以运行，但是今天的却没用了！一直返回

```json
{"status":200,"data":{"is_view":0},"msg":"ok","err":"no"}
```

看来应该是漏了某些包需要发送吧

10.22又试了一下，可以运行，发了不到5次，却是显示观看了视频5次，奇怪



## 发超话

微博超话发帖:会记录帖子是否被领取过

注意到返回内容

```json
{
	"status": 200,
	"data": {
		"status": 1,
		"msg": "快来wx小橙序『五号星球』一起为爱心公益助力，我们在[给你小心心]XX星球[给你小心心]等你哦~"
	},
	"msg": "",
	"err": ""
}
```

猜测msg是用来判断的基本模板。用gitee建立公开仓库，存入纯文档，点击`原始数据`,拿到url，塞进去测试能不能校验通过

试了，不能:(

再次尝试

内容为微博网页源代码

返回

```json
{"status":200,"data":0,"msg":"该超话任务不是今天的哦","err":null}
```

貌似还检测了发帖时间，还没在页面源代码里找到相应位置

伪造微博已完成。

# 尝试

签到api，修改时间，没用

邀请用户，修改uid，没用

都会提示用户异常

获取钻石的记录疑似后台会保存，短时间内获取数量太多会提示用户异常

检查一下，发现每隔30秒都会有validsave的请求，而且短时间内重复发送会用户异常

最小间隔13秒

抽奖，注意到
```
"angle": "0",
```

返回的值似乎是固定的。尝试更改初始angle


