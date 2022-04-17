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

	#Krijimi i  matrices  nga plain teksti me gjatesi = step_size
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
		
# Këtu "i" tregon thellësinë në të cilën jemi në matricë
# Lexojmë matricën normale në formë spirale duke filluar nga këndi i sipërm djathtas
	for i in range(allowed_depth):

		# Duke zbritur në anën e djathtë
		for j in range(i, matrix_height-i-1):
			encrypted_text += matrix_representation[j][matrix_width-i-1]

		# Duke shkuar majtas në anën e poshtme
		for j in range(matrix_width-i-1, i, -1):
			encrypted_text += matrix_representation[matrix_height-i-1][j]

		# Duke u ngjitur në anën e majtë
		for j in range(matrix_height-i-1, i, -1):
			encrypted_text += matrix_representation[j][i]
			
		# Duke shkuar djathtas në anën e sipërme
		for j in range(i, matrix_width-i-1):
			encrypted_text += matrix_representation[i][j]


	return encrypted_text

def route_decrypt(cipher_text="", step_size=4):
	"""
	    Merr tekstin e shifruar si hyrje dhe prodhon tekst të thjeshtë si dalje
        Zbaton të kundërtën e teknikës së route cipher
		
	"""

	idx = 0
	plain_text = ""

	matrix_width = step_size
	matrix_height = math.ceil(len(cipher_text)/step_size)

	if matrix_width < matrix_height:
		allowed_depth = matrix_width // 2
	else:
		allowed_depth = matrix_height // 2

	plain_text_matrix = [[0 for i in range(matrix_width)] for j in range(matrix_height)]

    '''
    Variabla "i" tregon thellesine ne te cilen jemi ne matrice  
    Ne rastin e dekriptimit po rikrijojme matricen "matrix_representation" qe kemi perdorur ne funksionin per enkriptim
    Per dekriptim veprojme ne menyre te kundert me rastin e enkriptimit
    Vendosja e tekstit te enkriptuar ne matrice behet ne forme spirale, ndersa leximi per percaktimin e plain tekstit behet rresht per rresht
    '''
   
    for i in range(allowed_depth):

        # Drejtimi poshte - ana e djathte
        for j in range(i, matrix_height - i - 1):
            plain_text_matrix[j][matrix_width - i - 1] = cipher_text[idx]
            idx += 1

        # Drejtimi majtas - pjesa e poshtme e matrices
        for j in range(matrix_width - i - 1, i, -1):
            plain_text_matrix[matrix_height - i - 1][j] = cipher_text[idx]
            idx += 1

        # Drejtimi lart - ana e majte
        for j in range(matrix_height - i - 1, i, -1):
            plain_text_matrix[j][i] = cipher_text[idx]
            idx += 1

        # Drejtimi djathtas - pjesa e siperme e matrices
        for j in range(i, matrix_width - i - 1):
            plain_text_matrix[i][j] = cipher_text[idx]
            idx += 1

    # rikonstruktimi i mesazhit (plaintext) duke e lexuar matricen e formuar rresht per rresht
    for i in range(matrix_height):
        for j in range(matrix_width):
            plain_text += str(plain_text_matrix[i][j])

    return plain_text


cipher = route_encrypt(plain_text="TODAY WE ARE PRESENTING OUR CODE")
print("ENCRYPTED TEXT: ", cipher)

plain_text = route_decrypt(cipher_text=cipher)
print("DECRYPTED TEXT: ",plain_text)
