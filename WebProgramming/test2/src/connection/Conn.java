package connection;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Conn {
	public static void main(String[] args) {
		try {
			Conn.getCon();
			System.out.println("연결성공");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	
	// 연결용
	public static Connection getCon() throws Exception {
		final String DB_URL = "jdbc:mysql://localhost:4406/mento?serverTimezone=UTC";
		final String DB_ID = "root";
		final String DB_PASSWORD= "qorhvk0.3";
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection con = DriverManager.getConnection(DB_URL, DB_ID, DB_PASSWORD);
		return con;
	}
//	Connection객체 : DB 연결용
//	PreparedStatement : DB쿼리 진행용
//	ResultSet : 쿼리결과 있다면 반환하는 용(조회(select)에만 사용)
	// 자원 회수용
	public static void close(Connection con, PreparedStatement ps, ResultSet rs) {
		if (rs != null) {
			try {
				rs.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		if (ps != null) {
			try {
				ps.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		if (con != null) {
			try {
				con.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
	public static void close(Connection con, PreparedStatement ps) {
		close(con,ps,null);
	}
}
