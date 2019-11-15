FULLTIME = 13.5 # duration it takes for the table to raise / lower all the way
STOP_SLEEP_DURATION = 0.5 # time between commands

# pins of raspberry pi
RELAIS_2_GPIO = 18
RELAIS_1_GPIO = 17

# user and their spells in arrays
# sit spell string - sit height from all lowered - stand spell string - stand height from all raised
JAN = ["impedimenta", 3.1, "expelliarmus", 3.0]
MERLIN = ["avada kedavra", 3.5, "expecto patronum", 3.2]
CELINA = ["crucio", 2.9, "lumos maximus", 3.4]
PROGRAM_EXIT = "beenden" # spell for exiting
