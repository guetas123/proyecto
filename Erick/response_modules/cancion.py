import string
def get_response(l):
    """
    This function returns a definition based on a query, in this case the function
    will return a definition as an answer
    :return: String with the answer
    """
    stopwords = ['Puedes', 'poner', 'la', 'cancion']

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

    return "Reproduciendo cancion "+str(clean_token)+"..."
