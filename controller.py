#coding=utf-8
#中文编码必备否则编译时即出错
import redis
import MySQLdb
import config
import menu
import query
import set_config

def main():
	while True:
		menu.welcome_view()
		cmd_a = raw_input()
		if(cmd_a == "1"):
			while True:
				menu.set_view()
				cmd_a1 = raw_input()
				if(cmd_a1 == "1"):
					#A11mysql连接配置
					while True:
						menu.set_mysql_view()
						cmd_a11 = raw_input()
						if(cmd_a11 == "1"):
							#A111mysql数据库IP地址
							config.mysql_host = raw_input()
							pass
						if(cmd_a11 == "2"):
							#A112mysql数据库端口
							config.mysql_port = raw_input()
							pass
						if(cmd_a11 == "3"):
							#A113mysql数据库连接账号
							config.mysql_acount = raw_input()
							pass
						if(cmd_a11 == "4"):
							#A114mysql数据库连接密码
							config.mysql_pass = raw_input()
							pass
						if(cmd_a11 == "5"):
							#A115测试连接
							query.mysql_connect_test()
							pass
						if(cmd_a11 == "6"):
							#A116退出
							break;						
						pass
					pass
				if (cmd_a1 == "2"):
					#A12redis连接配置
					while True:
						menu.set_redis_view()
						cmd_a12 = raw_input()
						if(cmd_a12 == '1'):
							config.redis_host = raw_input()
							pass
						if (cmd_a12 == '2'):
							config.redis_port = raw_input()
							pass
						if (cmd_a12 == '3'):
							config.redis_pass = raw_input()
							pass
						if (cmd_a12 == '4'):
							query.redis_connect_test()
							pass
						if (cmd_a12 == '5'):
							break
							pass						
						pass
					pass
				if (cmd_a1 == "3"):
					#A13csv连接配置
					while True:
						menu.set_csv_view()
						cmd_a13 = raw_input()
						if(cmd_a13 == '1'):
							config.csv_file = raw_input()
							pass
						if (cmd_a13 == '2'):
							query.csv_connect_test()
							pass
						if (cmd_a13 == '3'):
							break
							pass
						pass
					pass
				if (cmd_a1 == "4"):
					#A14json连接配置
					while True:
						menu.set_json_view()
						cmd_a14 = raw_input()
						if(cmd_a14 == '1'):
							config.json_file = raw_input()
							pass
						if(cmd_a14 == '2'):
							query.json_connect_test()
							pass
						if(cmd_a14 == '3'):
							break
							pass
						pass
					pass
				if (cmd_a1 == "5"):
					#A15配置信息输出
					set_config.config_show()
					pass
				if (cmd_a1 == "6"):
					#A16退出
					break;
					pass
			pass
		if (cmd_a == "2"):
			#A2查询工具
			while True:
				menu.query_view()
				cmd_a2 = raw_input()
				if(cmd_a2 == "1"):
					while True:
						menu.query_mysql_view()
						cmd_a21 = raw_input()
						if(cmd_a21 == "1"):
							query.mysql_db_show()
							pass
						if (cmd_a21 == "2"):
							query.printzh("请输入数据库名")
							db = raw_input()
							query.mysql_table_show(db)
							pass
						if (cmd_a21 == "3"):
							query.printzh("请输入数据库名")
							db = raw_input()
							query.printzh("请输入数据表名")
							table = raw_input()
							query.mysql_table_select(db,table)
							pass
						if (cmd_a21 == "4"):
							query.printzh("请输入数据库名")
							db = raw_input()
							query.printzh("请输入数据表名")
							table = raw_input()
							query.printzh("确定清除"+db+"下的"+table+"表数据，y确定，n取消")
							if (raw_input() == 'y'):
								query.mysql_table_clear(db,table)
								pass
							pass
						if (cmd_a21 == "5"):
							break
							pass
						pass
					pass
				if(cmd_a2 == "2"):
					while True:
						menu.query_redis_view()
						cmd_a22 = raw_input()
						if (cmd_a22 == "1"):
							query.redis_list_keys()
							pass
						if (cmd_a22 == "2"):
							query.printzh("请输入键名")
							key_name = raw_input()
							query.redis_show_key(key_name)
							pass
						if (cmd_a22 == "3"):
							query.printzh("请输入键名")
							key_name = raw_input()
							query.printzh("确定删除"+key_name+"下的内容，y确定，n取消")
							if(raw_input() == "y"):
								query.redis_delete_key(key_name)
							pass
						if (cmd_a22 == "4"):
							break
							pass						
						pass
					pass
				if (cmd_a2 == "3"):
					while True:
						menu.query_csv_view()
						cmd_a23 = raw_input()
						if (cmd_a23 == "1"):
							query.csv_connect_test()
							pass
						if (cmd_a23 == "2"):
							query.printzh("确定清空"+config.csv_file+",y确定，n取消")
							if (raw_input() == "y"):
								query.csv_clear()
								pass
							pass
						if (cmd_a23 == "3"):
							break
							pass
						pass
					pass
				if (cmd_a2 == "4"):
					while True:
						menu.query_json_view()
						cmd_a23 = raw_input()
						if (cmd_a23 == "1"):
							query.json_connect_test()
							pass
						if (cmd_a23 == "2"):
							query.printzh("确定清空"+config.json_file+",y确定，n取消")
							if (raw_input() == "y"):
								query.json_clear()
								pass
							pass
						if (cmd_a23 == "3"):
							break
							pass
						pass
						pass
					pass
				if (cmd_a2 == "5"):
					break
					pass
				pass
			pass
		if (cmd_a == "3"):
			#A3导入导出工具
			while True:
				menu.import_view()
				cmd_a3 = raw_input()
				if (cmd_a3 == "1"):
					#A31mysql导入redis
					types = {"1":"string","2":"set","3":"zset","4":"list","5":"hash"}
					printzh("请选择要存储的redis类型")
					printzh("1.string")
					printzh("2.set")
					printzh("3.zset")
					printzh("4.list")
					printzh("5.hash")
					key_type = types[raw_input()]
					printzh("存储类型为："+key_type)
					if (key_type == "string"):
						printzh("请输入要存储的键名")
						key_name = raw_input()
						printzh("请输入要存储的键值")
						key_value = raw_input()
						#存储value
						store_info = {"key_name":key_name,"key_type":key_type,"key_value":key_value}
						query.mysql_2_redis(store_info)
						pass
					if (key_type == "list"):
						printzh("请输入要存储的键名")
						key_name = raw_input()
						printzh("请输入要导出的mysql数据库")
						db = raw_input()
						printzh("请输入要导出的mysql数据表")
						table = raw_input()
						printzh("请输入要导出的mysql字段")
						field = raw_input()
						printzh("确定导出mysql数据库"+db+"下的"+table+"表"+field+"字段到redis数据库"+key_name+"键值下，y确定，n取消")
						if (raw_input() == "y"):
							#存储列值
							store_info = {"key_name":key_name,"key_type":key_type,"db":db,"table":table,"field":field}
							query.mysql_2_redis(store_info)
							pass
						pass
					if (key_type == "set"):
						printzh("请输入要存储的键名")
						key_name = raw_input()
						printzh("请输入要导出的mysql数据库")
						db = raw_input()
						printzh("请输入要导出的mysql数据表")
						table = raw_input()
						printzh("请输入要导出的mysql字段")
						field = raw_input()
						printzh("注意set为去重集合，重复数据将只保留一项")
						printzh("确定导出mysql数据库"+db+"下的"+table+"表"+field+"字段到redis数据库"+key_name+"键值下，y确定，n取消")
						if (raw_input() == "y"):
							#存储列值
							store_info = {"key_name":key_name,"key_type":key_type,"db":db,"table":table,"field":field}
							query.mysql_2_redis(store_info)
							pass
						pass
					if (key_type == "zset"):
						printzh("请输入要存储的键名")
						key_name = raw_input()
						printzh("请输入要导出的mysql数据库")
						db = raw_input()
						printzh("请输入要导出的mysql数据表")
						table = raw_input()
						printzh("请输入要导出的mysql字段")
						field = raw_input()
						printzh("请输入要导出为分数的mysql字段，注意只能为数字")
						score = raw_input()
						printzh("注意zset为去重集合，重复数据将只保留一项,分数项可以重复")
						printzh("确定导出mysql数据库"+db+"下的"+table+"表"+field+"字段到redis数据库"+key_name+"键值下，y确定，n取消")
						if (raw_input() == "y"):
							#存储列值
							store_info = {"key_name":key_name,"key_type":key_type,"db":db,"table":table,"field":field,"score":score}
							query.mysql_2_redis(store_info)
							pass
						pass
					if (key_type == "hash"):
						printzh("请输入要存储的键名")
						key_name = raw_input()
						printzh("请输入要导出的mysql数据库")
						db = raw_input()
						printzh("请输入要导出的mysql数据表")
						table = raw_input()
						printzh("导出数据将以"+key_name+"：id作为hash键名，字段名为hash字段键名，字段最为hash字段键值，以"+key_name+"为set键名，"+key_name+"：id作为set键值")
						printzh("确定导出mysql数据库"+db+"下的"+table+"表到hash表中，y确定，n取消")
						if (raw_input() == "y"):
							#存储表值
							store_info = {"key_name":key_name,"key_type":key_type,"db":db,"table":table}
							query.mysql_2_redis(store_info)
							pass
						pass
					pass
				if (cmd_a3 == "2"):
					#A32redis导入mysql
					printzh("请选择要导出的键值")
					key_name = raw_input()
					
					query.redis_2_mysql()
					pass
				if (cmd_a3 == "3"):
					#A35redis导入json
					query.redis_2_json()
					pass
				if (cmd_a3 == "4"):
					#A36json导入redis
					query.json_2_redis()
					pass
				if (cmd_a3 == "5"):
					#A37退出
					break
					pass
				pass
			pass
		if (cmd_a == "4"):
			#A4帮助
			pass
		if (cmd_a == "5"):
			#A5退出
			break
			pass
	pass