import numpy as np


#    *   threading within a single game in a way that the time taken to run a function
#        for eg : does not affect the flow of the game the time between auto attacks to calculate
#                 the damage that the next ability of the champion will do so that at the time the
#                 champion has to cast it's ability it does not because it is calculating the data
#    *   multiprocessing on different games so that multiple instances of the game can be run 
#        simultaneously to collect the data to feed the RL algorythm

# note : the approach may vary if a more viable solution can be brought up
# note : the complete explanation of the game is written in the 
#        "game_explanation.txt" file in the current directory



#extras
#  the board is a combination of a bunch of hexagons .. 7x4 with exeption in very few instances
#  the champion hits the target in the closest range 
#  if the target is not in range then, it moves towards the closest champion that will be in it's attack range
#  if the champion is in attack range but is moving then it chases the chapion to 1 hex before changing target to the target in range
#  that means that a melee champion will not keep on chaseing a melee champion or a ranged champion will not follow a melee champion
 

 

# universe_type is to determine the number of rows in the board_player ( not the main game board ( board_main ))
# for now unless a certain universe type with different board rows is set the number of rows is set to 4
# the number of rows in the board_main is determined my using the value of the player game mode

# global universe_type
# universe_type = .....( used to determine the value of item spwnm, champion spawn, boars size and other things )

"""
board_row_player_num = 3
board_row_num = 7
board_column_num = 6
board_data_num = 15
board_player_num = np.zeros(shape = ( board_row_player_num , board_column_num ), dtype=np.int16)
# the board_row and board_column value may not be used directly in the functions as matrices start from (0.0.0) haha :p
board_main = np.zeros(shape = ( board_row_num , board_column_num ), dtype=np.int16)
for board_main_x in range(board_row_num):
  for board_main_y in range(board_column_num):
    if board_player_num[board_main_x,board_main_y,0]== 0:
      break
    if board_player_num[board_main_x,board_main_y,0]== 1:
      for board_main_z in range(board_data_num):
        board_main[board_main_x,board_main_y,board_main_z] = board_player_num[board_row_player_num-board_main_x,board_column_num-board_main_y,board_main-board_main_z] 
    if board_player_num[board_main_x,board_main_y,0]== 2:
      for board_main_z in range(board_data_num):
        board_main[board_main_x,board_main_y,board_main_z] = board_player_num[((board_row_num-1)/2),board_column_num,board_main]
    else:
          ValueError("the data is out of range") 
"""      

class mainboarddata:
    def __init__(self,star,hea,mhea,mana,mmana,manareg,critper,critpro,attdmg,attrng,arm,mgrst,):
      h = "hello" 
      print (h)

class playerboarddata:
    def __init__(self,sym,cst,star,bhea,bmana,bmanareg,abifun,abitime,ori,cla,battdmg,battrng,barm,bmgrst,):
      h = "haha"
      print (h)
