name = input('请输入你的姓名：')
print('你好！'+name)
user_gender_input = False
while not user_gender_input:
	gender = input('请输入你的性别(F/M)：')
	if gender.upper() == 'F' :
		print('你是萌妹子')
		user_gender_input = True
	elif gender.upper() == 'M' :
		print('你是糙汉子')
		user_gender_input = True
	else :
		print('输入错误！')
birth = input('请输入你的出生年：')
if birth.isdigit():
	digit = int(birth)
	# 导入time模块
	import time
	time = time.strftime("%Y")
	# 转换为int类型
	int_time = int(time)
	print("你的年龄是：",(int_time-digit),"周岁")
else:
	print('输入错误！')
school = input('请输入你的学校：')
print('你的学校是',school)
constellation = input('请输入你的星座：')
print("***你今年的运势***")
print(name,"!","你是个",int_time-digit,"岁的",gender,"你运气不错哦，我们下次见！")