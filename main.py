import ast

import PySimpleGUI as sg

login_info = {}
vps = []


def find_vps():
    global vps
    with open('conf.json', 'r+', encoding='gbk') as c:
        d = c.read()
        login_info = ast.literal_eval(d)
        vps.append(login_info.keys())


def main():
    # 找到所有的vps信息
    find_vps()
    NAME_SIZE = 23

    def name(name):
        dots = NAME_SIZE - len(name) - 2
        return sg.Text(name + ' ' + '•' * dots, size=(NAME_SIZE, 1), justification='r', pad=(0, 0), font='Courier 10')

    layout_l = [[sg.Text('请选择需要连接的服务器'), sg.OptionMenu([*vps, ], s=(22, 2)), ],
                [sg.Output(s=(100, 20))],
                ]
    layout = [[sg.MenubarCustom([['文件', ['退出 ']], ['关于', ['关于软件', '关于作者']]], p=0)],

              [sg.Col(layout_l)]
              ]

    window = sg.Window('自用的简单服务器管理', layout)

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == '退出':
            break

        print('', values[0])

    window.close()


if __name__ == '__main__':
    main()
