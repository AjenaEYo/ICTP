# ICTP
윈도우창을 캡쳐해서 번역해준다.<br />
window capture->ocr->translation->text draw->view
![Screenshot](https://github.com/AjenaEYo/ICTP/blob/develop/example/ictp_first.gif)

해결해야할 과제
1. 0.1fps 성능문제 > ocr에서 많이 먹는데, 더 빠른거로 찾아볼까..
2. 번역 횟수 제한 > 카카오번역으로 임시로 변환, Translation 뉴럴네트워크를 박아야할까나..
3. 캡쳐 영역 > 완료

Python 3.7.9 64bit에서 작성(https://www.python.org/downloads/release/python-379/)
(https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe)

인스톨 버전으로 설치하면 pip같이 설치되지만 안되시는분은 아래 참고.<br />
pip install
``` bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

환경 변수에 python.exe pip.exe가 들어 있는 폴더가 설정되어 있어야 cmd에서 아래 명령 수행가능.<br />

``` bash
pip install easyocr
pip install pywin32
pip install pynput
pip install opencv-python
pip install kakaotrans
```
easyocr gpu에서 돌릴려면
``` bash
pip install torch==1.8.1+cu102 torchvision==0.9.1+cu102 torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
```
cuda 버전 맞춰서 설치. https://pytorch.org/ 가면 받을수 있다.



``` bash
python main.py
```

캡쳐할 윈도우 좌클릭.<br />
번역할 화면에서 T버튼 클릭(ICTP창에서 눌러야함).<br />
아무키 누르면 다시 캡쳐모드.<br />
종료는 캡쳐모드에서 q.<br />
