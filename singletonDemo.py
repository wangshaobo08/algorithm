class Singleton:
	_instance = None

	def singleton(cls,*args,**kargs):
		if not cls._instance:
			cls._instance = super(Singleton,cls).__new__(cls,*args,*kagrs)
		return cls._instance
