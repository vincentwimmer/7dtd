import time
import telnetlib
import random


HOST = "72.9.159.112"
password = "Pee-Pee-Poo-Poo-6969$420"

tn = telnetlib.Telnet(HOST, 27801)

if password:
	tn.read_until(b"Please enter password:")
	tn.write(b"Pee-Pee-Poo-Poo-6969$420\n")

# Static Settings
teeheematt = ['say "Matt you are doing it!"',
'say "Matt is the best at killing!"',
'say "OMG Matt save some zombies for the rest of us"',
'say "Look at big zombie killer Matt!"',
'say "Matt is so good at killing!"',
'say "Matt you are so brave!"',
'say "Matt you must keep killing to save the queen"',
'say "Oi Matt you almost spilled your tea!"',
'say "Matt is a killing machine!"']

# Place holder varibles
messageOnce15minRestartAlert = True
messageOnce10minRestartAlert = True
messageOnce5minRestartAlert = True
messageOnce2minRestartAlert = True
messageOnceRestartNotify = True

# Init Time
t = time.localtime()
current_time = time.strftime("%I:%M %p", t)
current_minute = time.strftime("%M", t)
current_hour = time.strftime("%I", t)
last_hour = current_hour
timecheck = 0

while True:
	try:
		whathappen = tn.read_some().decode('ascii')
		print(whathappen)

		if current_hour != last_hour:
			converToStr = str(time.strftime("%I:%M %p", t))
			timeString = str('say "Current real world time is: '+ converToStr+'"')
			converToByte = bytes(timeString, 'utf-8')
			tn.write(converToByte + b'\n\n')
			last_hour = current_hour

		#if ("led by CpuMatt" in str(whathappen)):
		#	converTeeHee = str(random.choice(teeheematt))
		#	convertedTeeHee = bytes(converTeeHee, 'utf-8')
		#	tn.write(convertedTeeHee + b'\n\n')

		if ("!rainonme" in str(whathappen)):
			tn.write(b"weather rain 1\n\n")
			time.sleep(0.1)
			tn.write(b"weather wind 1\n\n")
			time.sleep(1)
			tn.write(b'say "Rain begins to splish splash upon thee."\n\n')

		if ("!snowday" in str(whathappen)):
			tn.write(b"weather snow 1\n\n")
			time.sleep(0.1)
			tn.write(b"weather wind 1\n\n")
			time.sleep(0.1)
			tn.write(b"weather snowfall 1\n\n")
			time.sleep(1)
			tn.write(b'say "The snow smacks you in the face like a cold tortilla."\n\n')

		if ("!poofbegone" in str(whathappen)):
			tn.write(b"weather snow -1\n\n")
			time.sleep(0.1)
			tn.write(b"weather wind -1\n\n")
			time.sleep(0.1)
			tn.write(b"weather rain -1\n\n")
			time.sleep(0.1)
			tn.write(b"weather snowfall -1\n\n")
			time.sleep(1)
			tn.write(b'say "The skies clear because your makeup is too strong!"\n\n')

		if (int(current_hour) == 2) & (int(current_minute) == 15) & messageOnce15minRestartAlert == True:
			tn.write(b'say "Server Restart in 15min."\n\n')
			messageOnce15minRestartAlert = False
		elif ((int(current_hour) != 2) & (int(current_minute) != 15)):
			messageOnce15minRestartAlert = True

		if (int(current_hour) == 2) & (int(current_minute) == 20) & messageOnce10minRestartAlert == True:
			tn.write(b'say "Server Restart in 10min."\n\n')
			messageOnce10minRestartAlert = False
		elif ((int(current_hour) != 2) & (int(current_minute) != 20)):
			messageOnce10minRestartAlert = True

		if (int(current_hour) == 2) & (int(current_minute) == 25) & messageOnce5minRestartAlert == True:
			tn.write(b'say "Server Restart in 5min."\n\n')
			messageOnce5minRestartAlert = False
		elif ((int(current_hour) != 2) & (int(current_minute) != 25)):
			messageOnce5minRestartAlert = True

		if (int(current_hour) == 2) & (int(current_minute) == 28) & messageOnce2minRestartAlert == True:
			tn.write(b'say "Server Restart in 2min."\n\n')
			messageOnce2minRestartAlert = False
		elif ((int(current_hour) != 2) & (int(current_minute) != 28)):
			messageOnce2minRestartAlert = True

		if ((int(current_hour)/3).is_integer()) & messageOnceRestartNotify == True:
			tn.write(b'say "Server restarts at 2:30AM & PM."\n\n')
			messageOnceRestartNotify = False
		elif (int(current_minute) != 45):
			messageOnceRestartNotify = True

		if timecheck < 10:
			timecheck = timecheck + 1
		if timecheck == 10:
			t = time.localtime()
			current_time = time.strftime("%I:%M %p", t)
			current_minute = time.strftime("%M", t)
			current_hour = time.strftime("%I", t)
			timecheck = 0
	except:
			try: 
				time.sleep(60)
				tn = telnetlib.Telnet(HOST, 27801)
				tn.read_until(b"Please enter password:")
				tn.write(b"Pee-Pee-Poo-Poo-6969$420\n")
				timecheck = 0
			except:
				print("Can't connect...")
		
	time.sleep(0.05)
