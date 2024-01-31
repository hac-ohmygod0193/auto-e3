import json
import requests


def get_course_info(course_id):

    semester, id = course_id.split('.')
    url = 'https://timetable.nycu.edu.tw/?r=main/getCrsOutlineBase'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-Hans;q=0.6,und;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_ga=GA1.3.1957543104.1704789579; _gid=GA1.3.1024676991.1706581568; _ga_968BJ0NDY6=GS1.3.1706581570.5.1.1706581571.0.0.0; PHPSESSID=0g07podss3v2u6vnavu7vdjdc2; Path=/; nctu_id=AAE7WPG5ZTtOyUUAAAAAADtfdnfRh3D7QhfQOyZn9ydOM3NBq2VNTs6ki0h5QmagOw==R_W5ZQ==2bggfTtrnxyh816TwrOK1IGDCRk=',
        'Host': 'timetable.nycu.edu.tw',
        'Origin': 'https://timetable.nycu.edu.tw',
        'Referer': 'https://timetable.nycu.edu.tw/?r=main/crsoutline&Acy=112&Sem=1&CrsNo=515021&lang=zh-tw',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Gpc': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    # Your data for the POST request
    data = {
        'acy': semester[:3],
        'sem': semester[3],
        'cos_id': id,
        'user': ''
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        # Decode the JSON string
        decoded_data = json.loads(response.text)
        # Print the decoded data
        return decoded_data['cos_name'], decoded_data['tea_name']
    else:
        print('Request failed. Status code:', response.status_code)
        return 'NAN', 'NAN'
