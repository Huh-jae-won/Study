package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;

import connection.Conn;
import model.UserDTO;

public class UserDAO {
	// DAO : Data Access Object
	public static void main(String[] args) {

	}
	// 회원가입 메소드
	public void doJoin(UserDTO param) {
		Connection con = null;	// DB연결용
		PreparedStatement ps = null;	// DB쿼리용
		String sql = "INSERT INTO USER_TB(USER_ID, USER_PW) VALUES(?,PASSWORD(?))";
//		ResultSet rs = null;		// Select용
		
		try {
			con = Conn.getCon();	// DB연결성공
			ps = con.prepareStatement(sql);	// 쿼리매핑
			ps.setString(1, param.getUserId());	// 1: index
			ps.setString(2, param.getUserPw());
			ps.executeUpdate();	// 쿼리 실행
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		finally {
			Conn.close(con, ps, null);
		}
	}

}
