<%@ page language="java" contentType="text/html; charset=UTF-8"
   pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet"
   href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

<style>
	tr:hover{background-color: #ddd; cursor: pointer}
</style>
<meta charset="UTF-8">
<title>Main</title>
</head>
<body>
   <div style="text-align: center;">
      <h1>메인 페이지</h1>
      <c:if test="${loginUser != null }">
      	<h3>${loginUser} 님 환영합니다</h3>
      </c:if>
      <a href="/join">회원가입</a>		<!-- a태그를 이용하여 특정 주소로 이동 -->
      <a href="/board">게시물 작성</a>
      <a href="/login">로그인</a>
   </div>
   <div class="col-md-12">
      <div class="col-md-8" style="margin:0 auto;">
         <table class="table">
            <thead class="thead-dark">
               <tr>
                  <th scope="col">No.</th>
                  <th scope="col">제목</th>
                  <th scope="col">작성자</th>
                  <th scope="col">작성일자</th>
               </tr>
            </thead>
            <tbody>
            	<c:forEach items="${list }" var="dto"> <!-- list라는 놈을 변수명 dto 으로 사용 -->
            		<tr onclick="goBoardDetail(${dto.seq})" >
	                <th scope="row">${dto.seq }</th>
	                <td>${dto.title }</td>
	                <td>${dto.writer }</td>
	                <td>${dto.content }</td>
	               </tr>
	           	</c:forEach>
            </tbody>
         </table>
      </div>
   </div>
  <script>
  <!--자바 스크립트 문법-->
  	function goBoardDetail(seq){
  		location.href = "/board/detail?seq="+seq;
  	}
  </script>
</body>
</html>