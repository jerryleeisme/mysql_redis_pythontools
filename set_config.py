#coding=utf-8
#中文编码必备否则编译时即出错
import config
#中文输出处理
def printzh(zh_text):
	print (zh_text).decode('utf-8').encode('gbk')
	pass
#输出配置信息
def config_show():
	printzh("mysql数据库IP地址："+config.mysql_host)
	printzh("mysql数据库端口："+config.mysql_port)
	printzh("mysql数据库连接账号："+config.mysql_acount)
	printzh("mysql数据库连接密码："+config.mysql_pass)
	printzh("redis数据库IP地址："+config.redis_host)
	printzh("redis数据库端口："+config.redis_port)
	printzh("redis数据库连接密码："+config.redis_pass)
	printzh("csv文件地址："+config.csv_file)
	printzh("json文件地址："+config.json_file)
	raw_input()
	pass