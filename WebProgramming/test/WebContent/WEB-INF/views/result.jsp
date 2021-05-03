<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>전송결과</h1>
	<!-- 요즘방식 : el표현식 -->
	title : ${title} <br>
	content : ${content} <br>
	
	<hr>
	<!-- 옛날 스크립트 방식 -->
	<%
		String title = (String) request.getAttribute("title");
		String content = (String) request.getAttribute("content");	
	%>
	옛방식 <br>
	title : <%= title %>	<br>
	content : <%= content %>	<br>
	
</body>
</html>