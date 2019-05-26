from flask import *
import subprocess
from string import ascii_lowercase,ascii_uppercase

listallow=list(ascii_lowercase)
listallow+=list(ascii_uppercase)
listallow+=['_','-']
listallow+=['1','2','3','4','5','6','7','8','9','0']

make_key=input("api 통신에 사용할 비밀 KEY를 입력해주세요(디스코드 키 아님): \n")


app=Flask(__name__)

@app.route("/")
def index():
    return "home"


@app.route("/api", methods=['GET'])
def api():
    action=request.args.get('action')
    key=request.args.get('key')

    if key==make_key:
        if action=='update':
            out=subprocess.check_output(['apt-get update'], shell=True)
            return out

        elif action=='install':
            install=request.args.get('install')
            if install=="" or install==" ":
                return "Error: NO install param"
            else:
                for i in range(len(install)):
                    if list(install)[i] not in listallow:
                        return "NO Hack~~!, IP has been collected"
                out = subprocess.check_output(['apt-get -y install '+install], shell=True)
                return out

        elif action=='check':
            check = request.args.get('check')
            if check == "" or check == " ":
                return "Error: NO install param"
            else:
                for i in range(len(check)):
                    if list(check)[i] not in listallow:
                        return "NO HACK~~!, IP has been collected"
                try:
                    out = subprocess.check_output(['dpkg -l | grep '+check], shell=True)
                    return out
                except:
                    return "해당 패키지가 존재하지 않습니다."

        elif action=='adduser':
            adduser = request.args.get('adduser')
            passwd="teamkornewbie"
            if adduser == "" or adduser == " ":
                return "Error: NO install param"
            else:
                for i in range(len(adduser)):
                    if list(adduser)[i] not in listallow:
                        return "NO Hack~~!, IP has been collected"
                exec = subprocess.check_output(['useradd '+adduser+' -m -s /bin/bash'], shell=True)
                chpass=subprocess.check_output(['echo "'+adduser+':'+passwd+'" | chpasswd'], shell=True)
                out="유저명 "+adduser+"을 패스워드 teamkornewbie로 생성완료"
                return out
        else:
            "ERROR: Exception ERROR"

    else:
        return "403 Permission Error"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7864)