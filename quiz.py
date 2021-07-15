import discord 
import json 

# download quiz deck 
# unzip quiz_deck 

# dict for user and points

# iter each round 
#   iter each member 
#       select question and present
#           queue = []
#           answered = false
#           active user = user
#           reward = 25
#           punishment = 0
#           while not answered or reward > 5
#               answered correctly?                   
#                   award points 
#               else
#                   select some other user from queue
#                   reward -= 10
#                   if punishment == 0:
#                       punishment = 10