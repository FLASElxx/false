print('are you ok to play?')
print('play:1 no:0')
b=int(input('tell me what you choose:'))
if b==1:
	print('现在开始')
	print('请等待一会')
	print('你想玩哪一个游戏？')
	print('daan:答案之书 cai:猜数字 7:jump7 biao:表白')
	c=input('please choose:')
	if c=='daan':
		print('wait')
		print('sorry,答案之书目前只支持一个问题，您要开始吗？')
		f=input(' ')
		if f=='yes':
		    print('问题是：为毛接吻时要闭眼？')
		    print('hhhh/n/thhhhh/n/thhhhhh/n/thhhhhhhhh/n/thhhhhhh/n/thhhhhhhh/n/thhhhhhh/n/thhhh/n/thhhhh/n/thhhhhh/n/thhhhhhhhh/n/thhhhhhh/n/thhhhhhhh/n/thhhhhhh')
		    print('因为不闭眼怎么把你幻想成别人。')
	elif c=='cai':	
		print('one two play')
		d=int(input('please enter a number'))
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		print('wait')
		e=int(input('please guess a number:'))
		if d==e:
			print('you are right')
		elif d>e:
			print('too low')
			e=int(input('please guess a number::'))
		elif d<e:
			print('too high')
			e=int(input('please guess a number::'))
		if d==e:
			print('you are right')
		elif d>e:
			print('too low')
			e=int(input('please guess a number::'))
		elif d<e:
			print('too high')
			e=int(input('please guess a number::'))
		if d==e:
			print('you are right')
		elif d>e:
			print('too low')
			e=int(input('please guess a number::'))
		elif d<e:
			print('too high')
			e=int(input('please guess a number::'))
		if d==e:
			print('you are right')
		elif d>e:
			print('too low')
			e=int(input('please guess a number::'))
		elif d<e:
			print('too high')
			e=int(input('please guess a number::'))
		if d==e:
			print('you are right')
		elif d>e:
			print('too low')
			e=int(input('please guess a number::'))
		elif d<e:
			print('too high')
			e=int(input('please guess a number::'))
		if d==e:
			print('you are right')
		elif d>e:
			print('too low')
			e=int(input('please guess a number::'))
		elif d<e:
			print('too high')
			e=int(input('please guess a number::'))
		if d==e:
			print('you are right')
		elif d>e:
			print('too low')
			e=int(input('please guess a number::'))
		elif d<e:
			print('too high')
			e=int(input('please guess a number::'))
		if d==e:
			print('you are right')
		elif d>e:
			print('too low')
			e=int(input('please guess a number::'))
		elif d<e:
			print('too high')
			e=int(input('please guess a number::'))
		if d==e:
			print('you are right')
		elif d>e:
			print('too low')
			e=int(input('please guess a number:'))
		elif d<e:
			print('too high')
			e=int(input('please guess a number::'))
		if d==e:
			print('you are right')
		elif d>e:
			print('too low')
			e=int(input('please guess a number::'))
		elif d<e:
			print('too high')
			e=int(input('please guess a number:'))			
	elif c=='7':
		print('本游戏大概是这样的，输入一个数字，各位以内，在1-100内，所有包含该数字的数字都不会出现')
		h=0
		g=int(input('请输入数字:'))
		while h<100:
			h+=1
			if h//10==g:
				continue
			elif h%10==0:
				continue
			elif h%10==g:
				continue
			print(h)
			print('ok very ok')
		p=input('is very good')
	elif c=='biao':
		print('在下面输入名字，和你思恋他/她的天数，哈哈哈哈自动重复520次')#李鑫鑫倾情打造
		y=input('姓名：')
		u=input('天数：')
		for n in range(1,521):
			print(y+'我真真真喜欢你'+u+'天了,'+'我每天都对你日思夜想，和我处cp好不好！！！！！')
		r=int(input('按1有惊喜:'))
		if r==1:
			for n in range(1,521):
				print('我喜欢你的第{}'.format(n)+'天，'+'我爱你，'+y+'!')	
		
		
		
		
		
		
elif b==0:
	print('goodbay')
	print('欢迎下次再来')#2020.3.7
	
