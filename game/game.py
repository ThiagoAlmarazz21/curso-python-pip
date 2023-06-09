import random

username = input('Cual es tu nombre? ')
print('---' * 20)
print(f'Bienvenido al juego {username}!')

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('Elige una opcion: piedra, papel o tijera = ')
  user_option = user_option.lower()

  if not user_option in options:
    print('¡Esa opcion no es válida!')
    return None, None

  pc = random.choice(options)
  
  print(f'{username} elegiste', user_option.upper())
  print('Pc eligió', pc.upper())
  return user_option, pc

def check_rules(user_option, pc, user_win, pc_win):
  
  if user_option == pc:
    print('¡Empate!')
  elif user_option == 'piedra' and pc == 'tijera':
    print(f'¡{username} gana!')
    user_win += 1
  elif user_option == 'papel' and pc == 'piedra':
    print(f'¡{username} gana!')
    user_win += 1
  elif user_option == 'tijera' and pc == 'papel': 
    print(f'¡{username} gana!')
    user_win += 1
  else:
    print('¡Pc gana!')
    pc_win += 1
  return user_win, pc_win
 
def check_winner(user_win, pc_win):
    if pc_win == 3:
      print('---' * 20)
      print('¡El ganador es la PC!')
      print('¡Gracias por jugar!')
      exit()
    elif user_win == 3:
      print('---' * 20)
      print(f'El ganador es {username}')
      print('¡Gracias por jugar!')
      exit()

def run_game():
  user_win = 0
  pc_win = 0
  rounds = 1
  while True: 
    print('---' * 20)
    print(f'¡Ronda {rounds}!')
    print('---' * 20)
    print(f'Puntos de {username}: {user_win}')
    print(f'Puntos de la PC: {pc_win}')

    user_option, pc = choose_options()
    if user_option == None and pc == None: continue
    user_win, pc_win = check_rules(user_option, pc, user_win, pc_win)
    check_winner(user_win, pc_win)
    rounds += 1

run_game()