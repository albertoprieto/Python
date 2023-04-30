import email
from email.header import decode_header
import imaplib
import base64
import datetime
from datetime import date, timedelta
import os.path

#Set ukey & pkey in base64
folder_name='dowloads'
ukey = ''
ukey64 = ukey.encode('ascii')
ukeybytes = base64.b64decode(ukey64)
base64.b64decode(ukey64)
ukeydecode = ukeybytes.decode('ascii')
pkey = ''
pkey64 = pkey.encode('ascii')
pkeybytes = base64.b64decode(pkey64)
pkeydecode = pkeybytes.decode('ascii')

#Set days variable to the days you want to download
today = datetime.date.today()
yesterday = datetime.date.today() - timedelta(days=0)
yesterday = yesterday.strftime('%d') + '-' + yesterday.strftime('%b') + '-' + yesterday.strftime('%Y')
yesterday = '(SINCE ' + '"' + yesterday + '"' + ')'

#Set your imap domain & mailbox
imap = imaplib.IMAP4_SSL('')
imap.login('{}'.format(ukeydecode),'{}'.format(pkeydecode))
status, messages = imap.select('INBOX')
mailboxToRead=['INBOX','INBOX.spam']

for mensajes in mailboxToRead:
	status, messages = imap.select(mensajes)
	(retcode, messages) = imap.search(None, yesterday)
	
	if retcode == 'OK':
		for num in messages[0].split() :
			response, msg = imap.fetch(num, '(RFC822)')
			for response in msg:
				if isinstance(response, tuple):
					msg = email.message_from_bytes(response[1])
					try:
						subject, encoding = decode_header(msg['Subject'])[0]
						From, encoding = decode_header(msg.get('From'))[0]
						emisor = msg.get('From').split('<')[1].split('>')[0]
					except:
						subject= ''
						From = ''
						emisor = ''

					if isinstance(From, bytes):
						From = From.decode(encoding)
					
					if From != '':
						if msg.is_multipart():
							for part in msg.walk():
								content_type = part.get_content_type()
								content_disposition = str(part.get('Content-Disposition'))

								if content_type == 'text/plain' and 'attachment' not in content_disposition:
									pass
								elif 'attachment' in content_disposition:
									filename = part.get_filename()
									if filename.endswith('.pdf'):
										if not os.path.isdir(folder_name):
											os.mkdir(folder_name)
										filepath = os.path.join(folder_name, filename)
										print('Downloadig',filename,'from',From)
										open(filepath, 'wb').write(part.get_payload(decode=True))
