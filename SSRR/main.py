from get_url import get_html,v2_find
from url_decode import   v2_decode
import json


def My_Config(v2ray):

	address = v2ray['add']

	port = v2ray['port']
	ID = v2ray['id']
	alterId = v2ray['aid']
	network = v2ray['net']
	typ = v2ray['type']
	true = 'true'
	false = 'false'

	vs = {
		"log": {
		"access": "/var/log/v2ray/access.log",
		"error": "/var/log/v2ray/error.log",
		"loglevel": "warning"
		},
		"inbound": {
		"listen": "127.0.0.1",
		"port": 1080,
		"protocol": "socks",
		"settings": {
		"auth": "noauth",
		"udp": true
		},
		"domainOverride": [
		"http",
		"tls"
		]
		},
		"outbound": {
		"protocol": "vmess",
		"settings": {
		"vnext": [
		{
		"address": address,
		"port": port,
		"users": [
		{
		"id": ID,
		"alterId": alterId,
		"security": typ,
		"level": 0
		}
		]
		}
		]
		},
		"tag": "proxy",
		"streamSettings": {
		"network": network,
		"security": "tls",
		"tlsSettings": {
		"serverName": "",
		"allowInsecure": false
		},
		"httpSettings": {
		"host": [],
		"path": "\/sever"
		}
		},
		"mux": {
		"enabled": false,
		"concurrency": 8
		}
		},
		"outboundDetour": [
		{
		"protocol": "freedom",
		"settings": {},
		"tag": "direct"
		},
		{
		"protocol": "blackhole",
		"settings": {},
		"tag": "block"
		}
		],
		"policy": {
		"level": {
		"0": {
		"handshake": 4,
		"connIdle": 300,
		"uplinkOnly": 2,
		"downlinkOnly": 5,
		"bufferSize": 10240
		}
		}
		},
		"routing": {
		"strategy": "rules",
		"settings": {
		"domainStrategy": "IPIfNonMatch",
		"rules": [
		{
		"type": "field",
		"ip": [
		"geoip:private"
		],
		"outboundTag": "direct"
		},
		{
		"type": "chinaip",
		"outboundTag": "direct"
		}
		]
		}
		}
		}
	with open('/etc/v2ray/config1.json','w') as file:
		json.dump(vs,file)






if __name__ == '__main__':
	html = get_html()
	v2ray = v2_find(html)
  #print('v2ray链接1:')
	v1 = v2_decode(v2ray[0])
	print('V2ray解码如下：')
	print(v1)
	  #print('v2ray链接2:')
	v2 = v2_decode(v2ray[1])
	print('V2ray解码如下：')
	print(v2)

	My_Config(v1)



