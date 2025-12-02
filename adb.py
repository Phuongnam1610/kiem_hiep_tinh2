import time
import cv2 
import numpy as np
import imutils
import subprocess
import os
import logging
import os
import requests,datetime
import random
# Tạo thư mục logs nếu chưa có
if not os.path.exists("logs"):
    os.makedirs("logs")

# Cấu hình logging
logging.basicConfig(
    filename="logs/tool.log",             # File log
    filemode="a",                         # "a" = append, "w" = ghi đè
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG                   # Mức log tối thiểu
)

def get_cpu_id():
    try:
        output = subprocess.check_output('wmic cpu get ProcessorId', shell=True)
        lines = output.decode().splitlines()
        cpu_id = next((line.strip() for line in lines if line.strip() and "ProcessorId" not in line), None)
        return cpu_id
    except Exception as e:
        raise Exception(f"Lỗi khi lấy CPU ID: {e}")

def check_machine_id(blocked_id="BFEBFBFF000306A9"):
    cpu_id = get_cpu_id()
    print(f"CPU ID máy hiện tại: {cpu_id}")
    logging.info(f"CPU ID máy hiện tại: {cpu_id}")

    if cpu_id and cpu_id.lower() != blocked_id.lower():
        raise Exception("Thiết bị không được phép chạy chương trình này.")

def auth(key):
    """
    Authenticate user based on license key and expiration date using Google's time API
    """
    try:
        # Get current time from Google's servers
        response = requests.get("https://www.google.com", timeout=5)
        server_time = response.headers['date']
        today = datetime.datetime.strptime(server_time, '%a, %d %b %Y %H:%M:%S %Z')
        #Cam4
        # license_keys = {
        #     "pjk": datetime.date(2025, 5, 4),
        #     "ayh": datetime.date(2025, 6, 8),    # 35 days from May 4
        #     "gcv": datetime.date(2025, 7, 13),   # 35 days from June 8
        #     "xfh": datetime.date(2025, 8, 17),   # 35 days from July 13
        #     "a12": datetime.date(2025, 9, 21),   # 35 days from Aug 17
        #     "wuk": datetime.date(2025, 10, 26),  # 35 days from Sept 21
        #     "ool": datetime.date(2025, 11, 30),  # 35 days from Oct 26
        #     "pfg": datetime.date(2026, 1, 4),    # 35 days from Nov 30
        #     "kuu": datetime.date(2026, 2, 8),    # 35 days from Jan 4
        #     "igf": datetime.date(2026, 3, 15),   # 35 days from Feb 8
        #     "uưe": datetime.date(2026, 4, 19)    # 35 days from Mar 15
        # }
        #Cam3
        # license_keys = {
        #     "hjk": datetime.date(2025, 5, 4),
        #     "tyh": datetime.date(2025, 6, 8),    # 35 days from May 4
        #     "xcv": datetime.date(2025, 7, 13),   # 35 days from June 8
        #     "cfh": datetime.date(2025, 8, 17),   # 35 days from July 13
        #     "q12": datetime.date(2025, 9, 21),   # 35 days from Aug 17
        #     "yuk": datetime.date(2025, 10, 26),  # 35 days from Sept 21
        #     "pol": datetime.date(2025, 11, 30),  # 35 days from Oct 26
        #     "ffg": datetime.date(2026, 1, 4),    # 35 days from Nov 30
        #     "uuu": datetime.date(2026, 2, 8),    # 35 days from Jan 4
        #     "ugf": datetime.date(2026, 3, 15),   # 35 days from Feb 8
        #     "qưe": datetime.date(2026, 4, 19)    # 35 days from Mar 15
        # }
        #banmoi
        license_keys = {
            "hsr": datetime.date(2025, 11, 30),   # 30 days from Oct 23, 2025
            "qqq": datetime.date(2025, 11, 30),   # 30 days from Oct 28, 2025
            "ưgj": datetime.date(2025, 10, 30),   # 30 days from Sep 21, 2025
            "h54": datetime.date(2025, 12, 15),   # 30 days from Oct 26, 2025
            "oip": datetime.date(2025, 12, 30),   # 30 days from Nov 30, 2025
            "4th": datetime.date(2026, 2, 3),     # 30 days from Jan 4, 2026
            "vbn": datetime.date(2026, 3, 10),    # 30 days from Feb 8, 2026
            "xzx": datetime.date(2026, 4, 14),    # 30 days from Mar 15, 2026
            "ert": datetime.date(2026, 5, 19),    # 30 days from Apr 19, 2026
            "q23": datetime.date(2026, 6, 23),    # 30 days from May 24, 2026
            "poi": datetime.date(2026, 7, 28)     # 30 days from June 28, 2026
        }
        #Cam2
        # license_keys = {
        #     "123": datetime.date(2025, 5, 4),
        #     "hsr": datetime.date(2025, 6, 8),    # 35 days from May 4
        #     "hsư": datetime.date(2025, 7, 13),   # 35 days from June 8
        #     "hqư": datetime.date(2025, 8, 17),   # 35 days from July 13
        #     "hpư": datetime.date(2025, 9, 21),   # 35 days from Aug 17
        #     "hkư": datetime.date(2025, 10, 26),  # 35 days from Sept 21
        #     "hns": datetime.date(2025, 11, 30),  # 35 days from Oct 26
        #     "hqs": datetime.date(2026, 1, 4),    # 35 days from Nov 30
        #     "r8y": datetime.date(2026, 2, 8),    # 35 days from Jan 4
        #     "rhj": datetime.date(2026, 3, 15),   # 35 days from Feb 8
        #     "asq": datetime.date(2026, 4, 19)    # 35 days from Mar 15
        # }
        #Cam1
        # license_keys = {
        #     "sdf": datetime.date(2025, 5, 4),
        #     "sss": datetime.date(2025, 6, 8),    # 35 days from May 4
        #     "xxs": datetime.date(2025, 7, 13),   # 35 days from June 8
        #     "gue": datetime.date(2025, 8, 17),   # 35 days from July 13
        #     "uyt": datetime.date(2025, 9, 21),   # 35 days from Aug 17
        #     "yhn": datetime.date(2025, 10, 26),  # 35 days from Sept 21
        #     "ert": datetime.date(2025, 11, 30),  # 35 days from Oct 26
        #     "rưr": datetime.date(2026, 1, 4),    # 35 days from Nov 30
        #     "asf": datetime.date(2026, 2, 8),    # 35 days from Jan 4
        #     "ccd": datetime.date(2026, 3, 15),   # 35 days from Feb 8
        #     "ikl": datetime.date(2026, 4, 19)    # 35 days from Mar 15
        # }
        
        # NMY
        # license_keys = {
        #     "bnm": datetime.date(2025, 5, 10),
        #     "bvc": datetime.date(2025, 6, 6),   # 35 days from May 2
        #     "bgd": datetime.date(2025, 7, 11),  # 35 days from June 6 
        #     "bhj": datetime.date(2025, 8, 15),  # 35 days from July 11
        #     "bdr": datetime.date(2025, 9, 19),  # 35 days from Aug 15
        #     "bkl": datetime.date(2025, 10, 24), # 35 days from Sept 19
        #     "bth": datetime.date(2025, 11, 28), # 35 days from Oct 24
        #     "bqq": datetime.date(2026, 1, 2),   # 35 days from Nov 28
        #     "byy": datetime.date(2026, 2, 6),   # 35 days from Jan 2
        #     "buu": datetime.date(2026, 3, 13),  # 35 days from Feb 6
        #     "bss": datetime.date(2026, 4, 17)   # 35 days from Mar 13
        # }
        #Goc
        # license_keys = {
        #     "yyy": datetime.date(2025, 5, 10),
        #     "yuj": datetime.date(2025, 6, 6),   # 35 days from May 2
        #     "yhf": datetime.date(2025, 7, 11),  # 35 days from June 6 
        #     "yui": datetime.date(2025, 8, 15),  # 35 days from July 11
        #     "yee": datetime.date(2025, 9, 19),  # 35 days from Aug 15
        #     "sss": datetime.date(2025, 10, 24), # 35 days from Sept 19
        #     "ngh": datetime.date(2025, 11, 28), # 35 days from Oct 24
        #     "csd": datetime.date(2026, 1, 2),   # 35 days from Nov 28
        #     "iop": datetime.date(2026, 2, 6),   # 35 days from Jan 2
        #     "fsa": datetime.date(2026, 3, 13),  # 35 days from Feb 6
        #     "avb": datetime.date(2026, 4, 17)   # 35 days from Mar 13
        # }

        # Validate license key
        if key not in license_keys:
            print("Key không hợp lệ")
            logging.error("Key không hợp lệ")

            exit()
            
        # Check if license is expired
        expiration_date = license_keys[key]
        if today.date() > expiration_date:
            print("Key đã hết hạn") 
            logging.error("Key đã hết hạn")

            exit()
            
    except requests.RequestException as e:
        print(f"Lỗi kết nối internet: {e}")
        logging.error(f"Lỗi kết nối internet: {e}")
        exit()
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        logging.error(f"Lỗi không xác định: {e}")
        exit()
image_path = os.path.join('image')
def closeGame(udid,package):
    command = f"{adb} -s {udid} shell am force-stop {package}"
    os.system(command)
    print(f"{udid} đang đóng {package}")
    logging.info(f"{udid} đang đóng {package}")


def moGame(udid,package):
    command = f"{adb} -s {udid} shell am start -n {package}"
    os.system(command)
    print(f"{udid} đang mở {package}")
    logging.info(f"{udid} đang mở {package}")


def quetChuVie(img):
    #lay ra text trong anh
    text = pytesseract.image_to_string(img, lang="vie")
    return text

def clearData(img):
    command=f"{adb} -s {udid} shell am start -n {package}"


def restartLD():
    a=[]
    while True:
        command=f"{ld} quitall"
        subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)
        for i in range(u):
            command=f"{ld} launch --index {(i+1)}"
            subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)
            time.sleep(1)
        time.sleep(50)
        for i in range(10):
            a=get_connected_devices()
            if(len(a)==u):
                
                return a
def quetChuEn(img):
    #lay ra text trong anh
    
# Resize, grayscale, Otsu's threshold
    img = imutils.resize(img, width=500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Perform text extraction
    data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
    return data

def swipe(udid,x1,y1,x2,y2,time=1000):
    command = f"{adb} -s {udid} shell input swipe {x1} {y1} {x2} {y2} {time}"
    os.system(command)

def keycode(udid, code):
    command = f"{adb} -s {udid} shell input keyevent {code}"
    os.system(command)

def click(udid,x,y,Tag="None"):
    print(f"{udid} vua click vao {Tag}")
    logging.info(f"{udid} vua click vao {Tag}")

    command = f"{adb} -s {udid} shell input tap {x} {y}"
    os.system(command)
    time.sleep(random.randint(1,2))

def doubleclick(udid,x,y,Tag="None"):
    print(f"{udid} vua click vao {Tag}")
    logging.info(f"{udid} vua click vao {Tag}")

    command = f"{adb} -s {udid} shell input tap {x} {y} && {adb} -s {udid} shell input tap {x} {y}"
    os.system(command)
    time.sleep(1)
def delete(udid):
    for i in range(3):
        command = f"adb -s {udid} shell input keyevent KEYCODE_DEL"
        os.system(command)
def clickhold(udid,x,y,delay=200):
    command = f"{adb} -s {udid} shell input swipe {x} {y} {x} {y} {delay}"
    os.system(command)

def sendtext(udid, g):
    command = f"{adb} -s {udid} shell input text \'{g}\'"
    os.system(command)
    
def find(udid, img='', threshold=0.95):
    img=f"image\\{img}"
    img2 =    screen_capture(udid)
    img =  cv2.imread(img)
    result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    needle_w = img.shape[1]
    needle_h = img.shape[0]
    locations = list(zip(*loc[::-1]))
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)
    rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
    points=[]
    if len(rectangles):
        # marker_color = (255, 0, 255)
        # marker_type = cv2.MARKER_CROSS
        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append((center_x, center_y))
            # cv2.drawMarker(img2, (center_x, center_y), 
            #                     color=marker_color, markerType=marker_type, 
            #                     markerSize=40, thickness=2)
    else:
        return 0
    # cv2.imshow('Matches', img2)  
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    return points



def find2(img2, img1,udid=False,a=0,b=0,threshold=0.95):
    img1=f"image\\{img1}"
    img=cv2.imread(img1)
    result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    needle_w = img.shape[1]
    needle_h = img.shape[0]
    locations = list(zip(*loc[::-1]))
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)
    rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
    points=[]
    if len(rectangles):
        # marker_color = (255, 0, 255)
        # marker_type = cv2.MARKER_CROSS
        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append((center_x, center_y))
            # cv2.drawMarker(img2, (center_x, center_y), 
            #                     color=marker_color, markerType=marker_type, 
            #                     markerSize=40, thickness=2)
    else:
        return 0
    # cv2.imshow('Matches', img2)  
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    if(udid!=False):
        print(f'phat hien anh {img1}')
        logging.info(f'phat hien anh {img1}')

        click(udid, points[0][0]+a,points[0][1]+b )
        return points
    
    return points


def find3(img2, img,udid=False,a=0,b=0,threshold=0.95):
    
    result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    needle_w = img.shape[1]
    needle_h = img.shape[0]
    locations = list(zip(*loc[::-1]))
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)
    rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
    points=[]
    if len(rectangles):
        # marker_color = (255, 0, 255)
        # marker_type = cv2.MARKER_CROSS
        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append((center_x, center_y))
            # cv2.drawMarker(img2, (center_x, center_y), 
            #                     color=marker_color, markerType=marker_type, 
            #                     markerSize=40, thickness=2)
    else:
        return 0
  
    
    return points


def check_color2(image, x, y, color, threshold):
    # Lấy giá trị màu của điểm ảnh (x, y)
    b, g, r = image[y, x]
    # Tạo khoảng ngưỡng cho màu cần tìm
    lower_color = np.array(color) - threshold
    upper_color = np.array(color) + threshold
    # Kiểm tra xem giá trị màu có nằm trong khoảng ngưỡng hay không
    if lower_color[0] <= b <= upper_color[0] and lower_color[1] <= g <= upper_color[1] and lower_color[2] <= r <= upper_color[2]:
        print("Màu được tìm thấy!")
        logging.info("Màu được tìm thấy!")
        return 1
    else:
        print("Màu không được tìm thấy.")
        logging.info("Màu không được tìm thấy.")
        return 0

# def checkcolor(image,color,threshold):
#     hsvimg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     lb=np.array([94,80,2])
#     ub=np.array([126,255,255])
#     mask = cv2.inRange(hsvimg, lb, ub)   
#     if 255 in mask:
#         print("Blue color present")

def screen_capture(udid):
    pipe = subprocess.Popen(f"{adb} -s {udid} shell screencap -p",
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE, shell=True)
    image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    # cv2.imwrite("test.png",image)
    return image

# def screen_capture(udid):
#     try:
#         result = subprocess.check_output(['adb', '-s',f'{udid}', 'exec-out', 'screencap'])
#     except:
#         return None

#     # wigth, heightを取得。
#     wigth = int.from_bytes(result[0:4], 'little')
#     height = int.from_bytes(result[4:8], 'little')
#     _ = int.from_bytes(result[8:12], 'little')

#     # ここのCopyは必須。そうでないと、編集が出来ない
#     tmp = np.frombuffer(result[12:], np.uint8, -1, 0).copy() 

#     # 配列の形状変換。
#     # 1つの要素がRGBAである、height * widthの行列を作る。
#     img = np.reshape(tmp, (height, wigth, 4))    

#     # 要素入れ替え。
#     # RawDataはRGB、OpenCVはBGRなので、0番目の要素と、2番目の要素を入れ替える必要がある。
#     b = img[:, :, 0].copy()               # ここのコピーも必須
#     img[:, :, 0] = img[:, :, 2]
#     img[:, :, 2] = b

#     # alpha値を削除。alpha値が必要な場合は、下記行は消しても良いかも？
#     img2 = np.delete(img, 3, 2)
#     # 
#     # cv2.imshow("Screenshot", img2)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()
#     gray_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#     rotated_image = cv2.rotate(gray_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#     # cv2.imwrite("test.png",rotated_image)
    


#     return  rotated_image

# def screen_capture(udid: str):
#     try:
#         # Lấy dữ liệu màn hình từ thiết bị Android
#         result = subprocess.check_output(['adb', '-s', udid, 'exec-out', 'screencap'])
#     except subprocess.CalledProcessError:
#         print("❌ Lỗi khi chạy lệnh adb.")
#         return None

#     if len(result) < 12:
#         print("❌ Dữ liệu ảnh trả về không hợp lệ.")
#         return None

#     # Đọc width, height từ 12 byte đầu
#     width = int.from_bytes(result[0:4], byteorder='little')
#     height = int.from_bytes(result[4:8], byteorder='little')
#     _format = int.from_bytes(result[8:12], byteorder='little')  # thường là 1 (RGBA_8888)

#     # Dữ liệu ảnh RGBA bắt đầu từ byte 12
#     raw_img = np.frombuffer(result[12:], dtype=np.uint8).copy()

#     # Chuyển thành ma trận ảnh với 4 kênh (RGBA)
#     try:
#         img = raw_img.reshape((height, width, 4))
#     except ValueError:
#         print("❌ Không reshape được ảnh. Có thể thiết bị không trả đúng dữ liệu.")
#         return None

#     # Đổi từ RGBA → BGR (bỏ kênh alpha)
#     img_bgr = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

#     return img_bgr

def findTrue(udid,img='',yclick=1,time_sleep=0,threshold=0.95):
    while True:
        try:
            anh=find(udid,img,threshold=threshold)
            if(anh!=0):    
                print(f"Phat hien anh {img}")
                logging.info(f"Phat hien anh {img}")

                if(yclick==1):
                    time.sleep(time_sleep)
                    click(udid,anh[0][0],anh[0][1])
                return 1
            else:
                logging.info(f"khong phat hien anh {img}")
                print(f"khong phat hien anh {img}")
        except Exception as e:
            print(f"khong phat hien anh {img}")
            logging.error(f"khong phat hien anh {img}")
            print("Đã xảy ra lỗi: ",e)
            return 0

def findFalse(udid,n=2,img="",yclick=0):
    print(f"{udid} dang tim {img}") 
    logging.info(f"{udid} dang tim {img}")

    for i in range(n):
        try:
            anh=find(udid,img)
            if(anh==0):
                return 0
        except Exception as e:
            print(f"khong phat hien anh {img}",e)
            logging.error(f"khong phat hien anh {img}")

    return 1



def findFor(udid,n=2,img="",yclick=1,time_sleep=0,threshold=0.9):   
    
    print(f"{udid} dang tim {img}") 
    logging.info(f"{udid} dang tim {img}")

    for i in range(n):
        try:
            anh=find(udid,img,threshold)
            if(anh!=0):
                logging.info(f"Phat hien anh {img}")
                print(f"Phat hien anh {img}")
                if(yclick==1):
                    time.sleep(time_sleep)
                    click(udid,anh[0][0],anh[0][1])
                    print(anh[0][0],anh[0][1])
                    logging.info(f"Click vao {img}")

                return anh
        except Exception as e:
            logging.error(f"khong phat hien anh {img}")
            print(f"khong phat hien anh {img}",e)
    return 0

    

            
def get_connected_devices():
    """Lấy danh sách các thiết bị ADB đã kết nối sử dụng os.popen thay vì subprocess.run
    
    Returns:
        list: Danh sách ID thiết bị
    """
    devices = []
    try:
        # Sử dụng os.popen để thực thi lệnh adb
        stream = os.popen(f"{adb} devices")
        output = stream.read().strip().split('\n')
        
        # Phân tích ID thiết bị từ đầu ra
        for line in output[1:]:  # Bỏ qua dòng đầu tiên (tiêu đề)
            if line.strip():  # Bỏ qua các dòng trống
                device = line.split('\t')[0]
                devices.append(device)
                
        return devices
    except Exception as e:
        print(f"Lỗi khi lấy danh sách thiết bị: {e}")
        logging.error(f"Lỗi khi lấy danh sách thiết bị: {e}")

        return []





def changeDPI():
    devices = get_connected_devices()
    for i in range(len(devices)):                                     
        command = f"{adb} -s {devices[i]} shell wm density 160"
        os.system(command)
        command = f"{adb} -s {devices[i]} shell wm size 960x540"
        os.system(command)

def reDPI():
    devices = get_connected_devices()
    for i in range(len(devices)):                                     
        # Get current density
        command = f"{adb} -s {devices[i]} shell wm density"
        density = os.popen(command).read().strip().split(" ")[2]
        
        # Set density back
        command = f"{adb} -s {devices[i]} shell wm density {density}"
        os.system(command)
        
        # Get current size
        command = f"{adb} -s {devices[i]} shell wm size"
        wmsize = os.popen(command).read().strip().split(" ")[2]
        
        # Set size back
        command = f"{adb} -s {devices[i]} shell wm size {wmsize}"
        os.system(command)

def sendtextbr(udid, g):
    command = f"{adb} -s {udid} shell am broadcast -a ADB_INPUT_TEXT --es msg \'{g}\'"
    os.system(command)

def setadbkb(udid):
    command = f"{adb} -s {udid} shell ime enable com.android.adbkeyboard/.AdbIME"
    os.system(command)
    command = f"{adb} -s {udid} shell ime set com.android.adbkeyboard/.AdbIME"
    os.system(command)

def killadb():
    command = f"{adb} kill-server"
    os.system(command)

def startadb():
    command = f"{adb} start-server"
    os.system(command)
# check_machine_id(blocked_id="BFEBFBFF000406F1")
setting=open('setting.txt').readlines()
adb=setting[1].strip()
key=setting[2].strip()
th=float(setting[3].strip())
auth(key)

