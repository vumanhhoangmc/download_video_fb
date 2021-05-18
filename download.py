import os, sys
from time import sleep
try:
    import fbdown
except ImportError:
    os.system("pip3 install fb-down")
    import fbdown

class mau:
    hong = '\033[95m'
    tim = '\033[94m'
    xanh = '\033[32m'
    do = '\033[31m'
    vang = '\033[33m'
    trang = '\033[0m'
    trang_sang = '\033[1m'

logo = '''
    🦋    🦋  🦋    🦋   🦋   🦋    🦋 🦋  🦋 🦋  🦋  🦋 🦋 🦋  🦋 🦋 🦋 🦋  🦋\033[94m
       _____                      _                 _  __      ___     _            
      |  __ \                    | |               | | \ \    / (_)   | |           
      | |  | | _____      ___ __ | | ___   __ _  __| |  \ \  / / _  __| | ___  ___  
      | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |   \ \/ / | |/ _` |/ _ \/ _ \ 
      | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |    \  /  | | (_| |  __/ (_) |
      |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|     \/   |_|\__,_|\___|\___/      
                                                                                                                                                                                                                              
    🦋    🦋  🦋    🦋   🦋   🦋    🦋 🦋  🦋 🦋  🦋  🦋 🦋 🦋  🦋 🦋 🦋 🦋  🦋
    \033[1;97m╔═══════════════════════════════════════════════════════╗
    \033[1;97m║\033[1;93m* \033[1;97mDevlop By: \033[1;91m: \033[1;96mHOANGDZSVIP    \033[1;97m                         ║
    \033[1;97m║\033[1;93m* \033[1;97mYoutube \033[1;91m : \033[1;96mhoangdzsvip   \033[1;97m                            ║
    \033[1;97m║\033[1;93m* \033[1;97mFacebook \033[1;91m : \033[1;96mfb.com/manhhoang69   \033[1;97m                    ║
    \033[1;97m║\033[1;93m* \033[1;97mWebsite \033[1;91m:\033[1;96m hoangdzsvip.blogspot.com   \033[1;97m                ║
    \033[1;97m╚═══════════════════════════════════════════════════════╝'''

def facebook_download(): 
    os.system("clear")
    print(logo)
    print(mau.do+"         Download Video FaceBook")
    link = (input(mau.vang+"nhap link video: "))
    while not link:
        print(mau.do+"Bạn chưa nhập link.")
        link = (input(mau.vang+"nhap link video: "))
    file_name =  str(input(mau.vang+"Luu video voi ten: "))
    while not file_name:
        print(mau.do+"Bạn chưa nhập tên file")
        file_name =  str(input("Luu video voi ten: "))
    try:
        os.system("mkdir Video_FaceBook")
    except:
        pass    
    mau.xanh
    file_name_mp4 = file_name+".mp4"
    try:
        fbdown.main(link, path=file_name_mp4)
    except:
        print(mau.do+"Không Tìm Thấy Video.")
        sleep(4)
        main_tool()
    try:     
        os.system(f"mv {file_name_mp4} Video_FaceBook/")
    except:
        print(mau.do+"Lỗi.")
        sleep(4)
        main_tool()

def youtube_download():
    os.system("clear")
    print(logo)
    print(mau.do+"               Download Video YouTube")
    link = input("Nhap Link Video: ")
    url = pytube.YouTube(str(link))
    video = url.streams.first().download()

def main_tool():
    os.system("clear")
    print(logo)
    facebook_download()
if __name__ == "__main__":
    main_tool()