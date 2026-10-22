import random

def mostrarMenu():
  while True:
    print('----- Menu de juegos -----')
    print('1- Piedra, papel, tijeras')
    print('2- Ahorcado')
    print('3- Tres en raya')
    print('4- Blackjack')
    print('5- Salir')
    
    juego = int(input('Escoge un juego: '))

    match juego:
      case 1:
        piedraPapelTijeras()
      case 2:
        ahorcado()
      case 3:
        tresEnRaya()
      case 4:
        blackJack()
      case 5:
        break


def piedraPapelTijeras():
  print('---- PIEDRA - PAPEL - TIJERAS ----')

  puntosJugador = 0
  puntosRival = 0

  opciones = {1: 'Piedra', 2: 'Papel', 3: 'Tijeras'}

  while puntosJugador < 3 and puntosRival < 3:
    print('Escoge entre las siguientes opciones: ')
    for op in opciones:
      print(f'{op}- {opciones[op]}')

    try:
      opcionJugador = int(input(''))
      if opcionJugador not in opciones:
        print('Número inválido, escoge un número entre 1 y 3.')
        continue
    except ValueError:
      print('Introduce un número válido.')
      continue

    opcionRival = random.randint(1,3)

    print(f'Tu: {opciones[opcionJugador]} - Rival: {opciones[opcionRival]}')

    if opcionJugador == opcionRival:
      print(f'Empate. Marcador Tu: {puntosJugador} - Rival: {puntosRival}')
    elif (opcionJugador == 1 and opcionRival == 3) or (opcionJugador == 2 and opcionRival == 1) or (opcionJugador == 3 and opcionRival == 2):
      puntosJugador += 1
      print(f'Has ganado. Marcador Tu: {puntosJugador} - Rival: {puntosRival}')
    else: 
      puntosRival += 1
      print(f'Has perdido. Marcador Tu: {puntosJugador} - Rival: {puntosRival}')

  if puntosJugador >= 3:
    mensajeVictoria()
  elif puntosRival >= 3:
    mensajeDerrota()


def ahorcado():
  print('---- AHORCADO ----')

  palabras = ["COHETE", "ISLA", "VOLCAN", "BRUJA", "TESORO", "DRAGON", "COFRE", "SELVA", "ESPADA", "PLANETA",
              "ROBOT", "PLAN", "CASTOR", "CUEVA", "LIBRO", "GOL", "MAGIA", "TRUENO", "COLEGA", "COFRE"]

  palabra = random.choice(palabras)
  intentos = len(palabra)*2
  plantilla = ''

  for i in range(len(palabra)):
    plantilla += '_ '

  print(plantilla)

  while True:
    letra = input('Escribe una letra: ').upper()
    if palabra.find(letra) > -1:
      for i in range(len(palabra)):
        if palabra[i] == letra:
          palabra = palabra[:i] + letra.lower() + palabra[i + 1:]
          plantilla = plantilla[:i * 2] + letra + plantilla[i * 2 + 1:]
      print(plantilla)
      if plantilla.find('_') == -1:
        mensajeVictoria()
        break
    else:
      intentos -= 1
      print(f'Error, la letra {letra} no esta en la palabra. Intentos restantes: {intentos}')
      if intentos <= 0:
        mensajeDerrota()
        print(f'La palabra correcta era {palabra.upper()}')
        break
      else: 
        print(plantilla)


def tresEnRaya():
  print('---- TRES EN RAYA ----')

  tablero= [
    ['   ', ' | ', '   ', ' | ', '   '],
    [' - ', ' + ', ' - ', ' + ', ' - '],
    ['   ', ' | ', '   ', ' | ', '   '],
    [' - ', ' + ', ' - ', ' + ', ' - '],
    ['   ', ' | ', '   ', ' | ', '   ']
  ]

  mostrarTablero(tablero)

  while True:
    print('---- Tu turno ( O ) ----')
    while True:
      columna = int(input('Elige la columna donde quieres colocar tu ficha: '))
      fila = int(input('Elige la fila donde quieres colocar tu ficha: '))

      if tablero[(fila-1)*2][(columna-1)*2] == '   ':
        tablero[(fila-1)*2][(columna-1)*2] = ' O '
        break
      else:
        print('Esta casilla está ocupada')

    mostrarTablero(tablero)

    if comprobarVictoria3raya(tablero):
      break

    print('---- Turno del rival ( X ) ----')

    fila, columna = mejorMovimiento(tablero)
    tablero[fila][columna] = ' X '

    mostrarTablero(tablero)

    if comprobarVictoria3raya(tablero):
      break


def mostrarTablero(tablero):
  for i in tablero:
    print(''.join(i))


def comprobarVictoria3raya(tablero):

  checkFila = ''
  checkColumna = ''
  checkDiagonal1 = ''
  checkDiagonal2 = ''
  for i in range(0, 5, 2):
    checkFila = ''
    checkColumna = ''
    for j in range(0, 5, 2):
      checkFila += tablero[i][j].strip()
      checkColumna += tablero[j][i].strip()
    checkDiagonal1 += tablero[i][i].strip()
    checkDiagonal2 += tablero[i][4 - i].strip()

    if checkFila == 'OOO' or checkColumna == 'OOO':
      print('Has ganado')
      return True
    if checkFila == 'XXX' or checkColumna == 'XXX':
      print('Has perdido')
      return True

  if checkDiagonal1 == 'OOO' or checkDiagonal2 == 'OOO':
    print('Has ganado')
    return True

  if checkDiagonal1 == 'XXX' or checkDiagonal2 == 'XXX':
    print('Has perdido')
    return True

  if not any('   ' in fila for fila in tablero):
    print('Empate')
    return True

  return False


def obtenerGanador(tablero):
  for i in range(0, 5, 2):
    fila = ''
    columna = ''

    for j in range(0, 5, 2):
      fila += tablero[i][j].strip()
      columna += tablero[j][i].strip()

      if fila == 'OOO' or columna == 'OOO':
        return 'O'

    if fila == 'XXX' or columna == 'XXX':
      return 'X'

  diagonal1 = ''
  diagonal2 = ''

  for i in range(0, 5, 2):
    diagonal1 += tablero[i][i].strip()
    diagonal2 += tablero[i][4 - i].strip()

  if diagonal1 == 'OOO' or diagonal2 == 'OOO':
    return 'O'

  if diagonal1 == 'XXX' or diagonal2 == 'XXX':
    return 'X'

  return None

def minimax(tablero, esMaximizador, profundidad=0):
  ganador = obtenerGanador(tablero)

  if ganador == 'X':
    return 10 - profundidad

  if ganador == 'O':
    return profundidad - 10

  casillasLibres = [
    (fila, columna)
    for fila in range(0, 5, 2)
    for columna in range(0, 5, 2)
    if tablero[fila][columna] == '   '
  ]

  if not casillasLibres:
    return 0

  if esMaximizador:
    mejorPuntuacion = -float('inf')

    for fila, columna in casillasLibres:
      tablero[fila][columna] = ' X '
      puntuacion = minimax(tablero, False, profundidad + 1)
      tablero[fila][columna] = '   '

      mejorPuntuacion = max(mejorPuntuacion, puntuacion)

    return mejorPuntuacion

  else:
    mejorPuntuacion = float('inf')

    for fila, columna in casillasLibres:
      tablero[fila][columna] = ' O '
      puntuacion = minimax(tablero, True, profundidad + 1)
      tablero[fila][columna] = '   '

      mejorPuntuacion = min(mejorPuntuacion, puntuacion)

    return mejorPuntuacion


def mejorMovimiento(tablero):
  mejorPuntuacion = -float('inf')
  mejoresCasillas = []

  for fila in range(0, 5, 2):
    for columna in range(0, 5, 2):
      if tablero[fila][columna] == '   ':
        tablero[fila][columna] = ' X '
        puntuacion = minimax(tablero, False, 1)
        tablero[fila][columna] = '   '

        if puntuacion > mejorPuntuacion:
          mejorPuntuacion = puntuacion
          mejoresCasillas = [(fila, columna)]
        elif puntuacion == mejorPuntuacion:
          mejoresCasillas.append((fila, columna))

  return random.choice(mejoresCasillas)


def blackJack():
  print('---- BlackJack ----')

  cartas = [
    '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠',
    '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',
    '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
    '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣'
  ]

  cartasCroupier = []
  puntuacionesCroupier = []
  cartasJugador = []
  puntuacionesJugador = []

  cogerCarta(cartas, cartasCroupier, puntuacionesCroupier)

  for i in range(2):
    cogerCarta(cartas, cartasJugador, puntuacionesJugador)


  while True:
    mostrarCartasCroupier(cartasCroupier, puntuacionesCroupier)
    mostrarCartasJugador(cartasJugador, puntuacionesJugador)
    
    print('- Acciones -')
    print('1- Pedir')
    print('2- Plantarse')

    opc = int(input(''))

    match opc:
      case 1:
        cogerCarta(cartas, cartasJugador, puntuacionesJugador)
        while sum(puntuacionesJugador) > 21 and 11 in puntuacionesJugador:
          indice = puntuacionesJugador.index(11)
          puntuacionesJugador[indice] = 1

        if sum(puntuacionesJugador) >= 21:
          break

      case 2:
        while sum(puntuacionesCroupier) < 17:
          cogerCarta(cartas, cartasCroupier, puntuacionesCroupier)
          while sum(puntuacionesCroupier) > 21 and 11 in puntuacionesCroupier:
            indice = puntuacionesCroupier.index(11)
            puntuacionesCroupier[indice] = 1

        break

  mostrarCartasCroupier(cartasCroupier, puntuacionesCroupier)
  mostrarCartasJugador(cartasJugador, puntuacionesJugador)

  validarGanador(sum(puntuacionesCroupier), sum(puntuacionesJugador))



def cogerCarta(cartas, cartasEscogidas, puntuacionesEscogidas):
  carta = random.choice(cartas)
  cartasEscogidas.append(carta)
  if carta[0] == 'A':
    puntuacionesEscogidas.append(11)
  elif carta[0] in ('K', 'Q', 'J'):
    puntuacionesEscogidas.append(10)
  else:
    puntuacionesEscogidas.append(int(carta[:-1]))
  
  cartas.remove(carta)

def mostrarCartasCroupier(cartasCroupier, puntuacionesCroupier):
  print('┌── Cartas Croupier ──┐')
  print('│' + ' '.join(cartasCroupier).center(21) + '│')
  print(f'└───────────────────{sum(puntuacionesCroupier):02d}┘')

def mostrarCartasJugador(cartasJugador, puntuacionesJugador):
  print('┌─── Cartas Jugador ──┐')
  print('│' + ' '.join(cartasJugador).center(21) + '│')
  print(f'└───────────────────{sum(puntuacionesJugador):02d}┘')

def validarGanador(puntuacionCroupier, puntuacionJugador):
  if puntuacionJugador > 21:
    mensajeDerrota()
  elif puntuacionCroupier > 21:
    mensajeVictoria()
  elif puntuacionJugador > puntuacionCroupier:
    mensajeVictoria()
  elif puntuacionJugador < puntuacionCroupier:
    mensajeDerrota()
  else:
    print('Empate')


def mensajeVictoria():
  print('¡FELICIDADES! Has ganado la partida.')
      
def mensajeDerrota():
  print('Has perdido la partida. :(')


mostrarMenu()