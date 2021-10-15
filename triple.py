def tripler(func):
	def decor(*agrs):
			func(*args)
			func(*args)
			func(*args)
	return decor