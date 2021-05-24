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

@WebServlet("/board/detail")
public class BoardDetailController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		try {
			String seq = request.getParameter("seq");
			BoardDTO param = new BoardDTO();
			param.setSeq(Integer.parseInt(seq));
			
			BoardDAO bDAO = new BoardDAO();
			BoardDTO retDTO = bDAO.selectBoardOne(param);
			request.setAttribute("one", retDTO);
			
			RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/boardDetail.jsp");
			rd.forward(request, response);
		}catch(Exception e) {
			e.printStackTrace();
		}
		
	}
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
