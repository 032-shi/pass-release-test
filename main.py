import zipfile

def main():
  with zipfile.ZipFile("sampleFolder.zip","r") as zip_file: