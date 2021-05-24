<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

<style>
   .writerWrap{margin: 0 auto;}
   .tit{text-align: center;}
</style>

<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
   <h1 class="tit">게시물 수정</h1>
   <div class="col-md-12">
      <div class="col-md-8 writerWrap">
         <form action="/board/mod" method="post">
         	<input type="hidden" name="seq" value=${one.seq}>
            <div class="form-group">
               <label for="title">제목</label>
               <input type="text" name="title" class="form-control" id="title" value="${one.title}">
            </div>
               <div class="form-group">
            <label for="title">작성자</label>
               <input type="text" name="writer" class="form-control" id="writer" value="${one.writer}">
            </div>
            <div class="form-group">
               <label for="title">내용</label>
               <textarea name="content" class="form-control" id="content">${one.content}</textarea>
            </div>
            <button class="btn btn-success">수정</button>
         </form>   
      </div>
   </div>
</body>
</html>