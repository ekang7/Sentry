import smtplib
carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send(message):
		# Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = '3123168528{}'.format(carriers['att'])
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

send ("FBI open up")