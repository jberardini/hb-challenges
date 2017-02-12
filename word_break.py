
def parse(phrase, vocab, cache=None):
	#go through the phrase
	#if the current string matches a string in our set, hold onto it and add a space
	#keep adding to current string into it matches something in vocab set
	#if it never matches, throw it away
	#how do we not keep returning what we've already seen?
	#

	if cache is None:
		cache = {}


	if phrase in cache:
		return cache[phrase]

	possible_breaks = set()

	for word in vocab:
		if word == phrase:
			possible_breaks.add(word)

		elif phrase.startswith(word):
			rest = phrase[len(word):]

			cache[phrase] = rest

			word_and_rest = {word + " " + parsed for parsed in parse(rest, vocab, cache)}


			possible_breaks.update(word_and_rest)



	return possible_breaks


vocab = {'i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to', 'night',
         'ate', 'noodles', 'for', 'dinner', 'tonight'}

print parse("iatenoodlesfordinnertonight", vocab)




if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print