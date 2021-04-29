import codecs

filename = "../data/list-euckr.csv"
csv = codecs.open(filename, "r", "utf-8").read()
# csv파일을 파이썬 리스트로 변환
data = []
rows = csv.split("\r\n")
print(rows)
for i in rows:
    if i == "":
        continue
    value = i.split(",")
    print(value)
    data.append(value)
print(data)