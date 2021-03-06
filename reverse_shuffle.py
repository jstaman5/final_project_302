# Builds our working data set

import random
import csv
from r_cube import solver_helpers as sh

from r_cube.template_class import rubiks_cube

# Performs reverse shuffle algorithm/ optimizes the reverse moves
# Returns flat string, solution, and current state of rubiks cube
def reverse_shuffle(rotations):	
	
	rc    = rubiks_cube()	
	mvs   = []
	names = sh.names_of_moves() 

	for i in range(0, rotations):
		check = random.randint(1, 12)
	
		if (check == 1):
			rc.front()
			mvs.append(0)

		elif (check == 2):
			rc.front_prime()
			mvs.append(1)

		elif (check == 3):	
			rc.back()	
			mvs.append(2)

		elif (check == 4):
			rc.back_prime()
			mvs.append(3)
					
		elif (check == 5):		
			rc.up()
			mvs.append(4)

		elif (check == 6):
			rc.up_prime()		
			mvs.append(5)

		elif (check == 7):
			rc.down()		
			mvs.append(6)

		elif (check == 8):
			rc.down_prime()		
			mvs.append(7)

		elif (check == 9):
			rc.left()		
			mvs.append(8)

		elif (check == 10):
			rc.left_prime()		
			mvs.append(9)

		elif (check == 11):		
			rc.right()
			mvs.append(10)

		elif (check == 12):		
			rc.right_prime()
			mvs.append(11)
	
	j = rotations - 1			
	solution = []

	while (j >= 0):
		# Check if same move has been performed 4 times before
		curr_ind  = mvs[j]
		curr_name = names[ curr_ind ]
		comp_name = sh.counter_move( curr_name ) 
		comp_ind  = names.index( comp_name )

		temp = j - 1
		same_count = 0
		while (temp >= 0 and temp > j - 4):
			if (curr_ind == mvs[temp] ):
				same_count += 1
				temp -= 1
			else:
				break	
	
		# Four consecutive same moves is redudant
		if (same_count == 3):
			j -= 4
			continue
		
		# Three consecutive same moves is compliment move
		elif (same_count == 2):
			solution.append(curr_name)
			j -= 3 

		# Check if next two are consec. compliments
		elif ((same_count == 1 and j > 2) and (mvs[ j - 2 ] == mvs[j - 3]) and (mvs[j - 2] == comp_ind)): 
			j -= 4 

		# If two consecutive moves are compliments
		elif (( j != 0 ) and mvs[j - 1] == comp_ind ):
			if (j == 1):
				break
			else:
				j -= 2
		else:
			solution.append(comp_name)
			j -= 1
	
	return [ sh.flatten_faces(rc), solution, rc ]
			


# Takes the solution and performs it on the cube
def solve_back(sol, rc):

	for i in range(0, len(sol)):
		temp = sh.get_move(rc, sol[i])
		temp()
	
	print(sh.flatten_faces(rc))

	return rc

# Makes each move when shuffle number == 1
def first_layer_moves(check, rc):
	if (check == 0):
		rc.front()

	elif (check == 1):
		rc.front_prime()

	elif (check == 2):	
		rc.back()	

	elif (check == 3):
		rc.back_prime()
					
	elif (check == 4):		
		rc.up()

	elif (check == 5):
		rc.up_prime()		

	elif (check == 6):
		rc.down()		

	elif (check == 7):
		rc.down_prime()		

	elif (check == 8):
		rc.left()		

	elif (check == 9):
		rc.left_prime()		

	elif (check == 10):		
		rc.right()

	elif (check == 11):		
		rc.right_prime()

	names = sh.names_of_moves()
	n     = names[check]

	return [ sh.flatten_faces(rc), convert_sol(n, 1), rc ]

def main(f_name, rot, snum):
	
	sol = []
	r   = rubiks_cube()

	with open("cnn_solver/" + f_name, 'w', newline = '') as file:
		
		writer = csv.writer(file)
		writer.writerow( ['state', 'move'] )

		for i in range(0, snum):
			state, sol, r = reverse_shuffle(rot)
			
			while ( len(sol) != 0 ) :
				s_ind     = sol.pop(0)
				s_ind_str = sh.convert_sol(s_ind, into_num = 1 )
				state     = sh.flatten_faces(r)
				into      = [ state, s_ind_str ]
				writer.writerow( into )
				sh.get_move( r, s_ind )()
			
			state     = sh.flatten_faces(r) # Gets the solved state
			into      = [ state, 12 ]      # Inputs '0' for move on solved state
			writer.writerow( into )      
			r.reset()                       # Reset cube for good measure
				
			

# Main execution
rot  = input("How many rotations per shuffle? ")
rot  = int(rot)
snum = input("How many shuffles? ")
snum = int(snum)
fn   = input("Name of output file? ")
main(fn, rot, snum)


