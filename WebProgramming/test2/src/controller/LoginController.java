package controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import dao.UserDAO;
import model.UserDTO;

@WebServlet("/login")
public class LoginController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession hs = request.getSession();
		String loginUser = (String)hs.getAttribute("loginUser");
		if(loginUser!=null) {	
			// 이미 로그인 -> 메인페이지로 이동하도록
			response.sendRedirect("/main");
			return;
		}
		RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/login.jsp");
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		
//		System.out.println(id+", "+pw);
		
		UserDTO uDTO = new UserDTO();
		UserDAO uDAO = new UserDAO();
		uDTO.setUserId(id);
		uDTO.setUserPw(pw);
		int ret = uDAO.doLogin(uDTO);
		String msg = "로그인에 성공했습니다.";
		String url = "/main";
		switch (ret) {
		case 1:		// 로그인 성공 -> 메인페이지로
			// 로그인 정보를 세션에 저장 : 모든 페이지에서 사용할수있도록
			HttpSession hs = request.getSession();
			hs.setAttribute("loginUser", id);
			break;
		case -1:	// 로그인 실패 -> 다시 로그인페이지로
			msg = "아이디 또는 패스워드가 일치하지 않습니다.";
			url = "/login";
			break;
		default:	// 알수없는에러(0), 에러(-2)
			msg = "DB 오류 발생!! 관리자에게 문의하세요.";
			url = "/login";
			break;
		}
		request.setAttribute("msg", msg);
		request.setAttribute("url", url);
		request.setAttribute("uDTO", uDTO);
		
		RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/common/commonMsg.jsp");
		rd.forward(request, response);
	}
}
