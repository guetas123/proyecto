def add_place(place):
	with open("bb.txt", "w") as file:
		file.write("Destino: " + place)
		file.close()

def add_date(date):
	with open("bb.txt", "a") as file:
		file.write('\n' + "Fecha: " + date)
		file.close()

def add_name(name):
	with open("bb.txt", "a") as file:
		file.write('\n' + "Nombre: " + name)
		file.close()

def return_reservation():
	with open("bb.txt", "r") as file:
		reservation = file.readline() + file.readline() + file.readline()

	return reservation