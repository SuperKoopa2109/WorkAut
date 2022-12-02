import requests
import json
import os

import mysql.connector

#Python libraries that we need to import for our bot
import random

from pymessenger.bot import Bot

from flask import *

from telegram.ext import Updater, CommandHandler

from pymessenger import *

from wit import Wit

client = Wit('BT3MHAJMXLPXVHXBLEFFMKX3VZFELEXQ')

printex = {
	"counter": 0,
	"exercise": [],
	"plan": "0"
}

#from flask import Flask, render_template, request, jsonify, session, g, redirect
#from flask.ext.session import Session
app = Flask(__name__)
app.secret_key = os.urandom(24)
ACCESS_TOKEN = 'EAATnxXfYA08BAIt0vI5pVUYpg6LZBVUjE1pFsqXyC8VhMai2fyAb9QRnGT8paVvZCuiw6o5PSgszH6EJO0KUDCypSjZCuNtPJKaMBImpTeeuZBsoxic8CaTZCcP2gNTzmkudGBgVCdsUmhIzTQ3WHmGBSSjbhN6MhKhkr0VAruZAvdlFk3PILt'
VERIFY_TOKEN = 'keyWork4ut'
bot = Bot(ACCESS_TOKEN)

mydb = mysql.connector.connect(
	host="localhost",
	user="AGM",
	passwd="1234",
	database="workautdb"
	)
	
mycursor = mydb.cursor()

# prepped = Request('POST',  # oder irgendeine andere Methode, 'POST', 'PUT', etc.
                  # url,
                  # data=data
                  # headers=headers
                  # # ...Ö
                  # ).prepare()

@app.route('/fbconnect', methods=['POST', 'GET'])
def fbconnect():
	if request.method == 'GET':
		# Before allowing people to message your bot, Facebook has implemented a verify token
		# that confirms all requests that your bot receives came from Facebook. 
		token_sent = request.args.get("hub.verify_token")
		return verify_fb_token(token_sent)
	# if the request was not get, it must be POST and we can just proceed with sending a message # back to user
	else:
		output = request.get_json()
		for event in output['entry']:
			messaging = event['messaging']
			for message in messaging:
				# if 'message' in message:
					# if message['message'].get('attachments'):
							# print("hi")
				if message.get('message'):
					if message['sender']['id'] != "1884548588293899":
						if message['message'].get('attachments'):
							recipient_id = message['sender']['id']
							print(recipient_id)
							mycursor.execute("SELECT table_user.uID, table_user.username FROM table_user WHERE fb_id=" + recipient_id + "")
							logindata = mycursor.fetchall()
							print(logindata)
							if(logindata == []):
								send_message(recipient_id, "Bitte lasse dich von einem Admin freischalten!")
							else:
								mycursor.execute("SELECT table_user.cur_plan FROM table_user WHERE table_user.fb_id=" + str(recipient_id) + "")
								cur_plan = mycursor.fetchone()
								if (printex['exercise'] == []) or (printex['plan'] != cur_plan[0]):
									printex['plan'] = cur_plan[0]
									TPShowFB(cur_plan[0], recipient_id)
									mycursor.execute("SELECT table_user.counter FROM table_user WHERE table_user.fb_id=" + str(recipient_id) + "")
									counter = mycursor.fetchone()
									printex['counter'] = counter[0]
								print(len(printex['exercise']))
								print(printex['exercise'])
								send_message(recipient_id, printex['exercise'][printex['counter']][0] + "\n Sätze: " + str(printex['exercise'][printex['counter']][1]) + "\n Wiederholungen: " + str(printex['exercise'][printex['counter']][2]))
								printex['counter'] = printex['counter'] + 1
								print(recipient_id)
								mycursor.execute("UPDATE table_user SET table_user.counter=" + str(printex['counter']) + " WHERE table_user.fb_id=" + str(recipient_id) + "")
								mydb.commit()
								print(len(printex['exercise']))
								if printex['counter'] == len(printex['exercise']):
									printex['counter'] = 0
									print(recipient_id)
									mycursor.execute("UPDATE table_user SET table_user.counter=" + str(printex['counter']) + " WHERE table_user.fb_id=" + str(recipient_id) + "")
									mydb.commit()
									mycursor.execute("SELECT table_user.cur_plan FROM table_user WHERE table_user.fb_id=" + str(recipient_id) + "")
									cur_plan = mycursor.fetchone()
									send_message(recipient_id, "Super! Du hast dein Training für heute geschafft! \n Iss nun ordentlich und ruh dich aus.")
									mycursor.execute("SELECT table_plan.pID FROM table_plan INNER JOIN table_user ON table_plan.uID=table_user.uID WHERE table_user.fb_id=" + str(recipient_id) + " ORDER BY table_plan.pID ASC")
									pID = mycursor.fetchall()
									found = False
									#[{4, }; {5, }; {6, }]
									for x in pID:
										if (cur_plan[0] + 1) in x:
											mycursor.execute("UPDATE table_user SET table_user.cur_plan=" + str(cur_plan[0] + 1) + " WHERE table_user.fb_id=" + str(recipient_id) + "")
											found = True
											break
									if not found:
										mycursor.execute("UPDATE table_user SET table_user.cur_plan=" + str(pID[0][0]) + " WHERE table_user.fb_id=" + str(recipient_id) + "")
									mydb.commit()
						else:
							print("asdf")
							#Facebook Messenger ID for user so we know where to send response back to
							recipient_id = message['sender']['id']
							print(recipient_id)
							mycursor.execute("SELECT table_user.uID, table_user.username FROM table_user WHERE fb_id=" + recipient_id + "")
							logindata = mycursor.fetchall()
							print(logindata)
							if(logindata == []):
								send_message(recipient_id, "Bitte lasse dich von einem Admin freischalten!")
							else:
								ans = client.message(message['message'].get('text'))
								print(ans['entities'])
								if 'change' in ans['entities'] and 'exercise' in ans['entities']:
									# send_message(recipient_id, "Uebung ändern")
									nex = ChangeEx(ans['entities']['exercise'][0]['value'], recipient_id)
									send_message(recipient_id, "Die Übung " + ans['entities']['exercise'][0]['value'] + " wurde in " + nex + " getauscht")
								elif 'show' in ans['entities']:
									mycursor.execute("SELECT table_user.cur_plan FROM table_user WHERE \
														table_user.fb_id=" + str(recipient_id) + "")
									cur_plan = mycursor.fetchone()
									if (printex['exercise'] == []) or (printex['plan'] != cur_plan[0]):
										printex['plan'] = cur_plan[0]
										TPShowFB(cur_plan[0], recipient_id)
										mycursor.execute("SELECT table_user.counter FROM table_user WHERE \
															table_user.fb_id=" + str(recipient_id) + "")
										counter = mycursor.fetchone()
										printex['counter'] = counter[0]
									send_message(recipient_id, printex['exercise'][printex['counter']][0] + \
													"\n Sätze: " + str(printex['exercise'][printex['counter']][1]) + \
													"\n Wiederholungen: " + str(printex['exercise'][printex['counter']][2]))
									printex['counter'] = printex['counter'] + 1
									mycursor.execute("UPDATE table_user SET table_user.counter=" + str(printex['counter']) \
														+ " WHERE table_user.fb_id=" + str(recipient_id) + "")
									mydb.commit()
									print(len(printex['exercise']))
									if printex['counter'] == len(printex['exercise']):
										printex['counter'] = 0
										print(recipient_id)
										mycursor.execute("UPDATE table_user SET table_user.counter=" + str(printex['counter']) + " WHERE table_user.fb_id=" + str(recipient_id) + "")
										mydb.commit()
										mycursor.execute("SELECT table_user.cur_plan FROM table_user WHERE table_user.fb_id=" + str(recipient_id) + "")
										cur_plan = mycursor.fetchone()
										send_message(recipient_id, "Super! Du hast dein Training für heute geschafft! \n Iss nun ordentlich und ruh dich aus.")
										mycursor.execute("SELECT table_plan.pID FROM table_plan INNER JOIN table_user ON table_plan.uID=table_user.uID WHERE table_user.fb_id=" + str(recipient_id) + " ORDER BY table_plan.pID ASC")
										pID = mycursor.fetchall()
										found = False
										#[{4, }; {5, }; {6, }]
										for x in pID:
											if (cur_plan[0] + 1) in x:
												mycursor.execute("UPDATE table_user SET table_user.cur_plan=" + str(cur_plan[0] + 1) + " WHERE table_user.fb_id=" + str(recipient_id) + "")
												found = True
												break
										if not found:
											mycursor.execute("UPDATE table_user SET table_user.cur_plan=" + str(pID[0][0]) + " WHERE table_user.fb_id=" + str(recipient_id) + "")
										mydb.commit()
								elif 'create' in ans['entities']:
									print("hi")
									#mycursor.execute("UPDATE table_user SET table_user.cur_plan=" + str() + " WHERE table_user.fb_id=" + str(recipient_id) + "")
								elif 'cancel' in ans['entities']:
									printex['counter'] = 0
									mycursor.execute("UPDATE table_user SET table_user.counter=" + str(printex['counter']) + " WHERE table_user.fb_id=" + str(recipient_id) + "")
									mydb.commit()
									mycursor.execute("SELECT table_user.cur_plan FROM table_user WHERE table_user.fb_id=" + str(recipient_id) + "")
									cur_plan = mycursor.fetchone()
									send_message(recipient_id, "Dein Training wurde abgebrochen.")
									mycursor.execute("SELECT table_plan.pID FROM table_plan INNER JOIN table_user ON table_plan.uID=table_user.uID WHERE table_user.fb_id=" + str(recipient_id) + " ORDER BY table_plan.pID ASC")
									pID = mycursor.fetchall()
									found = False
									#[{4, }; {5, }; {6, }]
									for x in pID:
										if (cur_plan[0] + 1) in x:
											mycursor.execute("UPDATE table_user SET table_user.cur_plan=" + str(cur_plan[0] + 1) + " WHERE table_user.fb_id=" + str(recipient_id) + "")
											found = True
											break
									if not found:
										mycursor.execute("UPDATE table_user SET table_user.cur_plan=" + str(pID[0][0]) + " WHERE table_user.fb_id=" + str(recipient_id) + "")
									mydb.commit()
								elif 'help' in ans['entities']:
									send_message(recipient_id, "Hier findest du alle Befehle, die du mit WorkAut verwenden kannst: \n \ntausche * Übung *: Übung ändern \n \nanzeigen: Nächste Übung im Plan anzeigen \n \n* smiley *: Nächste Übung im Plan anzeigen \n \nbeenden: den aktuellen Plan beenden und mit dem nächsten fortfahren")
								else:
									send_message(recipient_id, "Diesen Befehl gibt es nicht, bitte schau doch in unsere Hilfe.")
							#-------------------------------------
							# for x in printex['exercise']:
								# send_message(recipient_id, x[0])
						# mycursor.execute("UPDATE table_user SET fb_id=" + str(recipient_id) + " WHERE uID=8")
						# mydb.commit()
						#response_sent_text = get_message()
						#send_message(recipient_id, response_sent_text)
					#if user sends us a GIF, photo,video, or any other non-text item
			# g.user = None
			# if 'pass' in session:
				# g.user = session['pass']
			# if g.user:
				# # get whatever message a user sent the bot
				# output = request.get_json()
				# for event in output['entry']:
					# messaging = event['messaging']
					# for message in messaging:
						# if message.get('message'):
							# #Facebook Messenger ID for user so we know where to send response back to
							# recipient_id = message['sender']['id']
							# print(recipient_id)
							# if message['message'].get('text'):
								# session['pass'] = request.form['Pass']
								# send_message(recipient_id, 'Bitte gib dein Passwort ein!')
								# #response_sent_text = get_message()
								# #send_message(recipient_id, response_sent_text)
							# #if user sends us a GIF, photo,video, or any other non-text item
							# if message['message'].get('attachments'):
								# response_sent_nontext = get_message()
								# send_message(recipient_id, response_sent_nontext)
				# else:
					# get whatever message a user sent the bot
	return "Message Processed"
				  
def choice(msg):
	if msg == "select":
		TPResp()
	if msg == "change":
		TPChange(ex)

#______________________________________________________________________________#
#______________________________TP Show_________________________________________#
#______________________________________________________________________________#

def TPShowFB(pID, fb_id):
	mycursor.execute("SELECT table_exercise.name, table_planex.sets, table_planex.reps FROM table_user INNER JOIN table_plan ON table_user.uID = table_plan.uID INNER JOIN table_planex ON table_plan.pID = table_planex.pID INNER JOIN table_exercise ON table_planex.eID = table_exercise.eID WHERE table_user.fb_id=" + str(fb_id) + " AND table_plan.pID='" + str(pID) + "' ORDER BY table_planex.position ASC ")
	printex['exercise'] = mycursor.fetchall()
	
#______________________________________________________________________________#
#______________________________TP CHANGE_______________________________________#
#______________________________________________________________________________#
	
def ChangeEx(ex, fb_id):
	altExes = TPSelEx(ex) #fb_id: 2020262244660563
	nex = ex
	while nex == ex:
		nex = random.choice(altExes)
	TPChange(nex[0], ex, fb_id)
	return nex[0]
	
def TPSelEx(ex):
	mycursor.execute("SELECT table_exercise.name FROM table_exercise WHERE table_exercise.subgrp=(SELECT table_exercise.subgrp FROM table_exercise WHERE table_exercise.name='" + ex + "')")
	altExes = mycursor.fetchall()
	return altExes
	
def TPChange(nex, ex, fb_id):
	mycursor.execute("SELECT table_plan.pID FROM table_user INNER JOIN table_plan ON table_user.uID=table_plan.uID WHERE table_user.fb_id=" + str(fb_id) + "")
	plans = mycursor.fetchall()
	for pID in plans:
		print(pID[0])
		mycursor.execute("UPDATE table_planex SET table_planex.eID=(SELECT table_exercise.eID FROM table_exercise WHERE table_exercise.name='" + nex + "') WHERE table_planex.eID=(SELECT table_exercise.eID FROM table_exercise WHERE table_exercise.name='" + ex + "') AND table_planex.pID=" + str(pID[0]) + "")
	mydb.commit()

#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#
	
def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

#chooses a random message to send to the user
def get_message():
    sample_responses = ["Hallo. Du hast ein Attachment gesendet. Das hat uns sehr gefreut", "SUUUPEEEER! Danke für dein Attachment. Oder auch Anhang.", "YEEEEY!", ":)"]
    # return selected item to the user
    return random.choice(sample_responses)

#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#

@app.route('/')
def index():
	if g.user:
		return render_template('Main.html')
	else:
		return redirect(url_for('login'))

#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#   
   
# Check Configuration section for more details
# SESSION_TYPE = 'redis'
# app.config.from_object(__name__)
# sess = Session()
# sess.init_app(app)

@app.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']
	# else:
		# return redirect(url_for('login'))

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')
   

@app.route('/login')
def login():
	session.pop('user', None)
	return render_template('Login.html')
   
#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#

@app.route('/start', methods=['POST'])
def start():
	mycursor.execute("SELECT username, pwd, uID, table_user.gender FROM table_user WHERE username='" + request.form['Username'] + "' AND pwd='" + request.form['Pass'] + "'")
	logindata = mycursor.fetchone()
	if logindata is None:
		return render_template('Login.html')
	else:
		session['user'] = request.form['Username']
		session['pass'] = request.form['Pass']
		session['uID'] = logindata[2]
		session['gender'] = logindata[3]
		return render_template('Main.html')
	
#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#

@app.route('/form_register')
def form_register():
	return render_template('Register.html')
   
#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#

@app.route('/register', methods=['POST'])
def register():
	pwd = request.form['regPass']
	pwdconf = request.form['regPassConf']
	gender = request.form['gender']
	print(gender)
	if( pwd == pwdconf):
		mycursor.execute("SELECT max(uID) FROM table_user")
		id = mycursor.fetchall()
		print(id[0][0]+1)
		mycursor.execute("INSERT INTO table_user(uID, username, gender, pwd) VALUES(" + str((id[0][0])+1) + ", '" + request.form['regUsername'] + "', " + str(request.form['gender']) + ", " + str(request.form['regPass']) + ")")
		mydb.commit()
		return render_template('Login.html')
	else:
		return render_template('Register.html')
#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#
   
@app.route('/test', methods=['POST', 'GET'])
def test():
	return render_template("test.html")
	
#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#
	
@app.route('/pageart', methods=['POST', 'GET'])
def pageart():
	return render_template('TPCreate.html')
	# pageart = string(request.form.get('pageart', 0))
	# data = {'pageart': pageart}
	# data = jsonify(data)
	# return data
	
#______________________________________________________________________________#	
#______________________________________________________________________________#
#______________________________________________________________________________#

@app.route('/TPSel', methods=['POST'])
def TPSel():
	#plansBEHINDERT=[ ["A", "B", "C", "D"], ["D", "C", "B", "A"], ["B", "C", "D", "A"], ["C", "D", "A", "B"]]
	#vorschlag1 = []
	goal = request.form['goal']
	tpw = request.form['tpw']
	mycursor.execute("SELECT table_group.gName FROM table_assign INNER JOIN table_group ON table_assign.gID=table_group.gID WHERE goal='"+goal+"' AND tpw="+tpw+" AND gender=" + str(session['gender']) + "")
	plans = mycursor.fetchall()
	#mycursor.execute("SELECT table_group.gName FROM table_assign INNER JOIN table_group ON table_assign.gID=table_group.gID WHERE goal='"+goal+"' AND tpw="+tpw+" AND gender=1")
	#plansBEHINDERT = mycursor.fetchall()
	#selPlan(1, goal, tpw)
	return render_template('TPSel.html', plans=plans)

#______________________________________________________________________________#	
#______________________________________________________________________________#
#______________________________________________________________________________#

@app.route('/SavePlans', methods=['POST'])
def SavePlans():
	delete()
	choice = request.args['choice']
	mycursor.execute("SELECT table_plan.pID, table_group.gID, table_plan.pName FROM table_group INNER JOIN table_plangroup ON table_group.gID=table_plangroup.gID INNER JOIN table_plan ON table_plangroup.pID=table_plan.pID WHERE table_group.gName='" + choice + "' AND table_plan.uID=0")
	pID = mycursor.fetchall()
	userPlans = {}
	startP = 0
	for planID in pID:
		mycursor.execute("SELECT table_exercise.name, table_planex.position, table_planex.reps, table_planex.sets, table_plan.pID, table_exercise.eID FROM table_plan INNER JOIN table_planex ON table_plan.pID=table_planex.pID INNER JOIN table_exercise ON table_planex.eID=table_exercise.eID WHERE table_plan.pID=" + str(planID[0]) + " ORDER BY table_planex.position ASC")
		userPlans[planID[2]]=mycursor.fetchall()
	for pName in userPlans:
		mycursor.execute("SELECT max(pID) FROM table_plan")
		maxPID = mycursor.fetchone()
		if startP == 0:
			startP = maxPID[0] + 1
		mycursor.execute("INSERT INTO table_plan(pID, pName, uID) VALUES(" + str(maxPID[0]+1) + ", '" + str(pName) + "', " + str(session['uID']) + ")")
		mycursor.execute("INSERT INTO table_plangroup(gID, pID) VALUES(" + str(pID[0][1]) + ", " + str(maxPID[0]+1) + ")")
		for exer in userPlans[pName]:
			mycursor.execute("INSERT INTO table_planex VALUES(" + str(maxPID[0]+1) + ", " + str(exer[5]) + ", " + str(exer[1]) + ", " + str(exer[2]) + ", " + str(exer[3]) + ")")
	mycursor.execute("UPDATE table_user SET cur_plan=" + str(startP) + " WHERE table_user.uID=" + str(session['uID']) + "")
	mycursor.execute("UPDATE table_user SET table_user.counter=0 WHERE table_user.uID=" + str(session['uID']) + "")
	mydb.commit()
	return render_template('TPShow.html', choice=choice, plans=userPlans)

#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#
	
def SavePlansFB(choice, recipient_id):
	deleteFB()
	mycursor.execute("SELECT table_user.uID FROM table_user WHERE table_user.fb_id=" + str(recipient_id) + "")
	userUID = mycursor.fetchone()
	uID = userUID[0]
	mycursor.execute("SELECT table_plan.pID, table_group.gID, table_plan.pName FROM table_group INNER JOIN table_plangroup ON table_group.gID=table_plangroup.gID INNER JOIN table_plan ON table_plangroup.pID=table_plan.pID WHERE table_group.gName='" + choice + "' AND table_plan.uID=0")
	pID = mycursor.fetchall()
	userPlans = {}
	startP = 0
	for planID in pID:
		mycursor.execute("SELECT table_exercise.name, table_planex.position, table_planex.reps, table_planex.sets, table_plan.pID, table_exercise.eID FROM table_plan INNER JOIN table_planex ON table_plan.pID=table_planex.pID INNER JOIN table_exercise ON table_planex.eID=table_exercise.eID WHERE table_plan.pID=" + str(planID[0]) + " ORDER BY table_planex.position ASC")
		userPlans[planID[2]]=mycursor.fetchall()
	for pName in userPlans:
		mycursor.execute("SELECT max(pID) FROM table_plan")
		maxPID = mycursor.fetchone()
		if startP == 0:
			startP = maxPID[0] + 1
		mycursor.execute("INSERT INTO table_plan(pID, pName, uID) VALUES(" + str(maxPID[0]+1) + ", '" + str(pName) + "', " + str(uID) + ")")
		mycursor.execute("INSERT INTO table_plangroup(gID, pID) VALUES(" + str(pID[0][1]) + ", " + str(maxPID[0]+1) + ")")
		for exer in userPlans[pName]:
			mycursor.execute("INSERT INTO table_planex VALUES(" + str(maxPID[0]+1) + ", " + str(exer[5]) + ", " + str(exer[1]) + ", " + str(exer[2]) + ", " + str(exer[3]) + ")")
	mycursor.execute("UPDATE table_user SET cur_plan=" + str(startP) + " WHERE table_user.uID=" + str(uID) + "")
	mycursor.execute("UPDATE table_user SET table_user.counter=0 WHERE table_user.uID=" + uID + "")
	mydb.commit()

#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#
	
def deleteFB(recipient_id):
	mycursor.execute("UPDATE table_user SET table_user.cur_plan=NULL WHERE table_user.fb_id=" + str(recipient_id) + "")
	mycursor.execute("SELECT table_plan.pID, table_user.uID FROM table_plan INNER JOIN table_user ON table_plan.uID=table_user.uID WHERE table_user.fb_id=" + str(recipient_id) + "")
	userPlans = mycursor.fetchall()
	if(userPlans != []):
		for plan in userPlans:
			mycursor.execute("DELETE FROM table_plangroup WHERE table_plangroup.pID=" + str(plan[0]) + "")
			mycursor.execute("DELETE FROM table_planex WHERE table_planex.pID=" + str(plan[0]) + "")
			mycursor.execute("DELETE FROM table_plan WHERE table_plan.uID=" + str(plan[1]) + " AND table_plan.pID=" + str(plan[0]) + "")
		mydb.commit()
	
#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#

@app.route('/TPShow', methods=['POST', 'GET'])
def TPShow():
	# ABFANGEN, wenn KEIN PLAN EXISTIERT
	userPlans = {}
	mycursor.execute("SELECT table_plan.pID, table_plan.pName, table_group.gName FROM table_group INNER JOIN table_plangroup ON table_group.gID=table_plangroup.gID INNER JOIN table_plan ON table_plangroup.pID=table_plan.pID WHERE table_plan.uID=" + str(session['uID']) + "")
	pID = mycursor.fetchall()
	for planID in pID:
		mycursor.execute("SELECT table_exercise.name, table_planex.position, table_planex.reps, table_planex.sets FROM table_plan INNER JOIN table_planex ON table_plan.pID=table_planex.pID INNER JOIN table_exercise ON table_planex.eID=table_exercise.eID WHERE table_plan.pID=" + str(planID[0]) + " AND table_plan.uID=" + str(session['uID']) + " ORDER BY table_planex.position ASC")
		userPlans[planID[1]] = mycursor.fetchall()
	return render_template('TPShow.html', choice=pID[0][2] , plans=userPlans)
	
#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#
	
def selPlan(gender, goal, tpw):
	plans = []
	mycursor.execute("SELECT gID FROM table_assign WHERE goal="+goal+" AND tpw="+str(tpw)+" AND gender="+str(gender)+" ")
	plans.append(mycursor.fetchone())
	print(plans[0][0])

#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#
	
def delete():
	mycursor.execute("UPDATE table_user SET table_user.cur_plan=NULL WHERE table_user.uID=" + str(session['uID']) + "")
	mycursor.execute("SELECT table_plan.pID FROM table_plan WHERE table_plan.uID=" + str(session['uID']) + "")
	userPlans = mycursor.fetchall()
	if(userPlans != []):
		for plan in userPlans:
			mycursor.execute("DELETE FROM table_plangroup WHERE table_plangroup.pID=" + str(plan[0]) + "")
			mycursor.execute("DELETE FROM table_planex WHERE table_planex.pID=" + str(plan[0]) + "")
			mycursor.execute("DELETE FROM table_plan WHERE table_plan.uID=" + str(session['uID']) + " AND table_plan.pID=" + str(plan[0]) + "")
		mydb.commit()

#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#
		
@app.route('/change')
def change():
	altEx = altExer(1, 1)
	for y in altEx:
		print(y)
	return render_template('Test.html')
	
#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#
	
@app.route('/datasecurity')
def datasecurity():
	return render_template('Richtlinien.html')
		
#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#
		
def altExer(musclegrp, subgrp):
	mycursor.execute("SELECT table_exercise.name FROM table_exercise WHERE muscleGrp=" + str(musclegrp) + " AND subGrp = " + str(subgrp) + "")
	altEx = mycursor.fetchall()
	return altEx

#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#


#______________________________________________________________________________#
#______________________________________________________________________________#
#______________________________________________________________________________#

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


# updater = Updater('YOUR TOKEN HERE')

# updater.dispatcher.add_handler(CommandHandler('hello', hello))

# updater.start_polling()
# updater.idle()
	
if __name__ == '__main__':
	app.run(debug=True)

# if __name__ == '__main__':
   # app.run(debug = True)

# from flask import Flask
# #from flask import render_template
# app = Flask(__name__)

# @app.route("/")
# def hello():
    # return render_template('Main.html')
	#return Main.html
	
