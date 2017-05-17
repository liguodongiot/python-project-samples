


### 利用phantomjs解决js问题

#### 示例说明：
**如果页面中部分数据或文字由js生成，pyspider不能直接提取页面的数据。pyspider获取页面的代码，
但是其中的js代码，用phantomjs解决js代码执行问题。**

#### 使用方法：
**
方法一：在self.crawl函数中添加fetch_type="js"调用phantomjs执行js代码。
方法二：为函数添加参数@config(fetch_type="js")。
**

#### 示例代码：
**phantomjs_demo**


### 解析JSON数据
**
pyspider爬取的内容通过回调的参数response返回，response有多种解析方式。
1、response.json用于解析json数据，
2、response.doc返回的是PyQuery对象，
3、response.etree返回的是lxml对象，
4、response.text返回的是unicode文本，
5、response.content返回的是字节码。

本示例主要是利用response.json解析返回的json数据。
**

```json
{
    "status": 1, 
    "data": {
        "total": 11489, 
        "next_start": 24, 
        "login_user": { }, 
        "object_list": [
            {
                "id": 14615786, 
                "username": "ZY你爸爸", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201704/21/20170421193515_haMTx.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 0, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 13709946, 
                "username": "Biubiubiutiful", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201702/22/20170222131816_HNP5L.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 0, 
                "city": "WORLDWIDE Vietnam", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 13564237, 
                "username": "林深时见鹿lw", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201612/05/20161205081507_ZS4yH.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 1, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 3160052, 
                "username": "by水边的文字屋", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201702/18/20170218235042_kxPWi.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 5044, 
                "city": "WORLDWIDE-Russia", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "但是我们还年轻，一切都还是充满希望着的。", 
                "letter_accessable": 0
            }, 
            {
                "id": 11690580, 
                "username": "iii薄荷梦", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201612/07/20161207182504_rZQXE.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 6, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 11361161, 
                "username": "QXJH", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201607/14/20160714211659_SeUnh.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 497, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 11655634, 
                "username": "摆渡人ai", 
                "avatar": "https://b-ssl.duitang.com/uploads/files/201312/19/20131219204922_5WTEa.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 0, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 14787275, 
                "username": "A--a", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201705/12/20170512112814_Xiskc.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 2, 
                "city": "浙江 杭州 ", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "对明天最好的准备，就是今天做到最好（微博@Shorty女生）", 
                "letter_accessable": 0
            }, 
            {
                "id": 14763758, 
                "username": "alubaby-", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201705/08/20170508210423_3jtVX.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 0, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 14773282, 
                "username": "土豆妹妹cici", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201705/10/20170510102708_PSmxE.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 0, 
                "city": "广州", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 12347224, 
                "username": "清歌寒.", 
                "avatar": "https://b-ssl.duitang.com/uploads/item/201611/13/20161113193634_HRTLa.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 268, 
                "city": "山东-淄博", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "难过若写不完 用情歌刁难", 
                "letter_accessable": 0
            }, 
            {
                "id": 977184, 
                "username": "hygeia1", 
                "avatar": "https://b-ssl.duitang.com/uploads/files/201312/19/20131219204950_iRLAQ.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 89, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 2467720, 
                "username": "Anisa", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201508/31/20150831204230_reBxU.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 1, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 12657988, 
                "username": "旖旎的", 
                "avatar": "https://b-ssl.duitang.com/uploads/files/201312/19/20131219204819_UdLfz.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 0, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 10744837, 
                "username": "淘小碗", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201606/17/20160617222139_WxZiw.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 196, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 2171239, 
                "username": "别梦他", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201402/16/20140216154334_fSx8x.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 2463, 
                "city": "广东省 ", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "刷屏能手", 
                "letter_accessable": 0
            }, 
            {
                "id": 185947, 
                "username": "杨小乐", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201507/10/20150710230149_icXFu.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 2102, 
                "city": "辽宁 大连 ", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "喜欢咖啡，喜欢茶；喜欢香水，喜欢多肉；喜欢下雨，喜欢下雪；喜欢一切世间的美好", 
                "letter_accessable": 0
            }, 
            {
                "id": 9110577, 
                "username": "采集一罐阳光", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201705/04/20170504223641_ak8dB.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 211, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 13328458, 
                "username": "低眉泯恩仇", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201611/02/20161102174236_EcRyH.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 7, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 13438291, 
                "username": "赵权爱佳仁", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201611/17/20161117235730_eFwNV.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 0, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "我的梦想是环游世界～", 
                "letter_accessable": 0
            }, 
            {
                "id": 9930266, 
                "username": "淘呀", 
                "avatar": "https://a-ssl.duitang.com/uploads/people/201508/12/20150812203441_JBLAW.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 0, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }, 
            {
                "id": 14649172, 
                "username": "cheese_cream", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201704/23/20170423150611_nzUKQ.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 8, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "大世界，走走，看看，试试", 
                "letter_accessable": 0
            }, 
            {
                "id": 14747023, 
                "username": "水手小孩", 
                "avatar": "https://b-ssl.duitang.com/uploads/item/201705/07/20170507124150_5xnrA.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 0, 
                "city": "", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "你的故事我什么位置", 
                "letter_accessable": 0
            }, 
            {
                "id": 14424214, 
                "username": "挽L", 
                "avatar": "https://b-ssl.duitang.com/uploads/people/201703/25/20170325175822_PZAtV.jpeg", 
                "identity": [
                    "normal"
                ], 
                "score": 32, 
                "city": "南宁", 
                "relationship": 0, 
                "is_certify_user": false, 
                "short_description": "", 
                "letter_accessable": 0
            }
        ], 
        "more": 1, 
        "limit": 1000, 
        "visit_user": {
            "user_id": 116965, 
            "username": "夏茵"
        }
    }
}
```
#### 示例代码：
**json_parse_duitang_demo**

### 用PyQuery解析页面数据

#### 示例说明：
**本示例主要是PyQuery解析返回的response页面数据。
response.doc解析页面数据是pyspider的主要用法，应该熟练掌握基本使用方法。**

#### 使用方法：
**PyQuery可以采用CSS选择器作为参数对网页进行解析。**
```
response.doc('.ml.mlt.mtw.cl > li').items()
response.doc('.pti > .pdbt > .authi > em > span').attr('title')
```

**CSS选择器**

|选择器				|示例					|示例说明                                                                                  |
|:------------      | :--------             | :----                                                                                    |
|.class 			|	.intro 				|	Selects all elements with class=”intro”                                                |
|#id 				|#firstname 			|	Selects the element with id=”firstname”                                                |
|element 			|p 						|Selects all <p> elements                                                                  |
|element,element 	|div, p 				|	Selects all <div> elements and all <p> elements                                        |
|element element 	|div p 					|Selects all <p> elements inside <div> elements                                            |
|element>element 	|div > p 				|Selects all <p> elements where the parent is a <div> element                              |
|[attribute] 		|[target] 				|Selects all elements with a target attribute                                              |
|[attribute=value] 	|[target=_blank] 		|Selects all elements with target=”_blank”                                                 |
|[attribute^=value] |a[href^=”https”] 	|	Selects every <a> element whose href attribute value begins with “https”               |
|[attribute$=value] |a[href$=”.pdf”] 	    |	Selects every <a> element whose href attribute value ends with “.pdf”                  |
|[attribute*=value] |a[href*=”w3schools”] | 	Selects every <a> element whose href attribute value contains the substring “w3schools”|
|:checked 			|input:checked 			|Selects every checked <input> element                                                     |


