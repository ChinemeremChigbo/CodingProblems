"""Download leetcode questions in leetcode_questions.json. On retrying, only download the missing ones."""

from time import sleep
from threading import Thread
from pathlib import Path
from subprocess import check_output
from json import loads, dump

response = loads(check_output("""curl 'https://leetcode.com/graphql/' \
  -H 'content-type: application/json' \
  --data-raw '{"query":"\\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\\n  problemsetQuestionList: questionList(\\n    categorySlug: $categorySlug\\n    limit: $limit\\n    skip: $skip\\n    filters: $filters\\n  ) {\\n    total: totalNum\\n    questions: data {\\n      acRate\\n      difficulty\\n      frontendQuestionId: questionFrontendId\\n      paidOnly: isPaidOnly\\n      title\\n      titleSlug\\n    }\\n  }\\n}\\n    ","variables":{"categorySlug":"algorithms","skip":0,"limit":5000,"filters":{}},"operationName":"problemsetQuestionList"}' \
  """, shell=True))


question_list = response['data']['problemsetQuestionList']
total_questions = question_list['total']
questions = question_list['questions']

p = Path('leetcode_questions.json')
all_questions = loads(p.read_bytes()) if p.exists() else {}

def saver():
    while True:
        sleep(5)
        with open(p, 'w') as f:
            while True:
                try:
                    dump(all_questions, f)
                except RuntimeError:
                    print("Runtime", end='\r')
                    continue
                break
        print(total_questions - len(all_questions), "remaining out of", total_questions, end='\r')
Thread(target=saver).start()

i = 1

def run(question):
    global i
    title_slug = question['titleSlug']

    cmd = """curl -s -S 'https://leetcode.com/graphql' \
      -H 'content-type: application/json' \
      --data-raw '{"operationName":"questionData","variables":{"titleSlug":\"""" + title_slug + """\"},"query":"query questionData($titleSlug: String\\u0021) {\\n  question(titleSlug: $titleSlug) {\\n    content\\n  }\\n}\\n"}' \
      --compressed"""
    i -= 1
    out = check_output(cmd, shell=True)
    i += 1

    response = loads(out)
    question['content'] = response['data']['question']['content']
    all_questions[title_slug] = question


for question in questions:
    while i < 0:
        sleep(0.1)
    title_slug = question['titleSlug']
    if question['paidOnly'] or title_slug in all_questions:
        continue
    Thread(target=lambda: run(question)).start()