# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import openpyxl
import urllib.request

def saveHtm(file_name, file_content):
    with open(file_name.replace('/', '_') + ".html", "wb") as f:
        f.write(file_content)

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4'
headers = {"User-Agent": "dududu"}
data = requests.get(url, headers=headers).text

html = etree.HTML(data)
htm = urllib.request.urlopen(url).read()
saveHtm("china", htm)
json_text = html.xpath('//script[@type="application/json"]/text()')
json_text = json_text[0]

result = json.loads(json_text)
result = result["component"]
result = result[0]["caseList"]

#建立数据文档
data_sheet = openpyxl.Workbook()
sheet = data_sheet.active
sheet.title = "国内疫情"
sheet.append(["疫情地区","新增","现有","累计","治愈","死亡"])
for line in result:
    line_name = [line["area"],line["confirmedRelative"],line["curConfirm"],line["confirmed"],line["crued"],line["died"]]
    for ele in line_name:
        if ele == '':
            ele = 0
    sheet.append(line_name)
data_sheet.save("./china.csv")