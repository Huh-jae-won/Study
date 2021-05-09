package 실전Java;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class N100_RegEx_02 {
	public static void main(String[] args) {
		String str1 = "나는 소년입니다.";
		String str2 = "I'm a boy.";
		Pattern p = Pattern.compile("[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]");
		Matcher m1 = p.matcher(str1);
		Matcher m2 = p.matcher(str2);
		
		System.out.printf("[%s] 한글이 포함 되었나요?\t%b\n",str1,m1.find());
		System.out.printf("[%s] 한글이 포함 되었나요?\t%b\n",str2,m2.find());
	}
}
