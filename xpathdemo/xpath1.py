from lxml import etree
# 解析本地文件
tree = etree.parse('xpath1.html')
# li_list = tree.xpath('//body//li')
li_list = tree.xpath('//ul/li[@id]/text()')
li_list = tree.xpath('//ul/li[@id="l1"]/text()')
# 引号
# 查找id=l1的li标签的class值
li = tree.xpath('//ul/li[@id="l1"]/@class')
# 查询id包含l的li标签
li = tree.xpath('//ul/li[contains(@id,"l")]/text()')
li = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
li = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
li = tree.xpath('//ul/li[@id="l1"]/text()|//ul/li[@id="l2"]/text()')
print(li)