	z =currentValue
	x = z.value
	pre = x[0:3]
	cut1 = x.find('>')
	cut2 = x.rfind('<')
	message = x[cut1 + 1:cut2]
	print len(x)
	if pre == "<u>":
		system.tag.write("[.]User",message)
	elif pre == '<h>':
		system.tag.write("[.]Heat.value",message)
	elif pre == '<p>':
		system.tag.write("[.]Part.value",message)
	elif pre == '<r>':
		system.tag.write("[.]MRB.value",message)
	elif len(x) == 14:
		system.tag.write("[.]WIP.value",message)
	else:
		pass