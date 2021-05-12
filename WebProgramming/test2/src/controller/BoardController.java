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

@WebServlet("/board")
public class BoardController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public BoardController() {
        super();
        // TODO Auto-generated constructor stub
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/board.jsp");
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String title = request.getParameter("title");
		String writer = request.getParameter("writer");
		String content = request.getParameter("content");
		System.out.println("title : "+title);
		System.out.println("writer : "+writer);
		System.out.println("content : "+content);
		
		BoardDTO boardDto = new BoardDTO();
		boardDto.setTitle(title);
		boardDto.setWriter(writer);
		boardDto.setContent(content);
		
		BoardDAO dao = new BoardDAO();
		int result = dao.insertBoard(boardDto);
		
		RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/common/commonMsg.jsp");
		request.setAttribute("msg","글작성성공" );
		request.setAttribute("url","/main" );
		
		if(result != 1) {
			// 에러인경우
			request.setAttribute("msg","글 작성 실패" );
			request.setAttribute("url","/board" );
		}else {
			
		}
		rd.forward(request, response);
		
	}

}
