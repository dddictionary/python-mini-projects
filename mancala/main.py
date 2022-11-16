import random

class Pit:
  def __init__(self,label,seeds=4):
    self.__seeds = seeds
    self.label = label

  def is_bank(self):
    if "bank" in self.label.lower():
      return True
    return False

  def add_seed(self):
    self.__seeds += 1

  def set_seeds_to_zero(self):
    self.__seeds = 0

  def get_seeds(self):
    return self.__seeds


class Board:
  def __init__(self,seeds=[4,4,4,4,4,4,0,4,4,4,4,4,4,0]):
    self.board = []
    self.player = "A"
    for i in range(14):
      if i < 6:
        self.board.append(Pit(f"A{i+1}",seeds[i]))
      elif i == 6:
        self.board.append(Pit(f"A BANK",seeds[i]))
      elif i < 13:
        self.board.append(Pit(f"B{i-6}",seeds[i]))
      elif i == 13:
        self.board.append(Pit("B BANK",seeds[i]))

  def __str__(self):
    display = []
    for i in range(12,6,-1):
      display.append(self.board[i].label)
    for i in range(12,6,-1):
      display.append(self.board[i].get_seeds())
    display.append(self.board[13].get_seeds())
    display.append(self.board[6].get_seeds())
    for i in range(0,6,1):
      display.append(self.board[i].label)
    for i in range(0,6,1):
      display.append(self.board[i].get_seeds())
    s = """    
    +------+------+--<<<<<-Player B----+------+------+------+
    B      |{}    |{}    |{}    |{}    |{}    |{}    |      A
           |  {:2d}  |  {:2d}  |  {:2d}  |  {:2d}  |  {:2d}  |  {:2d}  |
    B      |      |      |      |      |      |      |      B
    A {:2d}   +------+------+------+------+------+------+  {:2d}  A
    N      |{}    |{}    |{}    |{}    |{}    |{}    |      N
    K      |  {:2d}  |  {:2d}  |  {:2d}  |  {:2d}  |  {:2d}  |  {:2d}  |      K
           |      |      |      |      |      |      |       
    +------+------+------+-Player A->>>>>-----+------+------+
            """.format(*display)
    return s

  def play_move(self,label):
    index = 0
    seeds = 0
    for j in self.board:
      if label == j.label:
        seeds = j.get_seeds()
        index = self.board.index(j)
        break
        
    self.board[index].set_seeds_to_zero()
    
    while True:        
      index += 1
      if index == 14:
          index = 0
      cond1 = (self.board[index].is_bank() and self.player == "B" and index == 6)
      cond2 = (self.board[index].is_bank() and self.player == "A" and index == 13)
      if cond1 or cond2:
        index += 1
        if index == 14:
          index = 0

      self.board[index].add_seed()
      seeds -= 1
      if seeds == 0:
        break
    if self.player == "A" and index < 6:
      if self.board[index].get_seeds() == 1 and self.board[12-index].get_seeds() != 0:
        seeds2 = self.board[index].get_seeds() + self.board[12-index].get_seeds()
        for i in range(seeds2):
          self.board[6].add_seed()
        self.board[index].set_seeds_to_zero()
        self.board[12-index].set_seeds_to_zero()

        
    elif self.player == "B" and index > 6 and index != 13:
      if self.board[index].get_seeds() == 1 and self.board[12-index].get_seeds() != 0:
        seeds2 = self.board[index].get_seeds() + self.board[12-index].get_seeds()
        for i in range(seeds2):
          self.board[13].add_seed()
        self.board[index].set_seeds_to_zero()
        self.board[12-index].set_seeds_to_zero()
        
    # This code is for repeating a turn for a player
    # if index == 6 and self.player == "A" or index == 13 and self.player == "B":
    #     print(f"Player {self.player}'s turn. \n")
    #     print(*self.get_valid_moves(),end="\n\n")
    #     print(self)
    #     pit_choice = input("You get to play again. \n")
    #     self.play_move(pit_choice)

      

  
  def switch_player(self):
    if self.player == "A":
      self.player = "B"
    else:
      self.player = "A"

  def get_valid_moves(self):
    valid_moves = []

    if self.player == "A":
      for i in range(6):
        if self.board[i].get_seeds() != 0:
          valid_moves.append(self.board[i].label)
    else:
      for i in range(7,13):
        if self.board[i].get_seeds() != 0:
          valid_moves.append(self.board[i].label)

    return valid_moves


  def game_over(self):
    A = []
    B = []
    for i in range(6):
      if self.board[i].get_seeds() == 0:
        A.append(i)

    for i in range(7,13):
      if self.board[i].get_seeds() == 0:
        B.append(i)

    if len(A) == 6 or len(B) == 6:
      return True
    return False

  def results(self):
    for i in range(0,6):
      seeds = self.board[i].get_seeds()
      self.board[i].set_seeds_to_zero()
      for j in range(seeds):
        self.board[6].add_seed()

    for i in range(7,13):
      seeds = self.board[i].get_seeds()
      self.board[i].set_seeds_to_zero()
      for j in range(seeds):
        self.board[13].add_seed()

    a = self.board[6].get_seeds()
    b = self.board[13].get_seeds()
    if a > b:
      return f"{self}\n~~Player A wins! The final score:\n A: {a} B: {b}"
    elif a < b:
      return f"{self}\n~~Player B wins! The final score:\n A: {a} B: {b}"
    else:
      return f"{self}\n~~It is a tie! The final score:\n A: {a} B: {b}"

def simulate(game):
  d = {}
  if game.player == "B":
    for pit in game.get_valid_moves():
      copy = game
      # print(temp.get_valid_moves())
      copy.play_move(pit)
      d[pit] = copy.board[13].get_seeds()
    print(d)
    print(max(d))
  return str(max(d))

      
def start_game():
  game = Board()

  easy = False
  hard = False
  two_p = False
  game_diff = ""
  while game_diff not in ["1","2","3"]:
    game_diff = input("""
Chose between easy or hard mode:
                      
1. Easy
2. Hard (not really working)
3. two-player mode

""")
  if game_diff == "1":
    easy = True
    print("Easy mode chosen")
  elif game_diff == "2":
    hard = True
    print("Hard mode chosen")
  else:
    two_p = True
    print("Two Player mode chosen")

  print(game)
      
  while True:      
    if game.player == "B" and easy:
      print(f"Player {game.player}'s turn. \n")
      # print(game)
      print(*game.get_valid_moves(),end="\n\n")
      b_choice = random.choice(game.get_valid_moves())
      game.play_move(b_choice)
      print(f"Player B played {b_choice}")
      print(game)
      if game.game_over():
        break
      game.switch_player()

    if game.player == "B" and hard:
      print(f"Player {game.player}'s turn. \n")
      # print(game)
      print(*game.get_valid_moves(),end="\n\n")
      b_choice = simulate()
      game.play_move(b_choice)
      print(b_choice)
      print(f"Player B played {b_choice}")
      print(game)
      if game.game_over():
        break
      game.switch_player()
      
    print(f"Player {game.player}'s turn. \n")
    print(*game.get_valid_moves(),end="\n\n")
    
    pit_choice = ""
    while pit_choice not in game.get_valid_moves():
      pit_choice = input("Please chose a pit to play from the options above!\n")

    game.play_move(pit_choice)
    print(game)

    if game.game_over():
      break
    game.switch_player()

  print(game.results())

start_game()