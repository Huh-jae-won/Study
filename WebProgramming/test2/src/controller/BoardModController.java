package controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import dao.BoardDAO;
import model.BoardDTO;

@WebServlet("/board/mod")
public class BoardModController extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String title = request.getParameter("title");
		String writer = request.getParameter("writer");
		String content = request.getParameter("content");
		String seq = request.getParameter("seq");
		System.out.println("seq:"+seq);
		System.out.println("tit:"+title);
		System.out.println("wri:"+writer);
		System.out.println("con:"+content);
		BoardDAO bDAO = new BoardDAO();
		BoardDTO bDTO = new BoardDTO();
		bDTO.setTitle(title);
		bDTO.setWriter(writer);
		bDTO.setContent(content);
		bDTO.setSeq(Integer.parseInt(seq));
		
		int ret = bDAO.modifyBoard(bDTO);
		RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/common/commonMsg.jsp");
		
		if(ret != 1) {
			// 에러인경우
			request.setAttribute("msg","글 작성 실패" );
		}else {
			request.setAttribute("msg","글 수정성공" );
		}
		request.setAttribute("url","/main" );
		rd.forward(request, response);
		
	}

}
