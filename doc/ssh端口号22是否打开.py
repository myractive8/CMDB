import telnetlib
import re

tn = telnetlib.Telnet(host='192.168.1.30',port=22,timeout=5)
# read_until读取直到遇到了换行符或超时秒数。默认返回bytes类型，通过decode方法解码为字符串
tn_result = tn.read_until(b"\n",timeout=5).decode('utf-8')
print(tn_result)
##通过正则匹配且忽略大小写，寻找SSH服务是否开启
ssh_result =re.search(pattern=r'ssh',string=tn_result,flags=re.I)
print(ssh_result)
if ssh_result:
    print("Linux服务器存活")
else:
    print("其他服务器存活")
