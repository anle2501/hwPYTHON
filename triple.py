def tripler(func):
	def inner(*agrs):
			func(*args)
			func(*args)
			func(*args)
	return inner