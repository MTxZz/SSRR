import base64
import re
from get_url import v2_find
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


	return js

if __name__ == '__main__':
	v2_decode('//ew0KICAidiI6ICIyIiwNCiAgInBzIjogIjA4MTAt5rOV5Zu9LUMt6LSm5Y+35pu05paw77yaZmFuZ2VxaWFuZy5jb20iLA0KICAiYWRkIjogIjIxMi40Ny4yNDAuNzciLA0KICAicG9ydCI6ICIxNTI4NyIsDQogICJpZCI6ICJmMGJlODBlNS1iNTJlLTRhZWQtYWU1YS1hODgzNmU1MGYzOTQiLA0KICAiYWlkIjogIjY0IiwNCiAgIm5ldCI6ICJ0Y3AiLA0KICAidHlwZSI6ICJub25lIiwNCiAgImhvc3QiOiAiIiwNCiAgInBhdGgiOiAiIiwNCiAgInRscyI6ICIiDQp9')