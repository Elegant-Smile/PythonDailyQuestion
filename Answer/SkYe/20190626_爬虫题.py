import requests
url = input("输入爬取的URL:\n")
times = 0
while times <3:
	try:		r = requests.get(url,timeout=5)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		print(r.text[:1500])
		break
	except:
		times += 1
		print("第{}次错误,正在重试...".format(times))
else:
	print("None")
