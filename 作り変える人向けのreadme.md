# はじめに
特にいうことはない。

# 設計思想
GPT.py で記述した OpenAI API へのアクセスやログ管理ルールを、各種実行ファイルで記述した UI によって利用する構造をとっている。

# GPT.py について
GPT には、

- システムプロンプト
- ユーザ入力
- アシスタント出力

の三つの概念が存在する。ChatGPT ではこのうちユーザ入力のみ操作できるようになっている。  
GPT はシステムプロンプトの入力により強く従うため、積極的に使うことをお勧めする。  

# GUI-Server.exe および chrome-GUI-EXE.bat について
exeファイルは python のモジュールの一つである  
__pyinstaller__  
というものを使っている。中身は pyファイル版 と同じだが、変更が連動するわけではない。  
GUI-Server.py に加えた変更を適用する際は、再度 pyinstaller で exeファイルを作り直す必要がある。