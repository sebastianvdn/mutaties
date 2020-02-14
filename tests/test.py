import json

with open('tests/data.json') as f:
    data = json.load(f)

for key, value in data.items():
    for item in value:
        with open('tests/data.txt', 'a') as txt_file:
            txt_file.write(f"\n\n{item['date']}")
            txt_file.write(
                f"\npolicy: {item['policy']}\ncomment: {item['comment']}\nadmin: {item['admin']}\nGPO: {item['gpo']}"
                )
