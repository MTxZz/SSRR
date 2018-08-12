import base64
import re
from get_url import get_html,v2_find,ssr_find
import json


re_clean_1 = re.compile('\/\/')
re_clean_2 = re.compile('b\'(.*)\'')
re_clean_3 = re.compile('_')


def v2_decode(v2_url):
	#v2_url = v2_url.encode(encoding="utf-8")
	v2 = re_clean_1.sub('',v2_url)
	js = base64.b64decode(v2).decode('utf-8')
	js = json.loads(js)

	print(type(js))
	return js

def ssr_decode(ssr_url):

	ssr = re_clean_1.sub('',ssr_url)
	ssr = re_clean_3.sub('+',ssr)
	ssr1 = base64.b64decode(ssr + '==' )
	tmp = str(ssr1).split('\'')

	arr1 = tmp[1].split(':')
	ssr2 =  arr1[5]
	ssr2 = str(ssr2)
	arr2  = ssr2.split('/?')
	p_tmp = arr2[0]+ '=='

	ip = arr1[0]
	port = arr1[1]
	protocol = arr1[2]
	method = arr1[3]
	obfs = arr1[4]  
	p = base64.b64decode(p_tmp).decode('iso-8859-15')
	password = p.split('?')[0]
	#print(password)

	js= {
	"server": ip,
	"server_port": port,
	"password": password,
	"obfs": obfs,
	"method": method,
	"protocol": protocol,
	}
	#js = json.loads(js)

	print(type(js))
	return js

if __name__ == '__main__':
	ssr_decode('//NTEuMTUuMjMwLjI0OToxODgwNDphdXRoX3NoYTFfdjQ6Y2hhY2hhMjA6cGxhaW46Wm1GdVoyVnhhV0Z1Wnk1amIyMC8_b2Jmc3BhcmFtPSZyZW1hcmtzPU9PYWNpRFRtbDZVdDVyT1Y1WnU5UkMzcG1aRHBnSjh4TWpBd1MwSXZVeTNvdEtibGo3ZmxycHJtbDdibW03VG1sckJvZEhSd2N6b3ZMMlpoYm1kbGNXbGhibWN1WTI5dA')
	v2_decode('//ew0KICAidiI6ICIyIiwNCiAgInBzIjogIjA4MTAt5rOV5Zu9LUMt6LSm5Y+35pu05paw77yaZmFuZ2VxaWFuZy5jb20iLA0KICAiYWRkIjogIjIxMi40Ny4yNDAuNzciLA0KICAicG9ydCI6ICIxNTI4NyIsDQogICJpZCI6ICJmMGJlODBlNS1iNTJlLTRhZWQtYWU1YS1hODgzNmU1MGYzOTQiLA0KICAiYWlkIjogIjY0IiwNCiAgIm5ldCI6ICJ0Y3AiLA0KICAidHlwZSI6ICJub25lIiwNCiAgImhvc3QiOiAiIiwNCiAgInBhdGgiOiAiIiwNCiAgInRscyI6ICIiDQp9')