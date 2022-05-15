import datetime
import PySimpleGUI as sg
import time 
import winsound

layout = [
    
    [sg.VPush()],
    [sg.Text('',size = (7,1),key = '-CURTIME-')],
    [sg.Text('Hour',size=(4,1),font = 'Calibra 15'),sg.Text('Min',size=(3,1),font = 'Calibra 15'),sg.Text('Sec',size=(3,1),font = 'Calibra 15')],
    [sg.Spin([i for i in range(24)],size=(4,2), key ='-HOUR-'),sg.Spin([i for i in range(60)],size=(4,2), key ='-MIN-'),sg.Spin([i for i in range(60)],size=(4,2),key ='-SEC-')],
    [sg.Text('',s=(1,1),font = 'Calibra 3',expand_x=True)],
    [sg.Text('When to wake you up',font = 'Calibra 10', border_width= 3,relief= 'solid')],
    [sg.Text('',s=(1,1),font = 'Calibra 3',expand_x=True)],
    [sg.Button('Set Alarm',p = 0)],
    [sg.Text('',size = (7,1),key = '-MSG-',expand_x = True)],
    [sg.Text('',size = (7,1),key = '-BOOM-',expand_x = True)],
    [sg.VPush()]
    ]

window = sg.Window('Alarm Clock', layout,size=(500,500),element_justification= 'center',scaling=2.5)

while True:
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    
    event, values = window.read(timeout=10)
    window['-CURTIME-'].update(now)
    hour = values['-HOUR-']
    minute = values['-MIN-']
    second = values['-SEC-']
    set_alarm_timer = f"{hour}:{minute}:{second}"
    if event == sg.WIN_CLOSED:
        break
    if event == 'Set Alarm':
        window['-MSG-'].update(f'The alarm has been set for {hour}:{minute}:{second}')
        window['-BOOM-'].update('')
    
    if now == set_alarm_timer:
        time.sleep(1)
        window['-BOOM-'].update('Wake uppp you lazy!')
        print('Wake uppp you lazy!') 
        winsound.PlaySound('PySimpleGUI/sfx_point.wav', winsound.SND_ASYNC) 
        
         
window.close()    