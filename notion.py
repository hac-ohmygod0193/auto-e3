from notion_client import Client

# Initialize the client
# 取得token的方法，可以參考官方文件這邊 https://developers.notion.com/docs/getting-started
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
notion = Client(auth=NOTION_TOKEN)

database_id = os.environ["DATABASE_ID"]

def insert_to_notion(
    contents,
    subject: str,
    course_name: str,
    teacher_name: str,
    sender: str,
    date: str
):
    # 這邊需要`DATABASE_ID`，可以在網頁版Notion點選page後，網址最後會有一個id，可以在這邊抓取
    # 例如 https://www.notion.so/natlee/test-4f3f55661c333e5585660c4c35e10533
    # 這邊的DATABASE_ID就是`4f3f55661c333e5585660c4c35e10533`

    notion.pages.create(
        **{
            "parent": {"database_id": database_id},
            "properties": {
                # 標題的屬性跟標題是什麼
                "Subject": {"title": [{"type": "text", "text": {"content": subject}}]},
                # 標籤的屬性跟標籤是什麼
                "Course": {"type": "multi_select", "multi_select": [{"name": course_name}]},
                "Teacher": {"type": "multi_select", "multi_select": [{"name": teacher_name}]},
                "Sender": {"type": "multi_select", "multi_select": [{"name": sender}]},
                # 建立時間，我的例子是使用像這樣的資料 `2022-04-21`
                "Received time": {"date": {"start": date}},
            },
            "children": [  # 這邊比較麻煩，要指定內容是哪種屬性，例如paragraph
                {
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {
                        # 內文的屬性跟內容

                        "rich_text": [{"type": "text", "text": {"content": content}}]
                    },
                }for content in contents
            ],
        }
    )


if __name__ == '__main__':
    # Replace the following variables with your actual data
    subject = "Your Subject"
    course_id = "Your Course ID"
    sender = "Your Sender"
    date = "2022-04-21"
    content = "Your Content hello"
    contents = content.split()
    insert_to_notion(contents, subject, course_id, sender, date)
