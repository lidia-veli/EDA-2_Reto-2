# FUNCIONES
def comprobar_todos_suscriptores(n, a, q, lista_car):
    '''
    Función que comprueba si todos los suscriptres del canal han leído la publicación

    INPUT:--------------------------------
    - n (int): num. suscriptores del canal
    - a (int): num. inicial suscriptores en linea
    - q (int): num. notificaciones
    - lista_car (str): cadena de caracteres de las notificaciones de conxión y desconexión

    OUTPUT:--------------------------------
    YES, NO, MAYBE : str
    '''
        
    a_p = 0  # suscriptores que se añaden
    a_n = 0  # suscriptores que se quitan
    
    for i in range(q): # miramos cada caracter
        if n == (a + a_p - a_n):  # si en algun momento se llega al total de suscriptores del canal
            return 'YES'
        
        # si no, se sigue con la iteracion
        if lista_car[i] == '+':
            a_p += 1  # suscriptor se conecta
            #print('+1', (a + a_p - a_n))
        elif lista_car[i] == '-':
            a_n += 1  # suscriptor se desconecta
            #print('-1', (a + a_p - a_n))
        
    # cuando acaba de recorrer todos los caracteres
    if n == (a + a_p - a_n): # volvemos a comprobar si se llega al total de suscriptores del canal
        return 'YES'
    
    # si no
    if a_p >= (n-a):  # condicion que diferencia el MAYBE del NO
        return 'MAYBE'
    else:
        return 'NO'



# CODIGO EJECUTABLE-------------------------------------------------------------------------------------

t = int(input())  # numero casos de prueba

# desde la 2º linea, cada 2
for _ in range(1,t*2,2):
    # el primer input da los suscriptores
    n, a, q = input().split()
    n = int(n)  # num. suscriptores del canal
    a = int(a)  # num. inicial suscriptores en linea
    q = int(q)  # num. notificaciones

    # el segundo input da el flujo de suscriptores en linea
    lista_car = input()  # lista de caracteres

    print(comprobar_todos_suscriptores(n, a, q, lista_car))
