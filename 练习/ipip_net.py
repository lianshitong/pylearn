import  os
from ipip import IP
from ipip import IPX
ip_addr = raw_input("请输入你要查询的IP地址：")
print ip_addr
IP.load(os.path.abspath("mydata4vipday2.dat"))
print IP.find(ip_addr)

IPX.load(os.path.abspath("mydata4vipday2.datx"))
print IPX.find(ip_addr)