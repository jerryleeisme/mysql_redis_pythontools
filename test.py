#coding=utf-8
#中文编码必备否则编译时即出错
#中文输出处理
import query
import json
import config
import redis

def printzh(zh_text):
	print (zh_text).decode('utf-8').encode('gbk')
	pass

# file = open("f:\\test.json",'r')
# # file = open("f:\\test.json",'wb+')
# # redis_client = redis.StrictRedis(host=config.redis_host, port=int(config.redis_port), db=0, password=config.redis_pass, charset='utf8')
# # content = list(redis_client.smembers("content"))
# # content_str = json.dumps(content)
# # file.write(content_str)
# # print file
# content_str = file.read()
# # print content_str
# content = json.loads(content_str)
# for c in content:
# 	print c
# 	pass
query.json_2_redis()
# query.redis_2_json()
raw_input()