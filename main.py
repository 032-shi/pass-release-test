# 日本語対応させる
import zipfile

def main():
  with zipfile.ZipFile("sampleFolder.zip","r") as zip_file:
    try:
      zip_file.extractall(path=".", pwd="3456".encode("u"))
      print("zipを解凍できました")
    except RuntimeError:
      print("zipを開けませんでした")