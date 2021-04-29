from bs4 import BeautifulSoup
import urllib.request as req


url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"

# 데이터를 가져옴 : 네이버 영화랭킹의 1,2위를 가져옴
res = req.urlopen(url)


# 데이터를 추출하기 위해 추출가능한 형태로 바꿔줌
soup = BeautifulSoup(res,'html.parser')

# 원하는 데이터
# old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# old_content > table > tbody > tr:nth-child(3) > td.title > div > a

movie1 = soup.select_one("#old_content > table > tbody > tr:nth-child(2) > td.title > div > a")
print(movie1.string)
print(movie1.attrs['title'])

# 여러개 추출하기

# tr로 바꿔줌
movies = soup.select("#old_content > table > tbody > tr > td.title > div > a")
print("movies : ",movies,len(movies))
cnt = 1
for m in movies:
    print("%2d위 : %s"%(cnt,m.string))
    if cnt>=10:
        break
    cnt+=1
    