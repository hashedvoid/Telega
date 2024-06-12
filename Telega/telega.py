import requests
import time
import json

URL = 'https://api.telegram.org/bot'

class ExistenseException(Exception):
	pass

class Bot:
	class newExistense:
		def __init__(self, token):
			global TOKEN
			self.token = token
			TOKEN = self.token
		def getMe(self):
			try:
				self.result = requests.get(f'{URL}{self.token}/getMe').json()['result']
			except KeyError:
				raise ExistenseException('Invalid token entered.')
			return self.result
		def getUpdates(self, offset=0):
			self.result = requests.get(f'{URL}{self.token}/getUpdates?offset={offset}').json()
			return self.result['result']
		class sendMessage:
			def __init__(self, id, text, parsemode='Markdown', replymarkup={}):
				self.id = id
				self.text = text
				self.parsemode = parsemode
				self.replymarkup = replymarkup
				self.result = requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={self.id}&parse_mode={self.parsemode}&text={self.text}&reply_markup={self.replymarkup}').json()
			def response(self):
				return self.result
		class sendPhoto:
			def __init__(self, id, url):
				self.id = id
				self.url = url
				self.result = requests.get(f'{URL}{TOKEN}/sendPhoto?chat_id={self.id}&photo={self.url}').json()
			def response(self):
				return self.result
		class sendVideo:
			def __init__(self, id, video):
				self.id = id
				self.video = video
				self.result = requests.get(f'{URL}{TOKEN}/sendVideo?chat_id={self.id}&video={self.video}').json()
			def response(self):
				return self.result
		class sendAnimation:
			def __init__(self, id, animation):
				self.id = id
				self.animation = animation
				self.result = requests.get(f'{URL}{TOKEN}/sendAnimation?chat_id={self.id}&animation={self.animation}').json()
			def response(self):
				return self.result
		class sendVoice:
			def __init__(self, id, voice):
				self.id = id
				self.voice = voice
				self.result = requests.get(f'{URL}{TOKEN}/sendVoice?chat_id={self.id}&voice={self.voice}').json()
			def response(self):
				return self.result
		class sendVideoNote:
			def __init__(self, id, video_note):
				self.id = id
				self.video_note = video_note
				self.result = requests.get(f'{URL}{TOKEN}/sendVideoNote?chat_id={self.id}&video_note={self.video_note}').json()
			def response(self):
				return self.result
		class sendMediaGroup:
			def __init__(self, id, video_note):
				self.id = id
				self.video_note = video_note
				self.result = requests.get(f'{URL}{TOKEN}/sendMediaGroup?chat_id={self.id}&media={self.media}').json()
			def response(self):
				return self.result
		class sendLocation:
			def __init__(self, id, latitude, longitude):
				self.id = id
				self.latitude = latitude
				self.longitude = longitude
				self.result = requests.get(f'{URL}{TOKEN}/sendLocation?chat_id={self.id}&latitude={self.latitude}&longitude={self.longitude}').json()
			def response(self):
				return self.result
		class sendContact:
			def __init__(self, id, phonenumber, firstname):
				self.id = id
				self.phonenumber = phonenumber
				self.firstname = firstname
				self.result = requests.get(f'{URL}{TOKEN}/sendContact?chat_id={self.id}&phone_number={self.phonenumber}&first_name={self.firstname}').json()
			def response(self):
				return self.result
		class sendDice:
			def __init__(self, id):
				self.id = id
				self.result = requests.get(f'{URL}{TOKEN}/sendDice?chat_id={self.id}').json()
			def response(self):
				try:
					return self.result['result']
				except Exception as e:
					raise ExistenseException('{e}')
		class getUserProfilePhotos:
			def __init__(self, id):
				self.id = id
				self.result = requests.get(f'{URL}{TOKEN}/getUserProfilePhotos?chat_id={self.id}').json()
			def response(self):
				return self.result
		class banChatMember:
			def __init__(self, cid, uid, revoke_messages=False):
				# cid - chat id, uid - user id (target to ban)
				self.cid = cid
				self.uid = uid
				self.revoke_messages = revoke_messages
				self.result = requests.get(f'{URL}{TOKEN}/banChatMember?chat_id={self.cid}&user_id={self.uid}&revoke_messages={self.revoke_messages}').json()
		class unbanChatMember:
			def __init__(self, cid, uid, only_if_banned=True):
				# cid - chat id, uid - user id (target to unban)
				self.cid = cid
				self.uid = uid
				self.only_if_banned = only_if_banned
				self.result = requests.get(f'{URL}{TOKEN}/unbanChatMember?chat_id={self.cid}&user_id={self.uid}&only_if_banned={self.only_if_banned}').json()
			def response(self):
				return self.result
		class restrictChatMember:
			def __init__(self, cid, uid, permissions):
				# cid - chat id, uid - user id (target to restrict)
				self.cid = cid
				self.uid = uid
				self.permissions = permissions
				self.result = requests.get(f'{URL}{TOKEN}/unbanChatMember?chat_id={self.cid}&user_id={self.uid}&permissions={self.permissions}').json()
	class Keyboard:
		def __init__(self, mode="keyboard", **args):
			self.mode = mode
			self.keyboard = {mode: [[]]}
			self.keyboard.update(args)
		def add_line(self, *args):
			self.keyboard[self.mode].append(list(args))
		def add_button(self, **args):
			self.keyboard[self.mode][-1].append(args)
		def clear(self):
			self.keyboard[self.mode] = [[]]
		def compile(self):
			return json.dumps(self.keyboard)
