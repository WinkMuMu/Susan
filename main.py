#!/usr/local/bin/python3.8
# -*- coding: utf8 -*-
# 调用openai api的步骤
# 1. 安装openai库 pip install openai
# 2. 设置openai的api_key 
# 3. 调用openai的api
# 4. 参考文档
# https://platform.openai.com/docs/api-reference/completions/create
# https://platform.openai.com/docs/api-reference/authentication
# https://platform.openai.com/docs/api-reference/completions/create
# https://platform.openai.com/docs/libraries/community-libraries 
import os
import openai
import json
# 1. 准备好请求的url
#openai.organization = "YOUR_ORG_ID" # 
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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" #要更换成自已的API KEY
# 查看可以使用的模型列表
def get_model_list():
    models= openai.Model.list()
    print(models)
# 生成文本示例
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()
# 调用openai 画图示例
def generate_image(prompt):
    response = openai.Image.create(
        prompt = prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url
# 调用openai 问答示例
def chat(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content":prompt}
    ]
)
    answer = response.choices[0].message.content
    return answer
# 调用openai 改正错词输出正确句子
def correct():
    prompt="改正错词输出正确句子:\n\n我在京东电商平台买了苹果耳几和华为体脂称"  #建议prompt: 改正错词输出正确句子:\n\n input_sentence
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content":prompt}
    ]
)
    answer = response.choices[0].message.content
    return answer
# 调用openai 识别关键词
def keyword():
    prompt="对下面内容识别2个关键词，每个词字数不超过3个字:\n\n齐选汽车挂件车内挂饰车载后视镜吊坠高档实心黄铜玉石出入平安保男女 红流苏-玉髓平安扣"  #建议prompt: 对下面内容识别n个关键词，每个词字数不超过m个字:\n\n input data
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content":prompt}
    ]
)
    answer = response.choices[0].message.content
    return answer
# 抽取文本向量 (Embedding)
def embedding():
    content = '苹果手机'
    response = openai.Embedding.create(
    model="text-embedding-ada-002",
    input=content
)
    answer = response.data[0].embedding
    return answer
def api_test():
    # 测试chat 
    # prompt = "人口最多的国家?"
    # response = chat(prompt)
    # print(response)
# 
    # 测试generate_text
    # prompt = "Hello, how are you today?"
    # response = generate_text(prompt)
    # print(response) 
    # 测试generate_image
    #prompt = "a delicious dessert"
    #response = generate_image(prompt)
    #print(response)
    # 测试correct
    # response = correct()
    # print(response) #输出结果: 我在京东电商平台买了苹果耳机和华为体脂秤。
    # 测试keyword
    #response = keyword()
    #print(response) #输出结果: 挂件、平安扣
    # 测试embedding
    result = embedding()
    print(len(result))
    print(result)
if __name__ == '__main__':
    api_test()
