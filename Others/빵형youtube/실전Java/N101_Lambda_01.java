package 실전Java;

public class N101_Lambda_01 {
	public static void main(String[] args) {
		
		func1 f = (s) -> {
			// 인터페이서를 활용해서 메소드를 생성함
			System.out.println("f  출력 : "+s);
		};
		f.test("ㅎㅇ");	// 람다식은 @FunctionalInterface 만족해야함
		
		func1 f1 = new func1() {
			// 익명 내부 클래스 : @FunctionalInterface 만족안해도됨
			@Override
			public void test(String aa) {
				System.out.println("f1 출력 : "+aa);
			}
		};
		f1.test("aa");
		 
		// return이 있는 FunctionalInterface 일 때
		func2 f2 = (s)->s;	// return이 "->"의 오른쪽 값
		System.out.println(f2.test("2번"));
		
		func2 f3 = (s)->{
			// 내용을 1줄이상 : {}로
			System.out.println("3번 : "+s);
			return s;
		};
		String ret3 =f3.test("f3");
		System.out.println(ret3);
	}
}

@FunctionalInterface // 추상메소드를 한개만 가짐
interface func1{ 
	public void test(String s);	// abstract 생략가능
}
@FunctionalInterface // 추상메소드를 한개만 가짐
interface func2{
	public String test(String s);
}

