package controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import dao.BoardDAO;
import model.BoardDTO;

@WebServlet("/board/detail")
public class BoardDetailController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession hs = request.getSession();
		String id = (String) hs.getAttribute("loginUser");
		if(id==null) {
			// 로그인을 안했다면 게시물 수정도 불가
			response.sendRedirect("/login");	// rd.forward와의 차이점 : requset객체 못들고감, url자체가 바뀜
			return;
		}
		
		
		String seq = request.getParameter("seq");
		BoardDTO param = new BoardDTO();
		param.setSeq(Integer.parseInt(seq));
		
		BoardDAO bDAO = new BoardDAO();
		BoardDTO retDTO = bDAO.selectBoardOne(param);
		request.setAttribute("one", retDTO);
		
		RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/boardDetail.jsp");
		rd.forward(request, response);	// url은 안바뀜, request객체를 들고감
		
	}
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
