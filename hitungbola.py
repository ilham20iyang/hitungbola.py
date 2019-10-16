import bola
def main():

	r = 50
	
	print(" bola")


	luasbola = bola.luasbola(r)

	print("Luas bola dari jari-jari =",r,"adalah", luasbola)

	print(150*"=")

	volumeBola = bola.volumeBola(r)

	print("Luas bola dari jari-jari =",r,"adalah", volumeBola)

	print(150*"=")

	profil = bola.biodata("ilham","1829141005","B","teknik")



if __name__=="__main__":
	main()
