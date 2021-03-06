# Backend implementation of cube functions
import random

# Move functions
# Named weirdly to avoid mixups in names of functions
#   in template_class
def cube_upp(self):
	rotate(self, "u", "cw")
def cube_upp_p(self):
	rotate(self, "u", "ccw")
def cube_ri(self):
	rotate(self, "r", "cw")
def cube_ri_p(self):
	rotate(self, "r", "ccw")
def cube_fr(self):
	rotate(self, "f", "cw")
def cube_fr_p(self):
	rotate(self, "f", "ccw")
def cube_do(self):
	rotate(self, "d", "cw")
def cube_do_p(self):
	rotate(self, "d", "ccw")
def cube_le(self):
	rotate(self, "l", "cw")
def cube_le_p(self):
	rotate(self, "l", "ccw")
def cube_ba(self):
	rotate(self, "b", "cw")
def cube_ba_p(self):
	rotate(self, "b", "ccw")


# Rotate a specific face of the cube
# option is either "ccw" or "cw"
def rotate(self, face, option):
	
	if ((option != "ccw") and  (option != "cw")):
		print("Wrong option")
		return -1
	
	# Decide which face will be turned
	if   (face == "u"):
		self.u = move_around(self.u, option)
	elif (face == "r"):
		self.r = move_around(self.r, option)
	elif (face == "f"):
		self.f = move_around(self.f, option)
	elif (face == "d"):
		self.d = move_around(self.d, option)
	elif (face == "l"):
		self.l = move_around(self.l, option)
	elif (face == "b"):
		self.b = move_around(self.b, option)

	if (option == "ccw"):	
		self = check_cube(self, face, "other")
	else:
		self = check_cube(self, face, "regular") 
	
	return self
	
# Helper function for the rotate
# Rotates spaces on one face in desired direction
def move_around(face, option):
	if (option == "cw"):
		temp = face[0][0]
		face[0][0] = face[1][0]
		face[1][0] = face[1][1]
		face[1][1] = face[0][1]
		face[0][1] = temp
	else:
		temp = face[0][0]
		face[0][0] = face[0][1]
		face[0][1] = face[1][1]
		face[1][1] = face[1][0]
		face[1][0] = temp
	
	return face
	
# Changes all the values around a rotated face after rotation
def check_cube(self, precedence, direction):

	# Need some math to determine which faces to turn
	# Convention based off of Rubiks Cube conventions found in documentation	

	# Back face
	if   (precedence == "b"):
		
		# To be rotated:
		#  1. Top of u
		#  2. Bottom of d
		#  3. Left of l
		#  4. Right of r

		if (direction == "regular"):
			for i in range(0, self.dim):
				temp_val = self.r[i][self.dim - 1]
				self.r[i][self.dim - 1] = self.d[self.dim - 1][self.dim - i - 1]
				self.d[self.dim - 1][self.dim - i - 1] = self.l[self.dim - i - 1][0]
				self.l[self.dim - i - 1][0] = self.u[0][i]
				self.u[0][i] = temp_val
			
		else:
			for i in range(0, self.dim):
				temp_val = self.r[i][self.dim - 1]
				self.r[i][self.dim - 1] = self.u[0][i]
				self.u[0][i] = self.l[self.dim - i - 1][0]
				self.l[self.dim - i - 1][0] = self.d[self.dim - 1][self.dim - i - 1]
				self.d[self.dim - 1][self.dim - i - 1] = temp_val
				

	# Front face
	elif (precedence == "f"):
		# To be rotated:	
		#  1. Bottom of u	
		#  2. Left of r
		#  3. Top of d
		#  4. Right of l

		if (direction == "regular"):
			for i in range(0, self.dim):
				temp_val = self.r[i][0]
				self.r[i][0] = self.u[self.dim - 1][i]
				self.u[self.dim - 1][i] = self.l[self.dim - i - 1][self.dim - 1]
				self.l[self.dim - i - 1][self.dim - 1] = self.d[0][self.dim - i - 1]
				self.d[0][self.dim - i - 1] = temp_val
		else:
			for i in range(0, self.dim):
				temp_val = self.r[i][0]
				self.r[i][0] = self.d[0][self.dim - i - 1]
				self.d[0][self.dim - i - 1] = self.l[self.dim - i - 1][self.dim - 1]
				self.l[self.dim - i - 1][self.dim - 1] = self.u[self.dim - 1][i]
				self.u[self.dim - 1][i] = temp_val

	# Left face
	elif (precedence == "l"):

		if (direction == "regular"):
			for i in range(0, self.dim):
				temp_val = self.u[i][0]
				self.u[i][0] = self.b[i][self.dim - 1]
				self.b[i][self.dim - 1] = self.d[self.dim - i - 1][0]
				self.d[self.dim - i - 1][0] = self.f[i][0]
				self.f[i][0] = temp_val

		else:
			for i in range(0, self.dim):
				temp_val = self.u[i][0]
				self.u[i][0] = self.f[i][0]
				self.f[i][0] = self.d[self.dim - i - 1][0]
				self.d[self.dim - i - 1][0] = self.b[i][self.dim - 1]
				self.b[i][self.dim - 1] = temp_val
				

	# Right face
	elif (precedence == "r"):

		if (direction == "regular"):
			for i in range(0, self.dim):
				temp_val = self.u[i][self.dim - 1]
				self.u[i][self.dim - 1] = self.f[i][self.dim - 1]
				self.f[i][self.dim - 1] = self.d[i][self.dim - 1]
				self.d[i][self.dim - 1] = self.b[self.dim - i - 1][0]
				self.b[self.dim - i - 1][0] = temp_val
			
		else:
			for i in range(0, self.dim):
				temp_val = self.u[i][self.dim - 1]
				self.u[i][self.dim - 1] = self.b[self.dim - i - 1][0]
				self.b[self.dim - i - 1][0] = self.d[i][self.dim - 1]
				self.d[i][self.dim - 1] = self.f[i][self.dim - 1]
				self.f[i][self.dim - 1] = temp_val
				
	# Upper face
	elif (precedence == "u"):

		# We're moving the top ccw
		if (direction == "regular"):	
			for i in range(0, self.dim):
				temp_val     = self.f[0][i]
				self.f[0][i] = self.r[0][i]
				self.r[0][i] = self.b[0][i]
				self.b[0][i] = self.l[0][i]
				self.l[0][i] = temp_val
		
		else: # We're moving the top cw
			for i in range(0, self.dim):
				temp_val     = self.f[0][i]
				self.f[0][i] = self.l[0][i]
				self.l[0][i] = self.b[0][i]
				self.b[0][i] = self.r[0][i]
				self.r[0][i] = temp_val


	# Down face
	elif (precedence == "d"):
		ind = self.dim - 1
		
		if (direction == "regular"):	
			for i in range(0, self.dim):
				temp_val       = self.f[ind][i]
				self.f[ind][i] = self.l[ind][i]
				self.l[ind][i] = self.b[ind][i]
				self.b[ind][i] = self.r[ind][i]
				self.r[ind][i] = temp_val
		
		else:
			for i in range(0, self.dim):
				temp_val       = self.f[ind][i]
				self.f[ind][i] = self.r[ind][i]
				self.r[ind][i] = self.b[ind][i]
				self.b[ind][i] = self.l[ind][i]
				self.l[ind][i] = temp_val

		return self


# Shuffles the cube (calls random moves repeatedly)
def cube_shuffle(self, rotations):

	while(rotations > 0):

		check = random.randint(1, 12)

		if (check == 1):
			self.front()
		elif (check == 2):
			self.front_prime()
		elif (check == 3):
			self.back()
		elif (check == 4):
			self.back_prime()
		elif (check == 5):
			self.up()
		elif (check == 6):
			self.up_prime()
		elif (check == 7):
			self.down()
		elif (check == 8):
			self.down_prime()
		elif (check == 9):
			self.left()
		elif (check == 10):
			self.left_prime()
		elif (check == 11):
			self.right()
		elif (check == 12):
			self.right_prime()

		rotations -= 1

# Checks if the cube has been solved
def cube_if_solved(self):

	check = 1

	if(self.f[0][0] != self.f[0][1] or self.f[0][1] != self.f[1][0] or self.f[1][0] != self.f[1][1]) :
		check = 0
	

	if(self.b[0][0] != self.b[0][1] or self.b[0][1] != self.b[1][0] or self.b[1][0] != self.b[1][1]) :
		check = 0
	

	if(self.u[0][0] != self.u[0][1] or self.u[0][1] != self.u[1][0] or self.u[1][0] != self.u[1][1]) :
		check = 0
	

	if(self.d[0][0] != self.d[0][1] or self.d[0][1] != self.d[1][0] or self.d[1][0] != self.d[1][1]) :
		check = 0
	

	if(self.l[0][0] != self.l[0][1] or self.l[0][1] != self.l[1][0] or self.l[1][0] != self.l[1][1]) :
		check = 0
	

	if(self.r[0][0] != self.r[0][1] or self.r[0][1] != self.r[1][0] or self.r[1][0] != self.r[1][1]) :
		check = 0
	

	if(check == 1):
		#print("Solved")
		return 1
	else:
		#print("Not Solved")
		return 0

def cube_reset(self):
	
	self.f = [ ['r', 'r'], ['r', 'r'] ]
	self.b = [ ['o', 'o'], ['o', 'o'] ]
	self.u = [ ['w', 'w'], ['w', 'w'] ]
	self.d = [ ['y', 'y'], ['y', 'y'] ]
	self.l = [ ['g', 'g'], ['g', 'g'] ]
	self.r = [ ['b', 'b'], ['b', 'b'] ]	


