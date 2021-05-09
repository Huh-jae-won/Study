package 실전Java;

public class N099_RegEx_01 {
	public static void main(String[] args) {
		// 대상 문자열
		String[] str = {
				"ASDF123","123456","qwerty",
				"as09ds","09ahwd","허재원53"};
		
		String regex = "[^0-9]";	// 숫자가 아닌것
		
		for(String data : str) {
			// 숫자가 아닌것은 제거
			System.out.printf("%s\t->\t%s\n",data, data.replaceAll(regex, ""));
		}
	}
}
