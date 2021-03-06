from __future__ import print_function

import os

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "
HINT = "\x1b[3;33m"

def main():

    project_name = '{{ cookiecutter.project_name }}'

    print(SUCCESS +
          "Your MongoDB Atlas AWS Lambda Project initialized successfully! You can now jump to the {} folder.".
          format(project_name) + "\n" +
          "\t    View all your deployments at: https://cloud.mongodb.com"
          + TERMINATOR)
    print(TERMINATOR)
    print(INFO +
          "{}/README.md contains instructions on how to proceed.".
          format(project_name) + TERMINATOR)


if __name__ == '__main__':
    main()
