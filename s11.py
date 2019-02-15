class student(object):
	def get_score(self):
		return self.score
	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must ba an integer!')
		if value<0 or value>100:
			raise ValueError('score must between 0~100!')
		self.score = value
# a = student()
# a.set_score(56)
# print(a.get_score())
class Student(object):

	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		elif value<0 or value>100:
			raise ValueError('score must between 0~100!')
		self._score = value

a = Student()
a.score = 99
print(a.score)

