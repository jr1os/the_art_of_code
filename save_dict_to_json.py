# save file dict to file json

import json

programming = {'language': [{'name': 'python', 'version': '3.8.0'}, {'name': 'golang', 'version': '1.18'}, {'name': 'javascript', 'version': 'es6'}, {'name': 'php', 'version': '7.1.2'}], 'ides': ['vscode', 'eclipse', 'netbeans ide', 'pycharm', 'phpstorm']}


with open('programming.json', 'w') as file:
    json.dump(programming, file, indent=4, sort_keys=True)
