# coding: UTF-8
import zipfile

def open_zip():
  with zipfile.ZipFile("sampleFolder.zip","r") as zip_file:
    try:
      password = "1234"
      zip_file.extractall(path=".unZipFolder", pwd=password.encode())
      print("zipを解凍できました")
    except Exception as e:
      print(e)
      print("zipを開けませんでした")

def main():
  numbers = list(range(10))
  print(numbers)
  my_passwords = []

  for a in numbers: #1桁目の数字の生成
    #print(a)
    for b in numbers: #2桁目の数字の生成
      answer = str(a) + str(b)
      print(answer)

if __name__ == "__main__":
  main()