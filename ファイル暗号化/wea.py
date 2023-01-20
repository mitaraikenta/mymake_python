from cryptography.fernet import Fernet

#キーを作成する
key = Fernet.generate_key()

#キーをローカルに保存する
with open(r"C:\Users\mitar\OneDrive\デスクトップ\mymake_python\ディレクトリ\test\.key","wb") as key_data:
    key_data.write(key)

#暗号化するファイルの取得
with open(r"C:\Users\mitar\OneDrive\デスクトップ\mymake_python\ディレクトリ\test\","r") as file:
    data = file.read()

print("暗号化する前: ",data)

#データをバイトに変換する
byte_data = data.encode()

#Fernetオブジェクトの初期化
f = Fernet(key)

#バイトデータを暗号化する
encrypt_data = f.encrypt(byte_data)

#暗号化した情報をファイルに書き込む
with open(r"C:\test\baka.txt","wb") as file:
    file.write(encrypt_data)

print("暗号化した後: ", encrypt_data)