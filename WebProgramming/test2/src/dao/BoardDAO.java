package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import connection.Conn;
import model.BoardDTO;

public class BoardDAO {
	
//	게시글 가져오기
	public List<BoardDTO> selectBoardList(){
		List<BoardDTO> list = new ArrayList<>();
		
		// DB에서 가져와서
		Connection con = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		String sql = "select * from board_tb";
		try {
			con = Conn.getCon();			// 쿼리 연결
			ps = con.prepareStatement(sql);	// 쿼리 진행
			rs = ps.executeQuery();			// 쿼리(select) 결과를 받음
			while(rs.next()) {
				BoardDTO bdto = new BoardDTO();
				bdto.setTitle(rs.getString("title"));	// DB의 column명으로
				bdto.setContent(rs.getString("content"));
				bdto.setWriter(rs.getString("writer"));
				bdto.setSeq(rs.getInt("seq"));
				bdto.setReg_dt(rs.getString("reg_dt"));
				// list에 담아서
				list.add(bdto);
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		// 리턴
		return list;
	}
	
	public int insertBoard(BoardDTO dto) {
		int result = 0;
		
		Connection con = null;			// db연결용
		PreparedStatement ps = null;	// 쿼리진행용
		ResultSet rs = null;			// 조회용(select)
		
		String sql = "INSERT INTO board_tb(title, content, writer, reg_DT)" + 
				"VALUES(?, ?, ?,now())";
		try {
			con = Conn.getCon();
			ps = con.prepareStatement(sql);
			ps.setString(1, dto.getTitle());	// 1번쨰 ?에 값 세팅
			ps.setString(2, dto.getContent());
			ps.setString(3, dto.getWriter());
			
			result = ps.executeUpdate();
		} catch (Exception e) {
			result = -1;
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		finally {
			Conn.close(con, ps, null);
		}
		return result;
	}
}