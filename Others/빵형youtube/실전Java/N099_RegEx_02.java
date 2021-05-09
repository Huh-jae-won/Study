package 실전Java;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class N099_RegEx_02 {
	public static void main(String[] args) {
		String num = "주민등록번호 : 010101-2345678 주민등록번호 : 020202-4567890";
		String regex = "[0-9]{6}-[0-9]{7}";
		
		Pattern p = Pattern.compile(regex);
		Matcher m = p.matcher(num);
		
		while(m.find()) {
			System.out.printf(m.group() + " -> ");
			String newNum = m.group().substring(0,7) + "****" + m.group().substring(11);
			System.out.println(newNum);
		}
	}

}
