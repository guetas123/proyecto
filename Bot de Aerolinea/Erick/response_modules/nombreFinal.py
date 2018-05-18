import string
def get_response(l):
	#Aqui reserva el nombre y se finaliza
    """
    This function returns a definition based on a query, in this case the function
    will return a definition as an answer
    :return: String with the answer
    """
    stopwords = ['a', 'nombre', 'de', 'al', 'A', 'Nombre', 'De', 'Al']

    sentence= l
    tokens = sentence.split(' ')
    clean_token=[]
    for token in tokens:
    	if all(char in set(string.punctuation) for char in token):
    		continue
    	if token.isdigit():
    		continue
    	#token= token.lower()
    	token = token.strip()
    	if token in stopwords:
    		continue
    	clean_token.append(token)

    temp = []
    temp.append(' '.join(clean_token))
    token1 = ""

    for t in clean_token:
    	token1 =token1 + str(t) + " "

    return "Reservacion a nombre de "+token1+"lista. Gracias."