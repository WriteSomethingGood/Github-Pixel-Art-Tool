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
    current_day = datetime.date(2018, 1, 27)
    timeline = convertMessage(message = 'H')
    for week in timeline:
      for weekday in week:
        current_day += datetime.timedelta(days = 1)
        if weekday != 1:
          continue
        if current_day != datetime.date(2018, 2, 11):
          continue
        committer.setDate(current_day)
        for idx in range(1):
          committer.gitAdd()
          committer.gitCommit()
    print(committer.gitPush(
      username = githubCredentials['username'],
      password = githubCredentials['password'],
      repositoryLink = 'https://github.com/WriteSomethingGood/Github-Pixel-Art-Tool'
    ))

main()
