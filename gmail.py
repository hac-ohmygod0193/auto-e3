from gemini_agent import summarize_email
from simplegmail import Gmail
from simplegmail.query import construct_query
from notion import insert_to_notion
from get_course_info import get_course_info
gmail = Gmail()


def receive_email():
    query_params = {
        'newer_than': (25, 'day'),
        'older_than': (0,  'hour'),
        # 'unread': True,
        'sender': ['e3@nycu.edu.tw'],
        'exclude_sender': [['registra@nycu.edu.tw'], ['noreply@nycu.edu.tw']],
        # 'exclude_labels': [['To_Notion']]
    }
    messages = gmail.get_messages(query=construct_query(query_params))
    labels = gmail.list_labels()
    # To find a label by the name that you know (just an example):
    notion_label = list(filter(lambda x: x.name == 'To_Notion', labels))[0]
    print(len(messages))
    split_syb = '---------------------------------------------------------------------'
    filters = ['\"數位教學平台 E3\"', '\"E3數位教學平台\"', '\"E3 數位教學平台 公告\"']
    for message in messages:
        # message.mark_as_read()
        message.add_label(notion_label)

        # filter e3 announcement
        SENDER = message.sender.split(" <")
        if SENDER[0] in filters:
            continue
        print('From: ' + SENDER[0])
        print('Subject: ' + message.subject)
        print('Date: ' + message.date)
        summary = ""
        course_id = ""
        try:
            PLAIN = message.plain.split(split_syb)
            course_id = PLAIN[0].split()[0]
            summary = summarize_email(PLAIN[1])
        except:
            course_id = "NAN"
            summary = summarize_email(message.plain)
        if course_id[0] == '1':
            course_name, teacher_name = get_course_info(course_id)
        else:
            course_name = course_id
            teacher_name = 'NAN'
        contents = summary.split('\n')
        print('Course: ' + course_id)
        print('Summary: ' + summary)  # or message.html
        print('------------------------------------')
        insert_to_notion(contents, message.subject, course_name, teacher_name,
                         SENDER[0][1:-2], message.date)
