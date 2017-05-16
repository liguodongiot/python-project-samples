
```
pyspider爬取的内容通过回调的参数response返回，response有多种解析方式。
1、response.json用于解析json数据
2、response.doc返回的是PyQuery对象
3、response.etree返回的是lxml对象
4、response.text返回的是unicode文本
5、response.content返回的是字节码
```
