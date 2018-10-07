import datetime
import json
from commiter import Committer
from read_message import convertMessage

def read_json(filepath):
  with open(filepath, 'rb') as file:
    return json.load(file, encoding = 'utf-8')

def main():
  githubCredentials = read_json(
    '/home/pediogo/Github-Pixel-Art-Tool/credentials.json'
  )
  with Committer() as committer:

    current_day = datetime.date(2018, 10, 6)
    timeline = convertMessage(message = 'ME')

    for week in timeline:
      for weekday in week:
        current_day += datetime.timedelta(days = 1)
        if weekday != 1:
          continue
        committer.setDate(current_day)
        for idx in range(30):
          committer.gitAdd()
          committer.gitCommit()
    print(committer.gitPush(
      username = githubCredentials['username'],
      password = githubCredentials['password'],
      repositoryLink = 'github.com/WriteSomethingGood/Github-Pixel-Art-Tool'
    ))

main()
