import json
import os

def agreement_score(data):
    entries = data.get(next(iter(data)))
    sum_list = []
    for prompt in entries:
        topic = prompt.get("topic")
        bot_1_prompt = prompt.get("bot_1_prompt")
        bot_2_prompt = prompt.get("bot_2_prompt")
        bot_1_opinions = prompt.get("bot_1_opinions")
        bot_2_opinions = prompt.get("bot_2_opinions")
        
        bot_1_agreement = 0
        num_statments = 0
        for statement in bot_1_opinions:
            num_statments += 1
            if statement[1] == "strongly agree":
                bot_1_agreement += 2
            elif statement[1] == "agree":
                bot_1_agreement += 1
            elif statement[1] == "disagree":
                bot_1_agreement -= 1
            elif statement[1] == "strongly disagree":
                bot_1_agreement -= 2
        prompt_sum = {  "Agreement Score": bot_1_agreement,
                        "num_statements": num_statments}
        sum_list.append(prompt_sum)

    total_statements = 0
    total_score = 0
    for p in sum_list:
        total_statements += int(p.get("num_statements"))
        total_score += int(p.get("Agreement Score"))
    return(total_score/total_statements)




def reply_length(data):
    entries = data.get(next(iter(data)))
    sum_list = []
    for prompt in entries:
        topic = prompt.get("topic")
        bot_1_prompt = prompt.get("bot_1_prompt")
        bot_2_prompt = prompt.get("bot_2_prompt")
        bot_1_opinions = prompt.get("bot_1_opinions")
        bot_2_opinions = prompt.get("bot_2_opinions")

        total_statement_length = 0
        num_statements = 0
        for statement in bot_1_opinions:
            num_statements += 1
            total_statement_length += len(statement[0].split(' '))
    return(total_statement_length/num_statements)





os.chdir('C:/Users/jackl/Desktop/5541/5541_HW5')

with open('cot_records_openai.json') as f:
    cot_openai = json.load(f)
f.close()
with open('cot_records.json') as f:
    cot = json.load(f)
f.close()
with open('zero_shot_record_openai.json') as f:
    zero_openai = json.load(f)
f.close()
with open('zero_shot_record.json') as f:
    zero = json.load(f)
f.close()
with open('few_shot_record.json') as f:
    few = json.load(f)
f.close()
with open('few_shot_record_openai.json') as f:
    few_openai = json.load(f)
f.close()

print("Agreement Score for zero shot Qwen: ", round(agreement_score(zero),3))
print("Agreement Score for zero shot OpenAI: ", round(agreement_score(zero_openai),3))
print("Agreement Score for few shot Qwen: ", round(agreement_score(few),3))
print("Agreement Score for few shot OpenAI: ", round(agreement_score(few_openai),3))
print("Agreement Score for CoT Qwen: ", round(agreement_score(cot),3))
print("Agreement Score for CoT OpenAI: ", round(agreement_score(cot_openai),3))

print("Average statement length for zero shot Qwen: ", round(reply_length(zero),3))
print("Average statement length for zero shot OpenAI: ", round(reply_length(zero_openai),3))
print("Average statement length for few shot Qwen: ", round(reply_length(few),3))
print("Average statement length for few shot OpenAI: ", round(reply_length(few_openai),3))
print("Average statement length for CoT Qwen: ", round(reply_length(cot),3))
print("Average statement length for CoT OpenAI: ", round(reply_length(cot_openai),3))