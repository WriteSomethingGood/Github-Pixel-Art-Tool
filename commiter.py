import subprocess

class Committer:

  def __init__(self):
    self.setAutomaticSynchronization(False)
    self.setSSL(False)

  def __enter__(self):
    return self

  def __exit__(self, type, value, traceback):
    self.setAutomaticSynchronization(True)
    self.setSSL(True)

  def __runLocalCommand__(self, command):
    print(command)
    return subprocess.run(
      args = command,
      stdout = subprocess.PIPE,
      stderr = subprocess.STDOUT,
    )

  def gitAdd(self):
    with open('trash.txt', 'a') as file:
      file.write('.')
    command = [
      '/usr/bin/git',
      'add',
      '.'
    ]
    return self.__runLocalCommand__(command)

  def gitCommit(self):
    command = [
      '/usr/bin/git',
      'commit',
      '-m',
      '"."'
    ]
    return self.__runLocalCommand__(command)

  def gitPush(self, username, password, repositoryLink):
    command = [
      '/usr/bin/git',
      'push',
      (
        'https://'
        + username
        + ':'
        + password
        + '@'
        + repositoryLink
      )
    ]
    return self.__runLocalCommand__(command)

  def setAutomaticSynchronization(self, flag):
    command = [
      '/usr/bin/timedatectl',
      'set-ntp',
      str(flag)
    ]
    return self.__runLocalCommand__(command)

  def setDate(self, date):
    command = [
      '/usr/bin/timedatectl',
      'set-time',
      str(date)
    ]
    return self.__runLocalCommand__(command)

  def setSSL(self, flag):
    command = [
      '/usr/bin/git',
      'config',
      '--global',
      'http.sslverify',
      str(flag)
    ]
    return self.__runLocalCommand__(command)
