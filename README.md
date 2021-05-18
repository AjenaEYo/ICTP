# ICTP
Translate the text of the image into a specific language
![Screenshot](https://github.com/AjenaEYo/ICTP/blob/develop/example/ictp_first.gif)

해결해야할 과제
1. 0.1fps 성능문제 > ocr에서 많이 먹는데, 더 빠른거로 찾아볼까..
2. 번역 횟수 제한 > 카카오번역으로 임시로 변환, Translation 뉴럴네트워크를 박아야할까나..
3. 캡쳐 영역 > 완료

``` bash
pip install easyocr
pip install pywin32
pip install opencv-python
```
easyocr gpu에서 돌릴려면
``` bash
pip install torch==1.8.1+cu102 torchvision==0.9.1+cu102 torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
```
cuda 버전 맞춰서 설치.

Python 3.7.9에서 작성

``` bash
python main.py
```

캡쳐할 윈도우 좌클릭.<br />
번역할 화면에서 T버튼 클릭(ICTP창에서 눌러야함).<br />
아무키 누르면 다시 캡쳐모드.<br />
종료는 캡쳐모드에서 q.<br />
