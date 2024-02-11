from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail()

query_params = {
    'newer_than': (8, 'hour'),
    'older_than': (0,  'hour'),
    # 'unread': True,
}

messages = gmail.get_messages(query=construct_query(query_params))

# ...and many more easy to use functions can be found in gmail.py!

# Print them out!
print(len(messages))
for message in messages:
    print("To: " + message.recipient)
    print("From: " + message.sender)
    print("Subject: " + message.subject)
    print("Date: " + message.date)
    print("Preview: " + message.snippet)
    print("Message Body: " + message.plain)  # or message.html
