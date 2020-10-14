from xml.dom.minidom import parse
import xml.dom.minidom
dtree=xml.dom.minidom.parse("abc.xml")
tagss=dtree.documentElement
print(tagss)
print(tagss.getElementsByTagName("evenmoreinfo"))
