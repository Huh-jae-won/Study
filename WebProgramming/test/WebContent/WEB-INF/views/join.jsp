<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JOIN</title>
</head>
<body>
	<h2>회원가입 페이지</h2>
	<form action="/join" method="post">	<!-- post메소드로 /join이라는 도메인 주소로 요청함 -->
	<!-- GET : 안전x, POST : 안전 -->
		<div>id : <input type="text" name="id"></div>	<!-- 변수명 : id -->
		<div>pw : <input type="text" name="pw"></div>	<!-- 변수명 : pw -->
		<input type="submit" value="가입">
	</form>
</body>
</html>