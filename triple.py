def tripler(func):
	def decor(*agrs):
			func(*agrs)
			func(*agrs)
			func(*agrs)
	return decor