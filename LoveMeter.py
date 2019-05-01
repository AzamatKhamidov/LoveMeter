import random


def main():
	print('Welcome! I can calculate love percent beetwen two names.')
	first_name = input('First name: ')
	second_name = input('Second name: ')
	text = 'First name: {}\nSecond name: {}\nCompatibility ratio: {}%'.format(first_name, second_name,
		random.randint(0, 100))
	print('==== ==== ====')
	print(text)
	print('==== ==== ====')
	again = input('Again? ')
	if again == 'Yes':
		main()
	else:
		print('GoodBye!')
		exit()

main()