import requests

urls = [
    "https://epg.pw/api/epg.xml?channel_id=464293",
    "https://epg.pw/api/epg.xml?channel_id=463999",
    "https://epg.pw/api/epg.xml?channel_id=463905",
    "https://epg.pw/api/epg.xml?channel_id=463993",
    "https://epg.pw/api/epg.xml?channel_id=464263",
    "https://epg.pw/api/epg.xml?channel_id=464016"
]

channels = []
programmes = []

for url in urls:
    xml = requests.get(url).text

    ch_start = xml.find("<channel")
    ch_end = xml.find("</channel>") + len("</channel>")
    pr_start = xml.find("<programme")

    channels.append(xml[ch_start:ch_end])
    programmes.append(xml[pr_start:].replace("</tv>", ""))

final_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<tv>\n'

for ch in channels:
    final_xml += ch + "\n"

for pr in programmes:
    final_xml += pr + "\n"

final_xml += "</tv>"

with open("epg.xml", "w", encoding="utf-8") as f:
    f.write(final_xml)
