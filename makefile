
primero : Graph.png

Graph.png : grafica.py Data1.txt
	python grafica.py

Data1.txt : rk4
	./rk4 > Data1.txt

rk4 :
	c++ ejercicio1.cpp -o rk4

segundo: Graph2.png

Graph2.png : grafica2.py Data2.txt
	python grafica2.py

Data2.txt : rk4b
	./rk4b > Data2.txt

rk4b :
	c++ ejercicio2.cpp -o rk4b
