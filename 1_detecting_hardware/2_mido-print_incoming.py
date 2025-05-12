import mido

for device in mido.get_input_names():
	if 'LPK25' in device:
		keyboard = device

with mido.open_input(keyboard) as port:
	for msg in port:
		print(msg)
