from notion_client import Client
import os

# Initialize the client
# 取得token的方法，可以參考官方文件這邊 https://developers.notion.com/docs/getting-started
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
notion = Client(auth=NOTION_TOKEN)

database_id = os.environ["DATABASE_ID"]


def insert_to_notion(
    original_content: str,
    contents: list[str],
    course_name: str,
    teacher_name: str,
    sender: str,
    date: str
):
    # 這邊需要`DATABASE_ID`，可以在網頁版Notion點選page後，網址最後會有一個id，可以在這邊抓取
    # 例如 https://www.notion.so/natlee/test-4f3f55661c333e5585660c4c35e10533
    # 這邊的DATABASE_ID就是`4f3f55661c333e5585660c4c35e10533`

    created_page = notion.pages.create(
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
            "children": [],
        }
    )
    for content in contents:
        block_type = ""
        index = -1
        if len(content) == 0:
            continue
        if '#' in content:
            block_type = 'heading_3'
            index = content.find('#')
        elif '-' in content:
            block_type = 'bulleted_list_item'
            index = content.find('-')
        else:
            continue
        notion.blocks.children.append(
            created_page["id"],
            children=[
                {
                    "object": "block",
                    "type": block_type,
                    block_type: {
                        "rich_text": [{"type": "text", "text": {"content": content[index+1:]}}]
                    }
                }
            ]
        )
    notion.blocks.children.append(
        created_page["id"],
        children=[
            {
                "object": "block",
                "type": 'toggle',
                'toggle': {
                    "rich_text": [{"type": "text", "text": {"content": original_content}}]
                }
            }
        ]
    )


if __name__ == '__main__':
    # Replace the following variables with your actual data
    subject = "Your Subject"
    course_id = "Your Course ID"
    teacher_name = "nan"
    sender = "Your Sender"
    date = "2024-02-11"
    content = """   
    # Hello World
    - i am HAC
    """
    contents = content.split('\n')
    insert_to_notion(contents, subject, course_id, teacher_name, sender, date)
