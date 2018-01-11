# coding=utf-8

def main():
	"""
	本代码用于瞎jb计算群地位积分
	"""
	__point__ = 0
	__version__ = 0.2
	__introduction__ = """        
		  ___                     _            
		 / _ \ _   _ _ __     ___| | __ _  ___ 
		| | | | | | | '_ \   / __| |/ _` |/ __|
		| |_| | |_| | | | | | (__| | (_| | (__ 
		 \__\_\\__,_|_| |_|  \___|_|\__,_|\___| v{version}


		本代码用于瞎jb计算群地位积分

	""".format(version = __version__)

	print(__introduction__)


	base_shouru = 8572
	base_jidian = 3.5
	base_caichan = 2618181
	base_dianzi = 20000

	username = input("Username: ")

	print("Hello {username}, Welcome to Qun clac".format(username=username))
	print("下面正式进入群积分计算")
	print("本计算规则分为生活标准指数、感情生活指数，基准分为100，不设上限")

	shouru = input("你的月收入是多少(人民币元): ")
	shouru_point = int(shouru)/base_shouru*0.4*40
	__point__+=shouru_point

	if int(shouru) == 0:
		jidian = input("如果没有月收入，那么你上一次考试综合绩点为(0-5): ")
		jidian_point = int(jidian)/base_jidian*0.4*40
		__point__+=jidian_point


	caichan = input("你的财产总值约为多少(人民币元): ")
	if int(caichan) == 0:
		print("别骗自己了，你的财产总值不可能是0")
		caichan = input("你的财产总值约为多少(人民币元): ")
	caichan_point = int(caichan)/base_caichan*0.3*40
	__point__+=caichan_point

	print("你居住在几线城市?(1-5): ")
	cont = input("北上广深为1线，杭州为2线")
	if int(cont) not in [1,2,3,4,5]:
		print("你在搞什么??? 好好输入!")
		cont = input("你居住在几线城市?(1-5): ")

	if int(cont) == 1:
		__point__+=6
	elif 2<=int(cont)<=3:
		__point__+=(10-((int(cont)-2)*2))
	elif 4<=int(cont)<=5:
		__point__+=(10-((int(cont)-1)*2))
	else:
		print("发生了什么????")

	dianzi = input("你的电子玩具约为多少(人民币元):")
	if int(dianzi) == 0:
		print("别骗自己了，你的财产总值不可能是0")
		dianzi = input("你的电子玩具约为多少(人民币元):")
	dianzi_point = int(dianzi)/base_dianzi*0.3*40
	__point__+=dianzi_point

	print("你的生活标准指数为{point}".format(point = __point__))

	age = input("你今年多少岁了(周岁)? ")
	if 0>int(age) or int(age)>60:
		print("本计算器不敢计算比0岁小或超过60岁的，再见")
		exit(0)
	age_point =  -0.016*int(age)*int(age) + 0.8*int(age)
	__point__+=age_point


	years = input("从大学起算，这是你第几年上学？")
	if 0>int(years) or int(years)>12:
		print("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		years = input("从大学起算，这是你第几年上学？")

	years_point = int(years)
	__point__+=years_point

	is_biye = input("你毕业了吗?(1 or 0): ")
	if int(is_biye) not in [1,0]:
		print("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		is_biye = input("你毕业了吗?(1 or 0): ")
	if int(is_biye):
		__point__+=2

	is_cmu = input("你是在cmu上学吗?(1 or 0): ")
	if int(is_cmu) not in [1,0]:
		print("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		is_cmu = input("你是在cmu上学吗?(1 or 0): ")
	if int(is_cmu):
		__point__+=2

	have_meizi = input("你有妹子吗?(1 or 0): ")
	if int(have_meizi) not in [1,0]:
		print("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		have_meizi = input("你有妹子吗?(1 or 0): ")
	if int(have_meizi):
		__point__+=10


		love_point = input("感情稳定吗?(1-10): ")
		if int(love_point)<1 or int(love_point)>10:
			print("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
			love_point = input("感情稳定吗?(1-10): ")
		__point__ += int(love_point)


	have_time = input("自由支配时间占比怎么样?(1-10): ")
	if int(have_time)<1 or int(have_time)>10:
		print("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		have_time = input("自由支配时间占比怎么样?(1-10): ")
	__point__ += int(have_time)


	have_pet = input("你有宠物吗?(1 or 0): ")
	if int(have_pet) not in [1,0]:
		print("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		have_pet = input("你有宠物吗?(1 or 0): ")
	if int(have_pet):
		__point__+=10



	print("恭喜你，你的群地位指数为{point}".format(point = __point__))



if __name__ == '__main__':
    main()