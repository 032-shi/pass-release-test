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

  for a in numbers:
    print(a)

if __name__ == "__main__":
  main()