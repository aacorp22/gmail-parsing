# -*- coding: utf-8 -*-
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# oauth2 authorization
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
creds = Credentials.from_authorized_user_file('token.json', SCOPES)

#connecting to Gmail Api and getting messages
with build('gmail', 'v1', credentials=creds) as service:
    request = service.users().messages()
    address = request.list(userId='me')
    messages = address.execute().get('messages')
    zayavki = []
    
    for msg in messages:
        data = request.get(userId='me',id = msg['id'])
        txt = data.execute()
        if (txt['snippet'][:12]) == 'Новая заявка':
            zayavki.append(txt['snippet'])
