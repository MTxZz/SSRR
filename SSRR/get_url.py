
import requests
import re
import base64


def get_html():
	url = 'https://fangeqiang.com/408.html'
	headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',}
	proxies = {
	'https':'socks5://127.0.0.1:1080',
	}

	resp = requests.get(url,headers = headers,proxies = proxies)
	html = resp.text
	return html

def ssr_find(html):

	ssr = []
	find = re.findall(r'https://api.mrxn.net/api.php\?data=ssr:(.*)\r',html)

	j = 0
	for f in find:
		j = j+1
		ssrhref = 'ssr:' + f
		ssr.append(f)
		#print(type(ssrhref))
		print('SSRR链接如下：')
		print(ssrhref)
	return ssr

def v2_find(html):

	v2ray = []
	find = re.findall(r'vmess:(.*)\r',html)

	i = 0
	for f in find:
		i = i+1
		v2href = 'vmess:' + f
		v2ray.append(f)
		#print(type(v2href))
		print('V2ray链接如下：')
		print(v2href)
	return v2ray
if __name__ == '__main__':
	html = get_html()
	v2_find(html)
	ssr_find(html)