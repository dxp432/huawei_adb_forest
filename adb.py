import datetime
import time
from pykeyboard import PyKeyboard
import win32api
import win32con

# 定义鼠标键盘实例
k = PyKeyboard()


# 主函数
def main():

    # 打开支付宝蚂蚁森林操作
    def open_alipay():
        # 返回
        for i in range(5):
            hw_back()
        
        # 打开alipay
        copy_paste_2_cmd("adb shell input tap 750 1568")
        time.sleep(4)
        # # 打开蚂蚁
        # copy_paste_2_cmd("adb shell input tap 972 900")
        # time.sleep(4)
        # 打开蚂蚁
        copy_paste_2_cmd("adb shell input tap 963 535")
        time.sleep(4)

        # 收能量
        get()
        
        for i in range(2):
            # 找能量按钮
            copy_paste_2_cmd("adb shell input tap 982 1557")
            time.sleep(7)
            get_close()
            # 关掉小窗口
            copy_paste_2_cmd("adb shell input tap 540 1800")
            time.sleep(0.7)




    def get_close():
        copy_paste_2_cmd("adb shell input tap 184 834")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 149 756")
                
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 231 768")
                
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 200 678")
                
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 300 708")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 388 659")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 500 632")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 600 639")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 700 675")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 786 735")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 860 817")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 880 900")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 300 600")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 400 545")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 535 518")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 668 533")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 783 571")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 861 652")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 462 461")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        copy_paste_2_cmd("adb shell input tap 628 447")        
        # 关掉小窗口
        copy_paste_2_cmd("adb shell input tap 540 1800")
        time.sleep(0.3)
        time.sleep(1)



    def get():
        copy_paste_2_cmd("adb shell input tap 184 834")        

        copy_paste_2_cmd("adb shell input tap 149 756")
                

        copy_paste_2_cmd("adb shell input tap 231 768")
                

        copy_paste_2_cmd("adb shell input tap 200 678")
                

        copy_paste_2_cmd("adb shell input tap 300 708")        

        copy_paste_2_cmd("adb shell input tap 388 659")        

        copy_paste_2_cmd("adb shell input tap 500 632")        

        copy_paste_2_cmd("adb shell input tap 600 639")        

        copy_paste_2_cmd("adb shell input tap 700 675")        

        copy_paste_2_cmd("adb shell input tap 786 735")        

        copy_paste_2_cmd("adb shell input tap 860 817")        
 
        copy_paste_2_cmd("adb shell input tap 880 900")        

        copy_paste_2_cmd("adb shell input tap 300 600")        

        copy_paste_2_cmd("adb shell input tap 400 545")        

        copy_paste_2_cmd("adb shell input tap 535 518")        

        copy_paste_2_cmd("adb shell input tap 668 533")        

        copy_paste_2_cmd("adb shell input tap 783 571")        

        copy_paste_2_cmd("adb shell input tap 861 652")        

        copy_paste_2_cmd("adb shell input tap 462 461")        

        copy_paste_2_cmd("adb shell input tap 628 447")
        time.sleep(1)

    # 复制到cmd
    def copy_paste_2_cmd(my_string):
        k.type_string(my_string)
        enter()
        time.sleep(0.5)

    # enter
    def enter():
        win32api.keybd_event(0x0D, 0, 0, 0)
        win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)

    def hw_back():
        # 返回好多次
        copy_paste_2_cmd("adb shell input keyevent 4")
        time.sleep(2)

    i = 0
    while 1 == 1:
        mytime = datetime.datetime.now()
        print("现在时间（）：" + str(mytime.date())+ str(mytime.minute))
        time.sleep(4)
        # 支付宝
        if (mytime.hour == 6)  or (mytime.hour == 7) or (mytime.hour == 8)  or (mytime.hour == 9):
            i = 0
            # 返回好多次
            for i in range(7):
                hw_back()

            open_alipay()

            time.sleep(1)

        mytime = datetime.datetime.now()

        print("if outside _ timesleep。。。。。。。。")
        time.sleep(60)

main()