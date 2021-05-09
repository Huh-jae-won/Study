package 실전Java;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class N096_RegEx_01 {
/*
 	^ : 문자열or행의  처음
 	$ : 문자열or행의 끝
 	[] : 괄호 안 문자 중 하나 선택 	ex) [abc]d = ab,bd,cd 가능
 	[^]: 괄호 안 문자 모두 안됨 		ex) [^abc]d = ab,bd,cd는 빼고 가능
 	* : 0회 이상				ex) a*b = b, ab, aab, aaab, ... 가능
 	+ : 1회 이상				ex) a+b =  ab, aab, aaab, ... 가능
 	{m,n} : m이상 n이하 횟수 		ex) a{1,3} = ab, aab, aaab,(aaaab는 x) 
  	...
*/
	public static void main(String[] args) {
		// 대상 문자열
		String str = "12363-45-9#";
		String regex1 = "^[0-9]*$";		// 모두 숫자인지 확인
		String regex2 = "^[\\d-]*$";	// \\d : 숫자인지
										// -도 있는지
		String regex3 = "^[\\d-#]*$";	// regex2에 #추가
		
		str.matches(regex3);	// 한번에 사용하는법
		if(!str.matches(regex3)) {
			// 이런식으로 활용가능
			System.out.println("숫자를 입력하시오.");
		}
		
		Pattern p1 = Pattern.compile(regex1);
		Pattern p2 = Pattern.compile(regex2);
		Pattern p3 = Pattern.compile(regex3);
		
		Matcher m1 = p1.matcher(str);
		Matcher m2 = p2.matcher(str);
		Matcher m3 = p3.matcher(str);
		
		System.out.println(m1.find());	// T or F
		System.out.println(m2.find());
		System.out.println(m3.find());
	}
}
