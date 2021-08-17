# coding: UTF-8
import zipfile

def open_zip(password):
  with zipfile.ZipFile("sampleFolder.zip","r") as zip_file:
    try: #まずは、tryの処理が行われる。
      zip_file.extractall(path="./unZipFolder", pwd=password.encode()) #path=に解凍後のファイルを保存するフォルダーを指定する
      print("zipを解凍できました")
      print("パスワード:{}".format(password))
      exit()
    except Exception as e: #例外発生時に行う処理
      pass #例外発生後に何も処理を行わない
      #print(e)
      #print("zipを開けませんでした")

def main():
  numbers = list(range(10))
  #print(numbers)
  my_passwords = []

  for a in numbers: #1桁目の数字の生成
    for b in numbers: #2桁目の数字の生成
      for c in numbers: #3桁目の数字の生成
        for d in numbers: #4桁目の数字の生成
          prediction_password = str(a) + str(b) + str(c) + str(d)
          print(prediction_password)
          open_zip(password=prediction_password)

if __name__ == "__main__":
  main()