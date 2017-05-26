class analisadorLexico():


	def ehVariavel(self, palavra, palavra1):
		if(palavra == "inteiro"):
			return palavra1
		else:
			return False	

	def ehNumero(self, palavra):
		try: 
			palavra = int(palavra)
			return palavra
		except ValueError:	
			return False

	def ehPrint(self, palavra):
		if(palavra == "imprimir"):
			return "print"
		else:
			return False

	def ehIgual(self, palavra):
		if(palavra == "="):
			return "="
		else:
			return False

	def analisa(self):
		entrada = open("inteiro.txt", "r")
		codigo = entrada.read()
		lista = codigo.split()
		saida = open("saida.py", "w")
		linhaCode = ""
		codeOpt = ""
		print(lista)

		for i in range(0, len(lista)-1):
			if(self.ehVariavel(lista[i], lista[i+1]) != False):
				linhaCode = lista[i]
			elif(self.ehNumero(lista[i]) != False):
				linhaCode = lista[i]
			elif(self.ehPrint(lista[i]) != False):
				linhaCode = self.ehPrint(lista[i])
			elif(self.ehIgual(lista[i]) != False):
				linhaCode = self.ehIgual(lista[i])
			codeOpt += linhaCode + "\n"

		saida.write(codeOpt)
		entrada.close()
		saida.close()


teste = analisadorLexico()
teste.analisa()