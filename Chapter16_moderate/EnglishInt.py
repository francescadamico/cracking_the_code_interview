'''
Given an integer, print an English phrase that describes the integer (e.g. "One Thousand, Two Hundred Thirty Four").
'''

def create_decimals(d):
	
	d.update({i * 10 : d[i] + 'ty' for i in range(6, 10)})	
	
	return d


def create_eng_num_dic():
	d = {
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine',
		10: 'ten',
		11: 'eleven',
		12: 'twelve',
		13: 'thirteen',
		14: 'fourteen',
		15: 'fifteen',
		16: 'sixteen',
		17: 'seventeen',
		18: 'eighteen',
		19: 'nineteen',
		20: 'twenty',
		30: 'thirty',
		40: 'fourty',
		50: 'fifty',
		100: 'one hundred',
		1000: 'one thousand'
}

	create_decimals(d)

	return d
	

def un_dec(n_str, d):

	out_str = d[int(n_str[0]) * 10] + ' ' + d[int(n_str[1])]
	return out_str


def translate(n_str, d):

	if len(n_str) == 1:
		out =	str(d[int(n_str[0])])
	if len(n_str) > 1:
		out = un_dec(n_str[1:], d)
	if len(n_str) == 3:
		out = d[int(n_str[0])] + ' hundred ' + out

	return out

		
def eng_int(n):

	d = create_eng_num_dic()
	n_str = str(n)
	n_digit = len(n_str)		

	if n_digit > 3:
		dig = 3
	else:
		dig = n_dig
	out_str = translate(n_str[-dig:], d) # hundred

	if n_digit > 3:
		out_str = translate(n_str[-n_digit:-3], d) + ' thousand ' + out_str # thousand

	if n_digit > 6:
		out_str = translate(n_str[-n_digit:-6], d) + ' million ' + out_str # million

	return out_str

print(eng_int(123456))
	
	
	
	 
	
	

