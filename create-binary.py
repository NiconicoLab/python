#バイナリを作成プログラム

def createBin():
  with open("create-binary.bin", "wb") as fout:
    bin = bytearray([0x01, 0x02, 0x03])
    bin.append(4)
    bin.extend([5, 6])
    bin.append(7)
    bin.append(8)
    bin.extend([9, 0x0A])
    bin.extend([0x0B, 12])
    bin.append(0x0C)
    bin.append(0x0D)
    bin.append(0x0E)
    bin.append(0x0F)
    bin.append(0x10)
    fout.write(bin)

if __name__ == "__main__":
  createBin()

# 作成したbinaryの確認方法
# $ hexdump create-binary.bin
