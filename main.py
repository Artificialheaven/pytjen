import traceback


temp = ''							# 代码缓冲区
func_list = []						# 函数列表
global_var_table = {}				# 全局变量列表, 每次都要继承
while True:  						# 启动循环
	try:
		cmd = input(">>>")   			# 请求输入
		if cmd.startswith('def'):		# 创建函数
			while True:
				if cmd == '':				# 函数结束
					d, _d = {}, {}
					exec(temp, global_var_table)
					break
				else:
					temp = temp + '\n' + cmd
					cmd = input('...')
		else:
			exec(cmd, global_var_table)  	# 运行指令
	except Exception as e:
		traceback.print_exc()			# 获取全部报错
