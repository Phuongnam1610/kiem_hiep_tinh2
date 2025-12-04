from struct import pack
from main import *
from PyQt5.QtCore import QThread
from file import *
import time

tools = []
threads = []


def Ham():
    """Khởi động tất cả các thread tools"""
    for i in tools:
        i.terminate()
    for i in tools:
        i.start()


def stoptool():
    """Dừng tất cả các thread tools"""
    for i in tools:
        i.terminate()


class MyThread(QThread, toolLQ):
    """Thread class kế thừa từ QThread và toolLQ để xử lý đa luồng"""

    def __init__(self, u, udid,  index, packtk):
        super().__init__(udid=udid, index=index, packtk=packtk)
        self.u = u

    def run(self):
        """Phương thức chạy thread - gọi main() từ toolLQ"""
        self.main()


def resetLD(devices):
    """Reset và khởi tạo lại các thread cho danh sách devices"""
    listtd = open("listtd.txt", encoding='utf-8').readlines()
    listtk = open("listtk.txt", encoding='utf-8').readlines()
    # listmap = open("listmap.txt", encoding='utf-8').readlines()
    tools.clear()
    
    for index, v in enumerate(devices):
        try:
            values = listtd[index].strip().split()
            coordinates = []
            tkmk = listtk[index].strip().split()
            
            for i in range(0, len(values), 2):
                x = int(values[i])
                y = int(values[i+1])
                coordinates.append([x, y])
            
        except Exception as e:
            coordinates = [[300, 500]]
            tkmk = ("A", "B")
            print(f"chua co toa do may {v}: {e}")
        
        a = MyThread(0, v, index=coordinates, packtk=tkmk)
        tools.append(a)


last_reset_time = 0


class RestartThread(QThread):
    """Thread riêng để xử lý logic restart định kỳ"""
    
    def __init__(self):
        super().__init__()
        self.running = True
    
    def run(self):
        """Chạy logic restart trong thread riêng"""
        global last_reset_time
        while self.running:
            current_time = time.time()
            if current_time - last_reset_time >= 12 * 60 * 60:
                restartLD(somayld)
                stoptool()
                devices = get_connected_devices()
                print(devices)
                resetLD(devices)
                Ham()
                last_reset_time = current_time
        else:
            time_left = 12 * 60 * 60 - (current_time - last_reset_time)
            print(f"Restarting in {time_left} seconds")
            time.sleep(1)
    
    def stop(self):
        """Dừng thread"""
        self.running = False


if __name__ == "__main__":
    restart_thread = RestartThread()
    restart_thread.start()
    restart_thread.wait()

