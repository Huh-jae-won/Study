package model;

public class BoardDTO {
	private int seq;
	private String title;
	private String writer;
	private String content;
	private String reg_dt;
	
	public int getSeq() {
		return seq;
	}
	public void setSeq(int seq) {
		this.seq = seq;
	}
	public String getReg_dt() {
		return reg_dt;
	}
	public void setReg_dt(String regDT) {
		this.reg_dt = regDT;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getWriter() {
		return writer;
	}
	public void setWriter(String writer) {
		this.writer = writer;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	@Override
	public String toString() {
		return "BoardDTO [seq=" + seq + ", title=" + title + ", writer=" + writer + ", content=" + content + ", reg_dt="
				+ reg_dt + "]";
	}
	
	
}
