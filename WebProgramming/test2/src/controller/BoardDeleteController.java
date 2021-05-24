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

@WebServlet("/board/del")
public class BoardDeleteController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String seq = request.getParameter("seq");
		BoardDAO bDAO = new BoardDAO();
		BoardDTO bDTO = new BoardDTO();
		bDTO.setSeq(Integer.parseInt(seq));
		
		int ret = bDAO.deleteBoard(bDTO);
		
		RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/common/commonMsg.jsp");
		String msg = "삭제에 성공했습니다.";
		String url = "/main";
		if(ret!=1) {
			msg = "삭제에 실패했습니다.";
			// 실패
		}
		request.setAttribute("url", url);
		request.setAttribute("msg", msg);
		
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	}

}
