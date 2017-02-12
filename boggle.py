def play_boggle(board, word):
	# get a 5x5 board
	# can only move NEWS direction

	# look for the first letter in word, traversing l to r, t to b

	for i in range(len(board)):
		for j in range(len(board[0])):
			if check_directions(board, i, j, word, seen=set()):
				return True

	return False



def check_directions(board, i, j, word, seen):

	
	if board[i][j] != word[0]:
		return False

	if (i,j) in seen:
		return False

	if len(word)==1:
		return True

	seen = seen | {(y, x)}

	if j> 0:
		if check_directions(board, i, j-1, word[1:], seen):
			return True

	if j < 4:
		if check_directions(board, i, j+1, word[1:], seen):
			return True

	if i > 0:
		if check_directions(board, i-1, j, word[1:], seen):
			return True

	if i < 4:
		if check_directions(board, i+1, j, word[1:], seen):
			return True
	
	return False



	# once we find it, we can check all directions (if exist) to see if we find
	# once we find, we check all directions
	# anytime we can't find the next letter, we return false

print play_boggle([['N', 'C', 'A', 'N', 'E'], ['O', 'U', 'I', 'O', 'P'], ['Z', 'Q', 'Z', 'O', 'N'], ['F', 'A', 'D', 'P', 'L'], ['E', 'D', 'E', 'A', 'Z']], 'NOON')

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
