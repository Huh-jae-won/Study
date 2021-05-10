package 실전Java;

public class N101_Lambda_01 {
	public static void main(String[] args) {
		func1 f = (s) -> {
			System.out.println("func1 출력 : "+s);
		};
		// 람다식은 @FunctionalInterface 만족해야함
		f.test("ㅎㅇ");
		
		func1 f1 = new func1() {
			// 익명 내부 클래스 : @~ 만족안해도됨
			@Override
			public void test(String aa) {
				System.out.println("f2 출력 : "+aa);
			}
		};
		
		func2 f2 = (s)->s;
		System.out.println(f2.test("2번"));
		func2 f3 = (s)->{
			System.out.println("3번 : "+s);
			return s;
		};
	}
}

@FunctionalInterface // 추상메소드를 한개만 가짐
interface func1{
	public void test(String s);
}
@FunctionalInterface // 추상메소드를 한개만 가짐
interface func2{
	public String test(String s);
}

