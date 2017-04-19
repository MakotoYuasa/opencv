# opencv

_環境_  
OSX 10.12.4 Sierra  
Python 2.7.10  
Homebrew 1.1.12  

_準備_  
$ brew install numpy  

pipも必要  
$ easy_install pip  

音を出すのに必要  
$ brew install portaudio  
$ sudo env LDFLAGS="-L/usr/local/lib" CFFLAGS="-I/usr/local/include" pip install pyaudio  

Homebrewのアップデート  
$ brew update  
$ brew install -v cmake  
$ brew tap homebrew/science  

opencvのインストール, パスを通す  
$ brew install opencv  
$ export PYTHONPATH="/usr/local/lib/python2.7/site-packages/:$PYTHONPATH"  
(.bash_profileに書いておく方が良い,  
その場合は編集後に $ source .bash_profile  
を忘れない)  


_使い方, 説明_  
・capture.py
$ python capture.py  
webカメラを起動し, Sキーでpicture.pngとして画像を保存する.ESC, Qキーで終了させる.

・capture_gray.py  
$ python capture_gray.py  

・binarization.py  
$ python binarization.py  
2値化するプログラム.キー入力で2値化した画像の表示を終了する.  


_大変だったこと_  
pyaudioをimportできるようにしたら,  
ImportError: No module named cv2  
で結局, .bash_profileにパスを書くようにしたこと  

