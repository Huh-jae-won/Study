package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import connection.Conn;
import model.BoardDTO;

public class BoardDAO {	
	// 삭제
	public int deleteBoard(BoardDTO param) {
		Connection con = null;
		PreparedStatement ps = null;
		int ret = 0;
		String sql = "delete from board_tb where seq=?";
		try {
			con = Conn.getCon();
			ps = con.prepareStatement(sql);	// 쿼리진행
			ps.setInt(1, param.getSeq());
			ret = ps.executeUpdate();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			ret = -1;
		}
		finally {
			Conn.close(con, ps, null);
		}
		return ret;
	}
	
	
	// 수정
	public int modifyBoard(BoardDTO param) {
		Connection con = null;			// DB 연결용
		PreparedStatement ps = null;	// 쿼리 진행용
		int ret = 0;
		String sql = "update board_tb set title=?, writer=?, content=? where seq=?";
		try {
			con = Conn.getCon();
			ps = con.prepareStatement(sql);	// 쿼리 진행
			ps.setString(1,param.getTitle());
			ps.setString(2,param.getWriter());
			ps.setString(3,param.getContent());
			ps.setInt(4, param.getSeq());
			ret = ps.executeUpdate();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			ret = -1;
		}
		finally {
			Conn.close(con, ps, null);
		}
		return ret;
	}
	
//	게시물 하나 가져오기
	public BoardDTO selectBoardOne(BoardDTO param) {
		BoardDTO bDTO = new BoardDTO();
		
		Connection con = null;			// DB 연결용
		PreparedStatement ps = null;	// 쿼리 진행용
		ResultSet rs = null;			// 쿼리 결과 리턴
		
		String sql = "select * from board_tb where seq=?";
		
		try {
			con = Conn.getCon();
			ps = con.prepareStatement(sql);	// 쿼리 진행
			ps.setInt(1, param.getSeq());
			rs = ps.executeQuery();			// 쿼리 결과값 리턴
			if(rs.next()) {
				bDTO.setSeq(rs.getInt("seq"));
				bDTO.setTitle(rs.getString("title"));
				bDTO.setWriter(rs.getString("writer"));
				bDTO.setContent(rs.getString("content"));
				bDTO.setReg_dt(rs.getString("reg_dt"));
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		finally {
			Conn.close(con, ps, null);
		}
		
		bDTO.setSeq(param.getSeq());
		return bDTO;
	}
	
//	게시글 가져오기
	public List<BoardDTO> selectBoardList(){
		List<BoardDTO> list = new ArrayList<>();
		
		// DB에서 가져와서
		Connection con = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		String sql = "select * from board_tb order by seq desc";
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
		finally {
			Conn.close(con, ps, rs);
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
