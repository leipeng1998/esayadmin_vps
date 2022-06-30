import ast

with open('conf.json', 'r+') as c:
    d = c.read()
    print(d)
    login_info = ast.literal_eval(d)
    print(login_info)
