import struct

def to_csv(name, maxdata):
    # (1)  csv 저장할 데이터 준비
    # 레이블 파일과 이미지 파일 열기
    lbl_f = open("../data/MNIST/"+name+"-labels-idx1-ubyte","rb")
    img_f = open("../data/MNIST/"+name+"-images-idx3-ubyte","rb")
    csv_f = open("../data/MNIST/"+name+".csv","w",encoding='utf-8')

    # 헤더 정보읽기
    mag, lbl_count = struct.unpack(">II", lbl_f.read(8)) # 최상위비트부터 unsigned Int형으로
    mag, img_count = struct.unpack(">II", img_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixels = rows*cols

    # 이미지 데이터를 읽고 csv로 저장하기
    res = []
    for idx in range(lbl_count):
        if idx > maxdata : break

        # 숫자이미지 데이터가 의미하는 숫자값 읽기
        label = struct.unpack("B",lbl_f.read(1))[0] # 리턴타입(튜플)
        # 이미지 데이터 읽기
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n:str(n), bdata))
        csv_f.write(str(label)+",")
        csv_f.write(",".join(sdata)+"\r\n")

        # 잘 저장됐는지 이미지 파일로 저장해서 테스트하기
        if idx<10:
            s = "P2 28 28 255\n"
            s += " ".join(sdata)
            iname = "../data/MNIST/{}-{}-{}.pgm".format(name,idx,label)
            with open(iname,"w",encoding='utf-8') as fp:
                fp.write(s)
    csv_f.close()
    lbl_f.close()
    img_f.close()

# 결과를 파일로 출력
to_csv("train",1000)
to_csv("t10k",500)