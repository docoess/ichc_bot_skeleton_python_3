import requests, time

account = "bot_account_name"
api_key = "bot_api_key"
room = "room_name"

root_url = "http://www.icanhazchat.com/api.ashx?v=1"

def get_responses(s):
	s = requests.get(s).text.split("\n")
	if s[0] != "OK":
		raise Exception(f"Got [{s[0]}] instead of [OK]")
	return s

def process_chat(lines):
	say_something = False
	for (i,line) in enumerate(lines):
		if i != 0:
			if line != "":
				print(line)
				say_something = line.find("thing_to_look_for") != -1
	if say_something:
		print("Someone is talking to me")
		process_chat(get_responses(root_url + "&k=" + room_key + "&a=send&w=" + "thing_to_say/do"))
	else:
		time.sleep(2)



lines = get_responses(root_url + "&u=" + account + "&p=" + api_key + "&a=join&w=" + room)
room_key = lines[1]

while True:
	process_chat(get_responses(root_url + "&k=" + room_key + "&a=recv"))