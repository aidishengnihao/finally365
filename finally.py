import time 

def pomodoro_timer(minutes):
    seconds = minutes * 60  # 将分钟数转换为秒数
    while seconds:
        mins, secs = divmod(seconds, 60)  # 将秒数转换为分和秒的组合
        timer = '{:02d}:{:02d}'.format(mins, secs)  # 格式化时间显示
        print(timer, end="\r")  # 在同一行中不断刷新时间
        time.sleep(1)  # 稍等一秒
        seconds -= 1  # 减少时间秒数
        
    print('时间到！')  # 时间结束提示
    
pomodoro_timer(25)  # 使用25分钟的专注时间
