import bz2,os,sys

file_in=input("Enter the path of the file to be compressed:")
file_out=input("Enter the name of the compressed file:")

with open(file_in,mode="rb") as fin:
  fout=bz2.open(file_out,mode="wb")
  fout.write(fin.read())

print(f"Uncompressed size: {os.stat(file_in).st_size}")

print(f"Compressed size: {os.stat(file_out).st_size}")

with bz2.open(file_out, "rb") as fin:
    data = fin.read()
    print(f"Decompressed size: {sys.getsizeof(data)}")
