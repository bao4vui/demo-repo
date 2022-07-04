# import PySimpleGUI as sg

# sg.theme("DarkBlue3")

# newlist = [[f"Cell ({row+1}, {col+1})" for col in range(8)] for row in range(10)]
# COL_HEADINGS = ["Date", "Ref", "ID", "Owner", "Customer", "Price", "Size", "Path"]
# layout = [
#     [sg.Table(values=newlist, headings=COL_HEADINGS, max_col_width=25,
#         num_rows=10, alternating_row_color='green', key='-TABLE-',
#         enable_events=True, justification='center',)],
#     [sg.Text("", size=(50, 1), key='-Position-')]
# ]

# window = sg.Window('Table', layout, finalize=True)
# table = window['-TABLE-']
# table.bind('<Button-1>', "Click")
# position = window['-Position-']
# position.expand(expand_x=True)

# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#     elif event == '-TABLE-':
#         pass
#     elif event == '-TABLE-Click':
#         e = table.user_bind_event
#         region = table.Widget.identify('region', e.x, e.y)
#         if region == 'heading':
#             row = 0
#         elif region == 'cell':
#             row = int(table.Widget.identify_row(e.y))
#         elif region == 'separator':
#             continue
#         else:
#             continue
#         column = int(table.Widget.identify_column(e.x)[1:])
#         position.update(f"Table clicked at ({row}, {column})")
        
# window.close()

import PySimpleGUIQt as sg

# Design pattern 1 - First window does not remain active

layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)],
          [sg.Text(size=(15,1),  key='-OUTPUT-')],
          [sg.Button('Launch 2')]]

win1 = sg.Window('Window 1', layout)
win2_active=False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == sg.WIN_CLOSED:
        break
    win1.FindElement('-OUTPUT-').update(vals1[0])

    if ev1 == 'Launch 2'  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse
                   [sg.Button('Exit')]]

        win2 = sg.Window('Window 2', layout2)
        while True:
            ev2, vals2 = win2.read()
            if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                win2.close()
                win2_active = False
                win1.UnHide()
                break