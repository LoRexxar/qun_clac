# coding=utf-8

def main():
	"""
	本代码用于瞎jb计算群地位积分
	"""
	__point__ = 0
	__version__ = 0.2
	__floatroduction__ = """        
		  ___                     _            
		 / _ \ _   _ _ __     ___| | __ _  ___ 
		| | | | | | | '_ \   / __| |/ _` |/ __|
		| |_| | |_| | | | | | (__| | (_| | (__ 
		 \__\_\\__,_|_| |_|  \___|_|\__,_|\___| v{version}


		本代码用于瞎jb计算群地位积分

	""".format(version = __version__)

	prfloat(__floatroduction__)


	base_shouru = 8572
	base_jidian = 3.5
	base_caichan = 2618181
	base_dianzi = 20000

	username = input("Username: ")

	prfloat("Hello {username}, Welcome to Qun clac".format(username=username))
	prfloat("下面正式进入群积分计算")
	prfloat("本计算规则分为生活标准指数、感情生活指数，基准分为100，不设上限")

	shouru = input("你的月收入是多少(人民币元): ")
	shouru_point = float(shouru)/base_shouru*0.4*40
	__point__+=shouru_point

	if float(shouru) == 0:
		jidian = input("如果没有月收入，那么你上一次考试综合绩点为(0-5): ")
		jidian_point = float(jidian)/base_jidian*0.4*40
		__point__+=jidian_point


	caichan = input("你的财产总值约为多少(人民币元): ")
	if float(caichan) == 0:
		prfloat("别骗自己了，你的财产总值不可能是0")
		caichan = input("你的财产总值约为多少(人民币元): ")
	caichan_point = float(caichan)/base_caichan*0.3*40
	__point__+=caichan_point

	prfloat("你居住在几线城市?(1-5): ")
	cont = input("北上广深为1线，杭州为2线")
	if float(cont) not in [1,2,3,4,5]:
		prfloat("你在搞什么??? 好好输入!")
		cont = input("你居住在几线城市?(1-5): ")

	if float(cont) == 1:
		__point__+=6
	elif 2<=float(cont)<=3:
		__point__+=(10-((float(cont)-2)*2))
	elif 4<=float(cont)<=5:
		__point__+=(10-((float(cont)-1)*2))
	else:
		prfloat("发生了什么????")

	dianzi = input("你的电子玩具约为多少(人民币元):")
	if float(dianzi) == 0:
		prfloat("别骗自己了，你的财产总值不可能是0")
		dianzi = input("你的电子玩具约为多少(人民币元):")
	dianzi_point = float(dianzi)/base_dianzi*0.3*40
	__point__+=dianzi_point

	prfloat("你的生活标准指数为{point}".format(point = __point__))

	age = input("你今年多少岁了(周岁)? ")
	if 0>float(age) or float(age)>60:
		prfloat("本计算器不敢计算比0岁小或超过60岁的，再见")
		exit(0)
	age_point =  -0.016*float(age)*float(age) + 0.8*float(age)
	__point__+=age_point


	years = input("从大学起算，这是你第几年上学？")
	if 0>float(years) or float(years)>12:
		prfloat("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		years = input("从大学起算，这是你第几年上学？")

	years_point = float(years)
	__point__+=years_point

	is_biye = input("你毕业了吗?(1 or 0): ")
	if float(is_biye) not in [1,0]:
		prfloat("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		is_biye = input("你毕业了吗?(1 or 0): ")
	if float(is_biye):
		__point__+=2

	is_cmu = input("你是在cmu上学吗?(1 or 0): ")
	if float(is_cmu) not in [1,0]:
		prfloat("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		is_cmu = input("你是在cmu上学吗?(1 or 0): ")
	if float(is_cmu):
		__point__+=2

	have_meizi = input("你有妹子吗?(1 or 0): ")
	if float(have_meizi) not in [1,0]:
		prfloat("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		have_meizi = input("你有妹子吗?(1 or 0): ")
	if float(have_meizi):
		__point__+=10


		love_point = input("感情稳定吗?(1-10): ")
		if float(love_point)<1 or float(love_point)>10:
			prfloat("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
			love_point = input("感情稳定吗?(1-10): ")
		__point__ += float(love_point)


	have_time = input("自由支配时间占比怎么样?(1-10): ")
	if float(have_time)<1 or float(have_time)>10:
		prfloat("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		have_time = input("自由支配时间占比怎么样?(1-10): ")
	__point__ += float(have_time)


	have_pet = input("你有宠物吗?(1 or 0): ")
	if float(have_pet) not in [1,0]:
		prfloat("你再瞎填我就掀桌子了啊，(╯‵□′)╯︵┻━┻")
		have_pet = input("你有宠物吗?(1 or 0): ")
	if float(have_pet):
		__point__+=10



	prfloat("恭喜你，你的群地位指数为{point}".format(point = __point__))



if __name__ == '__main__':
    main()