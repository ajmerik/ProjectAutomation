# Type into terminal:
#       create [enter folder name]

import sys
import os
from github import Github

path = "[enter the path you want to create directory]"

username = "[enter your username here]"
password = "[enter your password here]"

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Succesfully created repository {}".format(sys.argv[1]))

if __name__ == "__main__":
    create()
