# E3 email summarizer

## 靈感來源
因為E3 email的訊息太亂太雜，希望能透過LLM統整、摘要重要訊息，並儲存在notion database上方便查閱。

## 執行方法
1. 將google makersuite api key填入gemini_agent.py
2. 將notion apiu以及想儲存到的database id填入notion.py
3. 執行下方程式
```python=
python3 main.py
```

## reference
[simplegmail](https://github.com/jeremyephron/simplegmail/tree/master)
[Get_course_info requests method](https://hackmd.io/@AndyChiang/DynamicCrawler#AJAX%E6%B3%95)
