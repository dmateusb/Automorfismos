import itertools
import pprint
def automorfismos(vectores,edges):
	v=vectores
	graphOriginal=edges
	#Crea todas las posibles permutaciones de la lista de vectores
	permutaciones=list(itertools.permutations(v))
	automorfismos={}
	while permutaciones:
		g=graphOriginal[:]
		permutacion=permutaciones[-1]
		cont=0
		automorfismo=[]
		for edge in g:
			newEdge=[]
			for i in edge:
				position=i
				x=permutacion[position]
				#Inserta en el edge el nuevo valor, segun la permutación que esté utilizando
				newEdge.append(x)
				automorfismo.append(newEdge)
		#Compara que las listas sean iguales convirtiendolas en conjuntos
		if (set(tuple(edge) for edge in g)) == (set(tuple(edge) for edge in automorfismo)):
			automorfismos[permutacion]=g
		permutaciones.pop()
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(automorfismos)
automorfismos([0,1,2,3],[[0,1],[1,3],[3,2],[2,0]])
