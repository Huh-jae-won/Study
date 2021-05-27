package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import connection.Conn;
import model.UserDTO;

public class UserDAO {
	// DAO : Data Access Object
	
	// 로그인 메소드
	public int doLogin(UserDTO param) {
		// ret : 성공(1), 실패(-1), 알수없는에러(-2), 쿼리문실패(0)
		int ret = 0;
		Connection con = null;			// DB연결용
		PreparedStatement ps = null;	// DB쿼리용
		ResultSet rs = null;			// select 반환용
		String sql = "SELECT * FROM user_tb WHERE user_id=? AND user_pw=PASSWORD(?)";

		try {
			con = Conn.getCon();
			ps = con.prepareStatement(sql);	// 쿼리진행
			ps.setString(1, param.getUserId());
			ps.setString(2, param.getUserPw());
			rs = ps.executeQuery();	// select 실행값 반환
			if(rs.next()) {
				ret = 1;	// 로그인 성공
				// 세션에 로그인 정보를 저장
			}else {
				ret = -1;	// 로그인 실패
			}
		} catch (Exception e) {
			ret = -2;
			e.printStackTrace();
		}			// DB연결
		finally {
			Conn.close(con, ps, rs);
		}
		return ret;
	}
	
	// 회원가입 메소드
	public int doJoin(UserDTO param) {
		int ret = 0;
		Connection con = null;	// DB연결용
		PreparedStatement ps = null;	// DB쿼리용
		String sql = "INSERT INTO USER_TB(USER_ID, USER_PW) VALUES(?,PASSWORD(?))";
//		ResultSet rs = null;		// Select용
		
		try {
			con = Conn.getCon();	// DB연결성공
			ps = con.prepareStatement(sql);	// 쿼리매핑
			ps.setString(1, param.getUserId());	// 1: index
			ps.setString(2, param.getUserPw());
			ret = ps.executeUpdate();	// 쿼리 실행
		} catch (Exception e) {
			ret = -2;
			e.printStackTrace();
		}
		finally {
			Conn.close(con, ps, null);
		}
		return ret;
	}

}
