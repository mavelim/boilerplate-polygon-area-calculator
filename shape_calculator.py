class Rectangle:
	name= "Rectangle"
	def __init__(self,width,height):
		
		self.width=width
		self.height=height

	def __str__(self):
		return "%s(width=%d, height=%d)" %(self.name,self.width,self.height)
	
	def set_width(self,width):
		self.width=width

	def set_height(self,height):
		self.height=height

	def get_area(self):
		return self.width * self.height
		
	def get_perimeter(self):
		return 2 * self.width + 2 *self.height
	def get_diagonal(self):
		return (self.width ** 2 + self.height ** 2)**0.5
	def get_picture(self):
		result=""
		if self.width >50 or self.height>50:
			result="Too big for picture."
		else:
			for i in range(self.height):
				for j in range(self.width):
					result += "*"
				result += "\n"

		return result
	
	def get_amount_inside(self,shape):
		return(self.width // shape.width)*(self.height // shape.height)

	

	





class Square(Rectangle):
	name = "Square"
	def __init__(self,lenght):
		self.width=lenght
		self.height=lenght

	def __str__(self):
		return "%s(side=%d)" %(self.name,self.width)

	def set_side(self,lenght):
		self.width=lenght
		self.height=lenght

	def set_height(self, lenght):
		self.set_side(lenght)
	
	def set_width(self, lenght):
		self.set_side(lenght)

