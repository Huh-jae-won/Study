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
		UserDTO uDTO = new UserDTO();
		uDTO.setUserId(id);
		uDTO.setUserPw(pw);
		
		UserDAO uDAO = new UserDAO();
		int ret = uDAO.doJoin(uDTO);
		
		String msg = "가입에 성공했습니다.";
		String url = "/login";
		if(ret!=1) {
			msg = "가입에 실패했습니다.";
			url = "/join";
		}
		RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/common/commonMsg.jsp");
		
		request.setAttribute("msg", msg);
		request.setAttribute("url", url);
		
		rd.forward(request, response);
	}

}
