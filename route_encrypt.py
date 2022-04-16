import math
import sys

def route_encrypt(plain_text="", step_size=4):
	"""
		 E merr plain tekstin si input dhe e formon tekstin e enkriptuar si output
		Implementimi sipas  route cipher
	"""

	idx = 0
	matrix_representation = []
	encrypted_text = ""

	# create a matrix from plain text with width = step_size
	for i in range(math.ceil(len(plain_text)/step_size)):
		matrix_row = []
		for j in range(step_size):
			if i*step_size+j < len(plain_text):
				matrix_row.append(plain_text[i*step_size+j])
			else:
				matrix_row.append("-")
		matrix_representation.append(matrix_row)

	matrix_width = len(matrix_representation[0])
	matrix_height = len(matrix_representation)
	allowed_depth = 0

	if matrix_width < matrix_height:
		allowed_depth = matrix_width // 2
	else:
		allowed_depth = matrix_height // 2

