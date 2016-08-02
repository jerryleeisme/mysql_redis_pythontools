#coding=utf-8
#中文编码必备否则编译时即出错

#中文输出处理
def printzh(zh_text):
	print (zh_text).decode('utf-8').encode('gbk')
	pass

#1主界面，第一屏欢迎界面
def welcome_view():
	printzh("A1连接配置")
	printzh("A2查询工具")
	printzh("A3导入导出工具")
	printzh("A4帮助")
	printzh("A5退出")
	pass

#A1连接配置
def set_view():
	printzh("A11mysql连接配置")
	printzh("A12redis连接配置")
	printzh("A13csv连接配置")
	printzh("A14json连接配置")
	printzh("A15配置信息输出")
	printzh("A16退出")
	pass

#A11mysql连接配置
def set_mysql_view():
	printzh("A111mysql数据库IP地址")
	printzh("A112mysql数据库端口")
	printzh("A113mysql数据库连接账号")
	printzh("A114mysql数据库连接密码")
	printzh("A115测试连接")
	printzh("A116退出")
	pass

#A12redis连接配置
def set_redis_view():
	printzh("A121redis数据库IP地址")
	printzh("A122redis数据库端口")
	printzh("A123redis数据库连接密码")
	printzh("A124测试连接")
	printzh("A125退出")
	pass

#A13csv连接配置
def set_csv_view():
	printzh("A131文件地址")
	printzh("A132测试连接")
	printzh("A133退出")
	pass

#A14json连接配置
def set_json_view():
	printzh("A141文件地址")
	printzh("A142测试连接")
	printzh("A143退出")
	pass

#A2查询工具
def query_view():
	printzh("A21mysql查询")
	printzh("A22redis查询")
	printzh("A23csv查询")
	printzh("A24json查询")
	printzh("A25退出")
	pass

#A21mysql查询
def query_mysql_view():
	printzh("A211显示数据库")
	printzh("A212显示数据表")
	printzh("A213显示表内容")
	printzh("A214清空表内容")
	printzh("A215退出")
	pass

#A22redis查询
def query_redis_view():
	printzh("A221列出键名")
	printzh("A222查询键名")
	printzh("A223清空键名")
	printzh("A224退出")
	pass

#A23csv查询
def query_csv_view():
	printzh("A231输出")
	printzh("A232清空")
	printzh("A233退出")
	pass

#A24json查询
def query_json_view():
	printzh("A241输出")
	printzh("A242清空")
	printzh("A243退出")
	pass

#A3导入导出工具
def import_view():
	printzh("A31mysql导入redis")
	printzh("A32redis导入mysql")
	printzh("A33redis导入json")
	printzh("A34json导入redis")
	printzh("A35退出")
	pass

#A4帮助
def help():
	printzh("A41配置操作")
	printzh("A42查询操作")
	printzh("A43导入操作")
	printzh("A44退出")
	pass

#A41配置操作
def help_set():
	printzh("")
	printzh("退出")
	pass

#A42查询操作
def help_query():
	printzh("")
	printzh("退出")
	pass

#A43导入操作
def help_import():
	printzh("")
	printzh("退出")
	pass