import pandas as pd

# dic 데이터로 DataFrame 객체 생성 -------------------------------------
tbl=pd.DataFrame(  {  "weight": [ 80.0, 70.4, 65.5, 45.9, 51.2 ],
                      "height": [ 170,  180,  155,  143,  154  ],
                      "type":   [ "f", "n", "n", "t", "t"]} )


# 인덱스 이름 변경 ----------------------------------------------------
print('tbl.index =>', tbl.index)                # 기본 index 출력
#tbl.index=['p1', 'p2','p3', 'p4', 'p5']         # index 변경
tbl.rename( index={ 0:'p1', 1:'p2', 2:'p3', 3:'p3', 4:'p4', 5:'p5'} , inplace=True)
print(tbl["weight"])
print(tbl[ ["weight", "height"]])

# 컬럼 이름 변경 ----------------------------------------------------
#tbl.columns=['몸무게','키','타입']
tbl.rename( columns={ 'weight':'몸무게', 'height':'키', 'type':'타입'} , inplace=True)
print('tbl.columns =>', tbl.columns)     
print(tbl["몸무게"])
print(tbl[ ["몸무게", "키"]])

# 행 선택 ---------------------------------------------
print('tbl.iloc[0] => '  ,tbl.iloc[0])            # 정수 인덱스 지정
print('tbl.loc["p1"] => ',tbl.loc['p1'])          # 문자열 인덱스 명 지정

print('tbl.iloc[0:2] => ',tbl.iloc[0:2])          # 범위 끝 미포함
print('tbl.iloc[0:2] => ',tbl.loc['p1':'p3'])     # 범위 끝 포함

# 열 선택 ----------------------------------------------
print(" tbl['키'] => ", tbl['키'])
print(" tbl.몸무게 => ", tbl.몸무게)

