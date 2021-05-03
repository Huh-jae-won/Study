

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/result")
public class ResultServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// DB에서 정보 select
		String title = "멘토링 프로젝트";
		String content = "오후 8시 26분";
		
		request.setAttribute("title", title);
		request.setAttribute("content", content);
		
		// 클라이언트에 데이터 전송
		
		
		
		RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/result.jsp");	// 상대적 주소를 적어줌
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
