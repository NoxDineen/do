player = 'nox'
troublemakers = ['wyatt', 'corey']
stones_kept = 0

if not player.in_trouble():
	if stones_kept == 0:
		goal_word = True
		author = troublemakers
		player.trouble_state = True
	elif stones_kept == 1:
		goal_word = True
		author = troublemakers
		player.trouble_state = True
		goal_word = False
		author = player
		player.trouble_state = False
	elif stones_kept == 2:
		goal_word = True # remains true for both chapters
		author = player
		author = troublemakers
		player.trouble_state = True
	else: # stones_kept == 3
		goal_word = True
		author = player
else: # player.in_trouble()
	if stones_kept == 0:
		goal_word = True
		author = troublemakers # troublemakers can choose to pass in this situation
	elif stones_kept == 1:
		goal_word = False
		author = player
		player.trouble_state = False
	elif stones_kept == 2:
		# as above, player can pass in which case troublemakers also pass
		goal_word = False
		author = player
		player.trouble_state = False
		goal_word = True
		author = troublemakers
		player.trouble_state = True
	else: # stones_kept == 3
		goal_word = False
		author = player
		player.trouble_state = False
