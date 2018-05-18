import string
def get_response(l):
	#Aqui reserva el nombre y se finaliza
    """
    This function returns a definition based on a query, in this case the function
    will return a definition as an answer
    :return: String with the answer
    """
    stopwords = ['a','nombre','de']

    sentence= l
    tokens = sentence.split(' ')
    clean_token=[]
    for token in tokens:
    	if all(char in set(string.punctuation) for char in token):
    		continue
    	if token.isdigit():
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

    with open("bb.txt", "r") as file:
        an= "DESTINO: "+ file.readline() + "FECHA: "+ file.readline()+" NOMBRE: "+file.readline()
    return an