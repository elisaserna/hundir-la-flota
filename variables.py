'''
variables fijas
'''
tamano_tablero=10
barco1=[1,1,1,1]
barco2=[2,2,2]
barco3=[3,3]
barco4=[4]
total_barcos = barco1 + barco2 + barco3 + barco4
total_casillas_barcos = sum(total_barcos)



'''
Simbolos del tablero
'''
agua = "~"
barco = "*"
disparo_fallado = "·"
barco_disparado = "X"

'''
Mensajes para el jugador 
'''
inicio= "Bienvenid@ a Hundir la Flota"
instrucciones ="selecciona las casillas donde quiera poner sus barcos. " \
"Tiene cuatro barcos del tamaño de una casilla, tres del tamaño de dos casillas, dos del tamaño de tres casillas y uno del tamaño de cuatro casillas"
acertado= "Has acertado, puedes volver a disparar"
fallado= "No has acertado, espera a tu turno para volver a disparar"
ganado= "Enhorabuena, has ganado"
perdido = "Has perdido la partida. Vuelve a jugar e intentalo de nuevo"
