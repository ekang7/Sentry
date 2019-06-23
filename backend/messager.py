import smtplib
carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send(message, number=8472121483, carrier='att'):
		# Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = str(number) + '{}'.format(carriers[carrier])
	auth = ('sentry.chicagoalerts@gmail.com', 'windycity2019')

	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		max_limit_in_bytes = int(server.esmtp_features['size'])
		print(max_limit_in_bytes)
		server.starttls()
		server.login('sentry.chicagoalerts@gmail.com', 'windyhacks2019')
		message = 'Subject: {}\n\n{}'.format('Sentry Alert', message)
		server.sendmail ('sentry.chicagoalerts@gmail.com', to_number, message)
		server.quit()
		print("Success: Email sent!")
	except:
		print("Email failed to send.")


from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC10c93e8cf2acd053202972f6ae7f6723"
# Your Auth Token from twilio.com/console
auth_token  = "a4e420e8109d0e57de9ebbfa57b1b93e"

client = Client(account_sid, auth_token)

def send_message (phone, msg):
	message = client.messages.create (to=phone, from_="+12248777304", body=msg)
	print(message.sid)
