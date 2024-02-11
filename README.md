# E3 email summarizer
## Star My Repo if you think it is useful, THX

**Orignal E3 mail**

<img width="252" alt="image" src="https://github.com/hac-ohmygod0193/auto-e3/assets/62164142/c820a901-104a-4759-905e-3110d3426682">

**Summarize Result**

<img width="289" alt="image" src="https://github.com/hac-ohmygod0193/auto-e3/assets/62164142/44446795-9f8d-438c-8db0-af975520f112">

## 靈感來源
因為E3 email的訊息太亂太雜，希望能透過LLM統整、摘要重要訊息，並儲存在notion database上方便查閱。

## Source of Inspiration
Due to the chaotic and cluttered nature of E3 emails, I hope to streamline and summarize important information using LLM, and store it in a Notion database for easy reference.

## Getting Start 
Clone all files to your
```
git clone https://github.com/hac-ohmygod0193/auto-e3.git
```
```
pip install -r requirements.txt
```
Here you need to paste your own secret key to enable the power of auto-e3
<img width="945" alt="image" src="https://github.com/hac-ohmygod0193/auto-e3/assets/62164142/51a2f931-9d80-4991-96be-f413c2c790a7">

### Setup Gmail secret token
1. Follow the instrustions from [setup tutorial source](https://github.com/jeremyephron/simplegmail?tab=readme-ov-file#getting-started)
**Remember** to set `Redirect URI in OAuth 2.0 Client IDs` to `http://localhost:8080/` 
<img width="364" alt="image" src="https://github.com/hac-ohmygod0193/auto-e3/assets/62164142/49acdd4e-c410-444b-808c-e1f97dcf2293">

2. After you finish step 6 above(download and rename the file as `client_secret.json`), Execute the code below
```python=
python3 setup_gmail_api.py
```

3. You will see the messeage like below in your terminal or just see a pop out webpage. Click and authorize with the account you apply for your gmail api.
<img width="722" alt="image" src="https://github.com/hac-ohmygod0193/auto-e3/assets/62164142/d9792146-cfba-4789-8535-617aa64481b8">

4. Copy the string in your gmail_token.json after step 4 and paste [here](https://www.base64encode.org/) to get encoded string.
<img width="689" alt="image" src="https://github.com/hac-ohmygod0193/auto-e3/assets/62164142/2518345a-876f-4ea0-84d6-70230dfbf82b">

5. New Repository secrets `Name` called `BASE64_GMAIL_TOKEN` and paste the encoded base64 string to `Secret` below
<img width="596" alt="image" src="https://github.com/hac-ohmygod0193/auto-e3/assets/62164142/4595a3fc-695b-4fda-bf20-01090a6be3e9">

### Setup Notion secret token
1. Follow the instructions from [here](https://github.com/ramnes/notion-sdk-py?tab=readme-ov-file#usage)

2. **Make Sure you create a new page** in your notion as `database` instead of `page`

3. **Make Sure you add connection to your notion api you just create**
<img width="779" alt="image" src="https://github.com/hac-ohmygod0193/auto-e3/assets/62164142/07fc706a-4c99-47cb-a38b-e3797eac7345">

4. New Repository secrets `Name` called `DATABASE_ID` and paste your id of your notion database to `Secret` below
> You need `DATABASE_ID` here, which can be obtained from the web version of Notion by clicking on the page. 
> At the end of the URL, there will be an ID that you can grab here.
> For example, in https://www.notion.so/ohmygod0193/test-4f3f55661c333e5585660c4c35e10533
> `4f3f55661c333e5585660c4c35e10533` is the DATABASE_ID.

5. New Repository secrets `Name` called `NOTION_TOKEN`

6. Paste the notion api your create with **step 1** to `Secret` below

### Setup Gemini APi secret token
1. Head over to makersuite.google.com/app/apikey [visit](https://makersuite.google.com/app/apikey) and sign in with your Google account.

2. Under API keys, click the “Create API key in new project” button.
![image](https://github.com/hac-ohmygod0193/auto-e3/assets/62164142/26c6a39c-3ef4-4e7f-a10f-09b25a8df063)

3. generate google gemini api key
4. Copy the API key and keep it private. Do not publish or share the API key publicly.
![image](https://github.com/hac-ohmygod0193/auto-e3/assets/62164142/9f6ccf15-9fec-41e9-9e32-a1c1c8776679)

5. New Repository secrets `Name` called `GOOGLE_API_KEY` and paste the API key to `Secret` below

## Deploy scheduled bot with Github Actions
1. Create a `.github/workflows` directory in your repository on GitHub if this directory does not already exist.
2. In the `.github/workflows` directory, create a file named `actions.yml`. For more information, see "Creating new files."
3. Copy my actions.yml [here](https://github.com/hac-ohmygod0193/auto-e3/blob/main/.github/workflows/actions.yml)
<img width="952" alt="image" src="https://github.com/hac-ohmygod0193/auto-e3/assets/62164142/4b7685bc-bdbd-44ba-8c08-0acc230dbb6e">

4. You can set up your desired running schedule by changing this line `- cron: `0 */3 * * *` # run every 3 hours`. For more crontab settings , see [here](https://crontab.guru/)

## Run it locally 
If you want to run it locally on your desktop or laptop.
Just replace 
1. `os.environ["NOTION_TOKEN"]` `os.environ["DATABASE_ID"]` in `notion.py`
2. `os.environ["GOOGLE_API_KEY"]` in `gemini_agent.py`

And Keep your `gmail_token.json` file under same directory with gmail.py

## Reference
[simplegmail](https://github.com/jeremyephron/simplegmail/tree/master)
[Get_course_info requests method](https://hackmd.io/@AndyChiang/DynamicCrawler#AJAX%E6%B3%95)
[How to access gemini model](https://beebom.com/how-use-google-gemini-api-key/)
[notion-client-api](https://github.com/ramnes/notion-sdk-py?tab=readme-ov-file#usage)
