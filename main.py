def has_chars(word, chars):
        return any([x for x in word if x in chars])

def meets_requirements(password):
        return(has_chars(password, [chr(c) for c in range(ord('a'), ord('z') + 1)]) and 
               has_chars(password, [chr(c) for c in range(ord('A'), ord('Z') + 1)]) and
               has_chars(password, [chr(c) for c in range(ord('0'), ord('9') + 1)]))

print meets_requirements('aA0');
print meets_requirements('zZ9');
print meets_requirements('z');
print meets_requirements('zZ');

def strength(password):
	rating = 1
	if has_chars(password, [chr(c) for c in range(ord('a'), ord('z') + 1)]):
		rating += 1
		if has_chars(password, [chr(c) for c in range(ord('A'), ord('Z') + 1)]):
			rating += 2
	elif has_chars(password, [chr(c) for c in range(ord('A'), ord('Z') + 1)]):
			rating += 1
	if has_chars(password, [chr(c) for c in range(ord('0'), ord('9') + 1)]):
		rating += 3
	if has_chars(password, ". ? ! & # , ; : - _ *".split()):
		rating += 3
	
	return rating

print strength("x")
print strength("aZ")
print strength("Z")
print strength("aZ0")
print strength("aZ0.")