# opencv

_環境_  
OSX 10.12.4 Sierra  
Python 2.7.10  
Homebrew 1.1.12  

_準備_  
$ brew install numpy

Homebrewのアップデート  
$ brew update  
$ brew install -v cmake  
$ brew tap homebrew/science  

opencvのインストール, パスを通す  
$ brew install opencv  
$ export PYTHONPATH="/usr/local/lib/python2.7/site-packages/:$PYTHONPATH"  

_使い方, 説明_  
・capture.py
$ python capture.py  
webカメラを起動し, Sキーでpicture.pngとして画像を保存する.ESC, Qキーで終了させる.

・binarization.py  
$ python binarization.py  
2値化するプログラム.キー入力で2値化した画像の表示を終了する.  
