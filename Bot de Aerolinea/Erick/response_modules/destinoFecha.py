import string
from reservation.add_reservation import *
def get_response(l):
	#Aqui reserva el destino del vuelo y despues pregunta por la fecha
    """
    This function returns a definition based on a query, in this case the function
    will return a definition as an answer
    :return: String with the answer
    """
    stopwords = ['quiero', 'ir', 'a', 'la', 'ciudad', 'de', 'Quiero', 'Ir', 'A', 'La', 'Ciudad', 'De']

    sentence= l
    tokens = sentence.split(' ')
    clean_token=[]
    for token in tokens:
    	if all(char in set(string.punctuation) for char in token):
    		continue
    	if token.isdigit():
    		continue
    	token = token.strip()
    	if token in stopwords:
    		continue
    	clean_token.append(token)

    temp = []
    temp.append(' '.join(clean_token))
    token = clean_token[0]

    add_place(token)
    
    return "En que fecha te gustaria volar a " + str(token) + "?"