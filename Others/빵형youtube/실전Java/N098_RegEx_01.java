package 실전Java;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class N098_RegEx_01 {
	public static void main(String[] args) {
		String url = "https://docs.oracle.com/en/java.html/javase/16/docs/api/java.base/java/lang/String.html";
		String regex = "\\w+.html";	// 문자.html인 부분 
		String regex2 = "\\w+.html$";	// 문자.html인 부분 
		
		Pattern p = Pattern.compile(regex);
		Matcher m = p.matcher(url);
		
		while(m.find()) {
			System.out.println(m.group());
			// 파일명(String.html)을 찾고싶음 but 중간경로(java.html)도 출력됨
			// regex2로 하면 됨
		}
		System.out.println();
		
		// .com, .net으로 끝나는 이메일만 출력하기
		String email = 
				"smaple@naver.com,test@test.co.kr,"
				+ "knu@knu.ac.kr"
				+ "example@example.net,"
				+ "school@school.org,apple@apple.com";
		String regex3 = "\\w+@\\w+(.com|.net)";
		Pattern p2 = Pattern.compile(regex3);
		Matcher m2 = p2.matcher(email);
		while(m2.find()) {
			System.out.println(m2.group());
		}
	}
}
