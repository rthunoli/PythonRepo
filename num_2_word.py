#!/usr/bin/python3

def n2w(number):
	words = ''
	NumWord = \
	{
		0:'zero',
		1:'one',
		2:'two',
		3:'three',
		4:'four',
		5:'five',
		6:'six',
		7:'seven',
		8:'eight',
		9:'nine',
		10:'ten',
		11:'eleven',
		12:'twelve',
		13:'thirteen',
		14:'fourteen',
		15:'fifteen',
		16:'sixteen',
		17:'seventeen',
		18:'eighteen',
		19:'nineteen',
		20:'twenty',
		30:'thirty',
		40:'forty',
		50:'fifty',
		60:'sixty',
		70:'seventy',
		80:'eighty',
		90:'ninety',
	}

	word = NumWord.get(number,'')
	if word == '':
		if number < 100:
			rem = number % 10
			number -= rem
			word = n2w(rem)	
			word = n2w(number) + " " + word
		elif number < 1000:
			rem = number % 100
			number //= 100
			if rem > 0:
				word = n2w(rem)	
			word = n2w(number) + " hundred " + word

		elif number < 1000000: #Less than one million
			rem = number % 1000
			number //= 1000
			if rem > 0:
				word = n2w(rem)	
			word = n2w(number) + " thousand " + word
		
		elif number < 1000000000: #Less than one billion
			rem = number % 1000000
			number //= 1000000
			if rem > 0:
				word = n2w(rem)	
			word = n2w(number) + " million " + word
		
		elif number < 1000000000000: #Less than one trillion
			rem = number % 1000000000
			number //= 1000000
			if rem > 0:
				word = n2w(rem)	
			word = n2w(number) + " billion " + word
	else:
		return word
	
	return word

while True:	
	number_string = input("Enter a number (q to quit) : ")
	if number_string == 'q' or number_string == 'Q':
		break

	number  = int(number_string)

	print(n2w(number))

