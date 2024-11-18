import common
url = 'http://localhost:1234/v1/chat/completions'


def detect(message, model, port_override = False):
    

    if port_override != False:
        local_url = 'http://localhost:' , port_override , '/v1/chat/completions'
    else:
        local_url = url


    template = """
    You are an AI that finds out whether or not there is an Emergency. You will receive the messages that include things that have to do with medical scnearios. 
    You will recieve messages about medical patients and things that patients might be saying. 
    Your task is to figure out when there is an issue with the situation that puts the patient or the nurse in danger. 
    For every prompt you are given, only answer with a 0 or 1.
    0 Means there is no Emergency, and 1 means someone's life might be in danger.
    Answer with 0 if this is a normal situation.
    Answer with 1 if someone's life is in danger.
    0 Means Safe
    1 Means Danger
    if the human is calling for help the answer is always 1
    ***Only answer with 0 or 1***
    """


    messages = [{'role': 'system', 'content': template},
                {'role': 'user', 'content': 'Hes not waking up, no matter what I do!'},
                {'role': 'assistant', 'content': '1'},
                # {'role': 'user', 'content': 'Sometimes I feel so alone in this journey'},
                # {'role': 'assistant', 'content': '0'},
                {'role': 'user', 'content': 'He suddenly cant move the left side of his body.'},
                {'role': 'assistant', 'content': '1'},
                {'role': 'user', 'content': 'What are some tips for creating a memory book?'},
                {'role': 'assistant', 'content': '0'},
                {'role': 'user', 'content': 'Shes talking about ending her life.'},
                {'role': 'assistant', 'content': '1'},
                {'role': 'user', 'content': 'How can I manage my own health while caregiving?'},
                {'role': 'assistant', 'content': '0'},
                {'role': 'user', 'content': 'Sometimes I feel like Im losing myself in this'},
                {'role': 'assistant', 'content': '0'},
                {'role': 'user', 'content': 'Hes coughing up blood.'},
                {'role': 'assistant', 'content': '1'},
                # {'role': 'user', 'content': 'Sometimes I feel like Im walking on eggshells'},
                # {'role': 'assistant', 'content': '0'},
                {'role': 'user', 'content': 'Shes having a severe asthma attack and her inhaler isnt helping.'},
                {'role': 'assistant', 'content': '1'},
                {'role': 'user', 'content': 'I am feeling hungry, lets order some steak.'},
                {'role': 'assistant', 'content': '0'},
                # {'role': 'user', 'content': 'What are some strategies for managing hallucinations calmly?'},
                # {'role': 'assistant', 'content': '0'},
                # {'role': 'user', 'content': 'I never knew love could hurt this much'},
                # {'role': 'assistant', 'content': '0'},
                # {'role': 'user', 'content': 'The nights are the hardest when she gets confused'},
                # {'role': 'assistant', 'content': '0'},
                {'role': 'user', 'content': message}]
    json={"model": model, 
          "messages": messages,
          "temperature": 0,
          "top_p": 1.0
          }



    return request(local_url,json, 1)
    

def request(url, json, count):
    if count < 3:
        response = common.sendRequest(url,json)
        
        if 'choices' in response:
            message = response['choices'][0]['message']['content']
            message = message.strip()
            if message == '0' or message == '1':
                return {"result":"success", "response": message}
            else:
                request(url, json, count+1)
        else:
            return {"result":"error", "response": 0}
    else:
        return {"result":"error", "response": 0}