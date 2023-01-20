from cryptography.fernet import Fernet

#キーの読み込み
with open(r"C:\test\baka.key","rb") as test_key:
    key = test_key.read()
#暗号化したファイルの読み込み
with open(r"C:\test\baka.txt","rb") as file:
    encryp_data = file.read()

print("暗号化された情報: ",encryp_data)

#キーを使ってFernetオブジェクトを初期化
f = Fernet(key)
#データの復号化
decrypt_data = f.decrypt(encryp_data)

print("復号化した情報: ",decrypt_data.decode('utf-8'))