package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import connection.Conn;
import model.BoardDTO;

public class BoardDAO {
	public void insertBoard(BoardDTO dto) {
		Connection con = null;			// db연결용
		PreparedStatement ps = null;	// 쿼리진행용
		ResultSet rs = null;			// 조회용(select)
		
		String sql = "INSERT INTO board_tb(title, content, writer)" + 
				"VALUES(?, ?, ?)";
		try {
			con = Conn.getCon();
			ps = con.prepareStatement(sql);
			ps.setString(1, dto.getTitle());
			ps.setString(2, dto.getContent());
			ps.setString(3, dto.getWriter());
			
			ps.executeUpdate();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}
