package 실전Java;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class N097_RegEx_01 { 
/*
  	\\w : 영어, 숫자,  _ 포함 == [A-Za-z0-9_]
  	()  : 식을 하나로 묶음		ex) abc|abd == a(b|d)c
 */
	public static void main(String[] args) {
		// 대상 문자열
		String[] str = {"ASDF12","123456","qwerty","as45we","2345AS","A"};
		
		String regex = "^[A-Z\\d]{6}$";	// 6자리 A~Z,0~9
		for(String data : str) {
			System.out.printf("%s\t : %b\n",data,data.matches(regex));
		}
		
		// .com으로 끝나는 이메일 찾기
		String email = "smaple@naver.com,test@test.co.kr,example@example.net,"
				+ "school@school.org,apple@apple.com";
				// , 로 구분해서 찾음
		String regex2 = "([\\w]+@[\\w]+.com)";
		/*
		 		(	   : 식을 하나로 묶음  
		 		[\\w]+ : 영어,숫자,_포함 1개이상
		 		@	   : @
		 		==
		 		.com   : .com
		 		)
		 */
		Pattern p = Pattern.compile(regex2);
		Matcher m = p.matcher(email);
		while(m.find()) {
			System.out.println(m.group());
		}
	}
}
