import string
def get_response(l):
	#Aqui reserva la fecha y pide el nombre
    """
    This function returns a definition based on a query, in this case the function
    will return a definition as an answer
    :return: String with the answer
    """
    stopwords = ['en','la','fecha','el']

    sentence= l
    tokens = sentence.split(' ')
    clean_token=[]
    for token in tokens:
    	if all(char in set(string.punctuation) for char in token):
    		continue

    	token= token.lower()
    	token = token.strip()
    	if token in stopwords:
    		continue
    	clean_token.append(token)

    temp = []
    temp.append(' '.join(clean_token))
    token = clean_token[0]


    with open("bb.txt", "w") as file:

        file.write('\n' + token)
        file.close()

    return "A que nombre desea la reservacion?"