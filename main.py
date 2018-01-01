import datetime
import json
from commiter import Committer
from read_message import convertMessage

def read_json(filepath):
  with open(filepath, 'rb') as file:
    return json.load(file, encoding = 'utf-8')

def main():
  githubCredentials = read_json(
    '/home/gardusi/github/credentials.json'
  )
  with Committer() as committer:
    i = 0
    j = -1
    flag = False
    current_day = datetime.date(2017, 12, 31)
    timeline = convertMessage(message = 'HIRE ME! DEV 4FUN')
    while True:
      current_day += datetime.timedelta(days = 1)
      if current_day > datetime.date(2018, 12, 31):
        break
      if current_day >= datetime.date(2018, 1, 28):
        j += 1
        if j == len(timeline[i]):
          j = 0
          i += 1
        if timeline[i][j] == 1:
          continue
      committer.setDate(current_day)
      for idx in range(105):
        committer.gitAdd()
        committer.gitCommit()
      print(committer.gitPush(
        username = githubCredentials['username'],
        password = githubCredentials['password'],
        repositoryLink = 'github.com/WriteSomethingGood/Github-Pixel-Art-Tool'
      ))

main()