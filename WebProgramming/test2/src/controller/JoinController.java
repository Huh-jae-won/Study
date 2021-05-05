package controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import dao.UserDAO;
import model.UserDTO;

@WebServlet("/join")
public class JoinController extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		RequestDispatcher rd =  request.getRequestDispatcher("/WEB-INF/views/join.jsp");
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// 받아와서 콘솔찍기
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		System.out.printf("[POST] id: %s, pw: %s\n",id,pw);
		
		// DB에 넣는다
		UserDTO dto = new UserDTO();
		dto.setUserId(id);
		dto.setUserPw(pw);
		
		UserDAO ud = new UserDAO();
		ud.doJoin(dto);
		
	}

}
