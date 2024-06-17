
#这个.py的目的是对部署在服务器的大模型发起http请求，响应之后接受返回的结果。最后根据结果修改游戏中装有台词的lua
import sys
import requests
import json
import re
def my_function():
    # 执行你的任务
    url = 'http://localhost:6789/chat/chat'
    payload = {

      "query": "我在哪",
      "conversation_id": "",
      "history_len": 5,
      "history": [
        {
          "role": "user",
          "content": "我……我怎么死了？!吓死我了，你是什么鬼？"
        },
        {
          "role": "assistant",
          "content": "我确实是鬼，但你可不是被我给吓死的.我在阎王爷那工作，现在来接你去阴曹地府"
        }
      ],
      "stream": 'false',
      "model_name": "chatglm3-6b",
      "temperature": 0.2,
      "max_tokens": 100,
      "prompt_name": "test"

            }

# 发送POST请求
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        #print("请求成功！")
        # dictionary = json.loads(response.text)
        # print("响应内容：", dictionary)
        data = response.text[6:]
        dic = json.loads(data)
        #print(dic['text'])
        return dic['text']
        #print(response.text)
    else:
        print("请求失败：", response.status_code)

if __name__ == "__main__":
    #print(my_function(sys.argv[1], sys.argv[2]))
    #my_function(sys.argv[1], sys.argv[2])
    result=my_function()
    with open('0.lua', 'r', encoding='utf-8') as f:
        # 逐行读取文件，直到读取到第3行
        line = f.readline()
    positions = [match.start() for match in re.finditer('"', line)]
    str = "早上"
    line = line[:positions[0] + 1] + str + line[positions[1]:]
    print(line)
    # 打印第1行
    with open("0.lua", "r+", encoding='utf-8') as f:
        # 将文件指针移动到文件的开头
        f.seek(0)
        # 写入内容
        f.write(line)
        f.flush()


# 定义一个字符串


# 使用正则表达式查找双引号的位置

# with open('0.lua', 'r',encoding='utf-8') as f:
#     # 逐行读取文件，直到读取到第3行
#     line = f.readline()
# positions = [match.start() for match in re.finditer('"', line)]
# str = "早上"
# line = line[:positions[0] + 1] + str + line[positions[1]:]
# print(line)
#     # 打印第1行
# with open("0.lua", "r+",encoding='utf-8') as f:
#     # 将文件指针移动到文件的开头
#     f.seek(0)
#     # 写入内容
#     f.write(line)
#     f.flush()



