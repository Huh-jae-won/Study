

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/join")
public class JoinServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public JoinServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

//  get방식이면 doGet 실행
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/join.jsp");	// 상대적 주소를 적어줌
		rd.forward(request, response);
		// 데이터 받고
//		String id = request.getParameter("id");
//		String pw = request.getParameter("pw");
//		System.out.printf("[GET] id: %s, pw: %s\n",id,pw);
	}
	
//	post면 doPost 실행
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// 데이터 받고
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		System.out.printf("[POST] id: %s, pw: %s\n",id,pw);
		
		// DB로 데이터 저장
	}

}
