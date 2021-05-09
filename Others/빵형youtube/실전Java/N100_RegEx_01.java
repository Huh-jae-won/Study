package 실전Java;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class N100_RegEx_01 {
	public static void main(String[] args) {
		 String str = "닭아 닭아 우지마라 네가 울면 날이 새고 날이 새면 나 죽는다.";
		 String ret = "";
		 int startIdx = 0;
		 Pattern p = Pattern.compile("새");
		 Matcher m = p.matcher(str);
		 
		 // m.start() m.end() : regex와 매칭되는 문자열의 시작, 끝 indx 반환
		 
		 while(m.find()) {
			 ret += str.substring(startIdx,m.start())+"["+m.group()+"]";
			 startIdx = m.end();
		 }
		 if(startIdx<str.length())
			 ret += str.substring(startIdx);
		 System.out.println(str+" -> "+ret);
		 
	}
}
