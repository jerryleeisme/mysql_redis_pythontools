#coding=utf-8
#中文编码必备否则编译时即出错
import MySQLdb
import redis
import config
import json

#sql语句构建器
def sql_builder(table,fields,values):
	sql_str = ""
	if (len(fields) == 1):
		sql_str = "insert into "+table+" (%s) values ('%s')"
		pass
	if (len(fields) > 1):
		ins_str = ""
		ins_str_n = ""
		for x in range(1,len(fields)):
			ins_str = ins_str+",'%s'"
			ins_str_n = ins_str_n+",%s"
			pass
		sql_str = "insert into "+table+" (%s"+ins_str_n+") values ('%s'"+ins_str+")"
		pass
	source = fields+values
	return sql_str % source
	pass

#中文输出处理
def printzh(zh_text):
	print (zh_text).decode('utf-8').encode('gbk')
	pass
#mysql数据库连接测试
def mysql_connect_test():
	try:
		conn = MySQLdb.connect(host=config.mysql_host,user=config.mysql_acount,passwd=config.mysql_pass,port=int(config.mysql_port),charset="utf8")#添加字符编码避免数据从数据库取出时乱码现象
		if conn:
			printzh("mysql连接成功")
			pass
		else:
			printzh("mysql配置错误")
			pass
		pass
		conn.close()
	except Exception, e:
		conn.close()
		print e
	pass
#redis数据库连接测试
def redis_connect_test():
	try:
		client =  redis.StrictRedis(host=config.redis_host, port=int(config.redis_port), db=0, password=config.redis_pass)
		if(client.ping()):
			printzh("redis连接成功")
			pass
		else:
			printzh("redis连接失败")
			pass
		pass
	except Exception, e:
		print e
	pass
#csv文件连接测试
def csv_connect_test():
	try:
		csv_client = open(config.csv_file)
		if(csv_client):
			printzh("csv文件打开成功,输入y显示，n不显示文件内容")
			if (raw_input() == "y"):
				print csv_client.read()
				pass
			else:
				pass
			pass
		else:
			printzh("csv文件打开失败")
			pass
		csv_client.close()
		pass
	except Exception, e:
		print e
	pass
#json文件连接测试
def json_connect_test():
	try:
		json_client = open(config.json_file)
		if(json_client):
			printzh("json文件打开成功，输入y显示，n不显示文件内容")
			if(raw_input() == "y"):
				print json_client.read()
				pass
			else:
				pass
			pass
		pass
	except Exception, e:
		print e
	pass
#mysql数据库，库名查询
def mysql_db_show():
	try:
		conn = MySQLdb.connect(host=config.mysql_host,user=config.mysql_acount,passwd=config.mysql_pass,port=int(config.mysql_port),charset="utf8")#添加字符编码避免数据从数据库取出时乱码现象
		cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
		cur.execute('show databases;')
		results = cur.fetchall()
		for r in results:
			print r["Database"]
			pass
		conn.close()
		pass
	except Exception, e:
		print e
	pass
#mysql数据库，表名查询
def mysql_table_show(db):
	try:
		conn = MySQLdb.connect(host=config.mysql_host,user=config.mysql_acount,passwd=config.mysql_pass,port=int(config.mysql_port),charset="utf8")#添加字符编码避免数据从数据库取出时乱码现象
		cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
		conn.select_db(db)
		cur.execute('show tables;')
		results = cur.fetchall()
		for r in results:
			print r["Tables_in_"+db]
			pass
		conn.close()
		pass
	except Exception, e:
		print e
	pass
#mysql数据库表数据查询
def mysql_table_select(db,table):
	try:
		conn = MySQLdb.connect(host=config.mysql_host,user=config.mysql_acount,passwd=config.mysql_pass,port=int(config.mysql_port),charset="utf8")#添加字符编码避免数据从数据库取出时乱码现象
		cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
		conn.select_db(db)
		cur.execute('select * from '+table)
		results = cur.fetchall()
		for r in results:
			print r
			pass
		conn.close()
		pass
	except Exception, e:
		print e
	pass
#mysql数据表清空
def mysql_table_clear(db,table):
	try:
		conn = MySQLdb.connect(host=config.mysql_host,user=config.mysql_acount,passwd=config.mysql_pass,port=int(config.mysql_port),charset="utf8")#添加字符编码避免数据从数据库取出时乱码现象
		cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
		conn.select_db(db)
		cur.execute('delete from '+table)
		conn.commit()
		conn.close()
		pass
	except Exception, e:
		conn.rollback()
		conn.close()
		print e
	pass
#redis列出所有键名
def redis_list_keys():
	try:
		client =  redis.StrictRedis(host=config.redis_host, port=int(config.redis_port), db=0, password=config.redis_pass)
		print client.ping()
		result = client.keys()
		print result
		pass
	except Exception, e:
		print e
	pass
#redis显示键值
def redis_show_key(key_name):
	try:
		client =  redis.StrictRedis(host=config.redis_host, port=int(config.redis_port), db=0, password=config.redis_pass)
		key_type = client.type(key_name)
		if (key_type == "hash"):
			print client.hgetall(key_name)
			pass
		if (key_type == "string"):
			print client.get(key_name)
			pass
		if (key_type == "set"):
			print client.smembers(key_name)
			pass
		if (key_type == "zset"):
			print client.zrangebyscore(key_name,0,-1)
			pass
		if (key_type == "list"):
			print client.lrange(key_name,0,-1)
			pass
		pass
	except Exception, e:
		print e
	pass
#redis删除键值
def redis_delete_key(key_name):
	try:
		client =  redis.StrictRedis(host=config.redis_host, port=int(config.redis_port), db=0, password=config.redis_pass)
		result = client.delete(key_name)
		if(result):
			printzh("删除成功")
		pass
	except Exception, e:
		print e
	pass
#csv文件清空
def csv_clear():
	csv_client = open(config.csv_file,'wb')
	if(csv_client):
		csv_client.write("")
		pass
	csv_client.close()
	pass
#json文件清空
def json_clear():
	json_client = open(config.json_file,'wb')
	if(json_client):
		json_client.write("")
		pass
	json_client.close()
	pass
#mysql导入redis流程
def mysql_2_redis(store_info):
	#数据库连接开始
	try:
		redis_client = redis.StrictRedis(host=config.redis_host, port=int(config.redis_port), db=0, password=config.redis_pass)
		mysql_conn = MySQLdb.connect(host=config.mysql_host,user=config.mysql_acount,passwd=config.mysql_pass,port=int(config.mysql_port),charset="utf8")#添加字符编码避免数据从数据库取出时乱码现象
		mysql_cur = mysql_conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
		#处理导出业务
		if (store_info.has_key("key_type")):
			if (store_info["key_type"] == "string"):
				if (store_info.has_key("key_name") and store_info.has_key("key_value")):
					if (redis_client.set(store_info["key_name"],store_info["key_value"])):
						printzh("存储成功")
						pass
					else:
						printzh("存储失败")
						pass
					pass
				else:
					printzh("参数不全")
				pass
			pass
			if (store_info["key_type"] == "set"):
				if (store_info.has_key("key_name") and store_info.has_key("db") and store_info.has_key("table") and store_info.has_key("field")):
					mysql_conn.select_db(store_info["db"])
					mysql_cur.execute('select '+store_info["field"]+' from '+store_info["table"])
					results = mysql_cur.fetchall()
					for r in results:
						#print r[store_info["field"]]
						redis_client.sadd(store_info['key_name'],r[store_info["field"]])
						pass
					pass
				else:
					printzh("参数不全")
					pass
				pass
			if (store_info["key_type"] == "zset"):
				if (store_info.has_key("key_name") and store_info.has_key("db") and store_info.has_key("table") and store_info.has_key("field") and store_info.has_key("score")):
					mysql_conn.select_db(store_info["db"])
					mysql_cur.execute('select '+store_info["field"]+','+store_info["score"]+' from '+store_info["table"])
					results = mysql_cur.fetchall()
					for r in results:
						redis_client.zadd(store_info["key_name"],r[store_info["score"]],r[store_info["field"]])
						pass
					pass
				else:
					printzh("参数不全")
					pass
				pass
			if (store_info["key_type"] == "list"):
				if (store_info.has_key("key_name") and store_info.has_key("db") and store_info.has_key("table") and store_info.has_key("field")):
					mysql_conn.select_db(store_info["db"])
					mysql_cur.execute('select '+store_info["field"]+' from '+store_info["table"])
					results = mysql_cur.fetchall()
					for r in results:
						redis_client.lpush(store_info["key_name"],r[store_info["field"]])
						pass
					pass
				else:
					printzh("参数不全")
					pass
				pass
			if (store_info["key_type"] == "hash"):
				if (store_info.has_key("key_name") and store_info.has_key("db") and store_info.has_key("table")):
					mysql_conn.select_db(store_info["db"])
					mysql_cur.execute('select * from '+store_info["table"])
					results = mysql_cur.fetchall()
					for r in results:
						redis_client.sadd(store_info["key_name"],store_info["key_name"]+":%d"%r['id'])
						redis_client.hmset(store_info["key_name"]+":%d"%r['id'],r)
						pass
					pass
				else:
					printzh("参数不全")
					pass
				pass
		else:
			printzh("未选择存储类型")
			pass		
		pass
	except Exception, e:
		print e
		mysql_conn.close()
	#数据库连接结束

	pass
#redis导入mysql
def redis_2_mysql(key_name):
	try:
		redis_client = redis.StrictRedis(host=config.redis_host, port=int(config.redis_port), db=0, password=config.redis_pass, charset='utf8')
		mysql_conn = MySQLdb.connect(host=config.mysql_host,user=config.mysql_acount,passwd=config.mysql_pass,port=int(config.mysql_port),charset="utf8")#添加字符编码避免数据从数据库取出时乱码现象
		mysql_cur = mysql_conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
		if (redis_client.exists(key_name)):
			if (redis_client.type(key_name) == "set"):
				printzh("请输入要导入的mysql数据库名")
				db = raw_input()
				printzh("请输入要导入的mysql数据表名,导入前确保表结构已建立")
				table = raw_input()
				mysql_conn.select_db(db)
				results = redis_client.smembers(key_name)
				for r in results:
					print r
					fields = redis_client.hkeys(r)
					values = redis_client.hgetall(r)
					value_list = []
					for x in fields:
						value_list.append(values[x])
						pass
					# print tuple(fields)
					# print tuple(value_list)
					sql_str = sql_builder(table,tuple(fields),tuple(value_list))
					# print sql_str
					mysql_cur.execute(sql_str)
					mysql_conn.commit()
					pass
				pass
			else:
				printzh("该类型内容不支持导入到mysql数据库")
				pass
			pass
		pass
	except Exception, e:
		print e
	pass
#mysql导入csv
def mysql_2_csv():
	
	pass
#csv导入mysql
def csv_2_mysql():
	
	pass
#redis导入json
def redis_2_json():
	try:
		redis_client = redis.StrictRedis(host=config.redis_host, port=int(config.redis_port), db=0, password=config.redis_pass, charset='utf8')
		printzh("请输入要导出的redis键名")
		key_name = raw_input()
		printzh("请输入要导出的json文件地址,回车使用系统设置文件地址")
		json_file = raw_input()
		if (json_file != ""):
			json_client = open(json_file,'wb+')
			pass
		else:
			json_client = open(config.json_file,'wb+')
			pass
		key_type = redis_client.type(key_name)
		if (key_type == "hash"):
			print redis_client.hgetall(key_name)
			json_client.writelines("{\""+key_name+"\":"+json.dumps(redis_client.hgetall(key_name))+"}\n")
			pass
		if (key_type == "string"):
			print redis_client.get(key_name)
			json_client.writelines("{\""+key_name+"\":"+redis_client.get(key_name)+"}\n")
			pass
		if (key_type == "set"):
			print redis_client.smembers(key_name)
			json_client.writelines("{\""+key_name+"\":"+json.dumps(list(redis_client.smembers(key_name)))+"}\n")
			printzh("是否同时导出关联hash表内容,y导出，n不导出")
			if (raw_input() == "y"):
				for item in redis_client.smembers(key_name):
					json_client.writelines("{\""+item+"\":"+json.dumps(redis_client.hgetall(item))+"}\n")
					pass
				pass
			pass
		if (key_type == "zset"):
			print redis_client.zrangebyscore(key_name,0,-1)
			json_client.writelines("{\""+key_name+"\":"+json.dumps(redis_client.zrangebyscore(key_name,0,-1))+"}\n")
			pass
		if (key_type == "list"):
			print redis_client.lrange(key_name,0,-1)
			json_client.writelines("{\""+key_name+"\":"+json.dumps(redis_client.lrange(key_name,0,-1))+"}\n")
			pass
		printzh("导出完毕")
		json_client.close()
		pass
	except Exception, e:
		print e
	pass
#json导入redis
def json_2_redis():
	try:
		redis_client = redis.StrictRedis(host=config.redis_host, port=int(config.redis_port), db=0, password=config.redis_pass, charset='utf8')
		printzh("请输入要导入的文件地址")
		json_file = raw_input()
		json_client = open(json_file,'r')
		printzh("请输入要导入redis的数据类型")
		printzh("1:string")
		printzh("2:set")
		printzh("3:zset")
		printzh("4:list")
		printzh("5:hash")
		key_type = raw_input()
		printzh("请输入键名")
		key_name = raw_input()
		printzh("请输入要导入redis的键名,默认与json键名相同")
		redis_key_name = raw_input()
		if (redis_key_name == ""):
			redis_key_name = key_name
			pass
		else:
			pass
		if (key_type == "1"):
			if (redis_client.set(key_name,json_client.read())):
				printzh("导入完毕")
				pass
			pass
		if (key_type == "2"):
			content = json_client.readlines()
			set_content = json.loads(content[0])
			for k in set_content[key_name]:
				redis_client.sadd(redis_key_name,k)
				pass
			if (content[1]):
				for c in xrange(1,len(content)):
					c_node = json.loads(content[c])
					redis_client.hmset(c_node.keys()[0],c_node[c_node.keys()[0]])
					keys = c_node[c_node.keys()[0]].keys()
					pass
				pass
			printzh("导入完毕")
			pass
		if (key_type == "3"):
			# 导入zset文件
			pass
		if (key_type == "4"):
			# 导入list文件
			pass
		if (key_type == "5"):
			# 导入hash文件
			pass
		pass
	except Exception, e:
		print e
	pass
