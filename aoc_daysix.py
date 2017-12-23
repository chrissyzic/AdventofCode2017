test_bank = [0, 2, 7, 0]
daysix_input = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"
daysix_list = daysix_input.split("\t")
for i in range(len(daysix_list)):
	daysix_list[i] = int(daysix_list[i])

# FIRST STAR

def redistribute(bank_list):
	max_value = max(bank_list)
	max_position = bank_list.index(max_value)
	new_bank = []
	
	for item in bank_list:
		new_bank.append(item)
	
	new_bank[max_position] = 0 

	if max_position == len(new_bank) - 1:
		current_index = 0
	else:
		current_index = max_position + 1

	for i in range(max_value):
		new_bank[current_index] = new_bank[current_index] + 1
		if current_index == len(new_bank) - 1:
			current_index = 0
		elif current_index < len(new_bank) - 1:
			current_index = current_index + 1
	return new_bank

def stop_loop(bank_listy):
	redis_list = []
	unique = 'TRUE'
	old_dis = redistribute(bank_listy)
	redis_list.append(old_dis)

	'''
	new_dis = redistribute(old_dis)
	redis_list.append(new_dis)
	old_dis = new_dis
	new_dis = redistribute(old_dis)
	redis_list.append(new_dis)
	old_dis = new_dis
	new_dis = redistribute(old_dis)
	redis_list.append(new_dis)
	old_dis = new_dis
	new_dis = redistribute(old_dis)
	redis_list.append(new_dis)
	'''

	while unique == 'TRUE':
		new_dis = redistribute(old_dis)
		if new_dis in redis_list:
			redis_list.append(new_dis)
			unique = 'FALSE'
		else:
			redis_list.append(new_dis)
			old_dis = new_dis
	return len(redis_list)

#print stop_loop(test_bank)
print "First star answer: " + str(stop_loop(daysix_list))

#SECOND STAR

def stop_loop_remix(bank_listy):
	redis_list = []
	unique = 'TRUE'
	old_dis = redistribute(bank_listy)
	redis_list.append(old_dis)

	while unique == 'TRUE':
		new_dis = redistribute(old_dis)
		if new_dis in redis_list:
			#redis_list.append(new_dis)
			first_occurrence_position = redis_list.index(new_dis)
			unique = 'FALSE'
		else:
			redis_list.append(new_dis)
			old_dis = new_dis
	return len(redis_list) - first_occurrence_position

print test_bank
print "Second star answer: " + str(stop_loop_remix(daysix_list))

