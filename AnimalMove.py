# dog_x = 0
# cat_x = 0

# def dog_move():
# 	global dog_x
# 	dog_x = dog_x + 10

# def cat_move():
# 	global cat_x
# 	cat_x = cat_x + 10

# user_input = input()
# if user_input == 'move':
# 	print('dog{},cat{}'.format(dog_x,cat_x))
# 	dog_move()
# 	cat_move()
# 	print('dog{},cat{}'.format(dog_x,cat_x))
class Animal(): #定义一个动物类

	def __init__(self): #定义原本的坐标
		self.x = 0

	def move(self): #定义增加的坐标
		self.x += 10

dog = Animal() #类实例化的对象
cat = Animal()

user_input = input()

if user_input == 'move':
	dog.move() #执行Animal类的move方法
	cat.move()
	print('Dog position',dog.x)
	print('Cat position',cat.x)