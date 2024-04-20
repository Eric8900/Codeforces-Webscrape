import requests
import json
from bs4 import BeautifulSoup

with open('links.json', 'r') as f:
    d = f.read()
    
links = json.loads(d)

problems = []

#problem statement, input, output, time limit, memory limit, tag
i = 0
for link in links:
    res = requests.get("https://codeforces.com" + link)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        problem_statement = soup.find("div", class_="problem-statement")
        if not problem_statement:
            continue
        prob_state = problem_statement.get_text().replace("$$$", "")
        
        inp = problem_statement.find("div", class_="input")
        if not inp:
            continue
        out = problem_statement.find("div", class_="output")
        if not out:
            continue
        input1 = inp.get_text().replace("Input\n", "")
        output = out.get_text().replace("Output\n", "").replace("\n", " ")

        tl = problem_statement.find("div", class_="time-limit")
        if not tl:
            continue
        time_limit = tl.get_text().replace("time limit per test", "")
        ml = problem_statement.find("div", class_="memory-limit")
        if not ml:
            continue
        memory_limit = ml.get_text().replace("memory limit per test", "")
        
        
        tags = soup.find_all("span", class_="tag-box")
        if not tags:
            continue

        tags1 = []
        for t in tags:
            tags1.append(t.get_text().replace("\r\n", "").strip())

        di = dict(
            problem_statement = prob_state,
            input = input1,
            output = output,
            time_limit = time_limit,
            memory_limit = memory_limit,
            tags = tags1
        )
        problems.append(di)
    print(i)
    i += 1

data = json.dumps(problems)

with open('problems.json', 'w') as f:
    f.write(data)