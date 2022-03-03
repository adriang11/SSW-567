import requests
import json

def getInfo():
    print('Enter GitHub Username: ')
    x = input()
    r = requests.get('https://api.github.com/users/' + x + '/repos')

    repos = json.loads(r.text) #dictionary
    repoNames = []
    listOfCommits = []


    for count in repos:
        names = count['name']
        repoNames.append(names)
        listOfCommits.append(0)

    commitCount = [0] * len(listOfCommits)
    iter = 0

    for k in repoNames:
        r = requests.get('https://api.github.com/repos/' + x + '/' + k + '/commits')
        commits = json.loads(r.text)
        for num in commits:
            commitCount[iter] = commitCount[iter] + 1
        iter = iter + 1

    iter = 0

    for k in repoNames:
        print('Repo: ' + k + ' Number of commits: ' + str(commitCount[iter]))
        iter = iter + 1

if __name__ == "__main__":
    getInfo()