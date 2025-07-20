import imaplib


USER = ''
PASSWORD = ''
IMAP_HOST = 'outlook.office365.com'
PORT = 993
CATEGORY = 'Teste Python'
check = imaplib.IMAP4(IMAP_HOST, PORT)
check.login(USER, PASSWORD)
check.select()
check.search(CATEGORY)
print(check.fetch())
check.close()