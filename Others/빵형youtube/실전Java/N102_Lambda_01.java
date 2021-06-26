package 실전Java;

import java.util.function.Function;

public class N102_Lambda_01 {
	public static void main(String[] args) {
		Runnable r = () ->{
			// sub_01로 구현해놔야 실행됨
			System.out.println("익명 내부 클래스 실행22");
		};
		r.run();
		
		func f1 = (t)->{
			String ret = "f1 : ";
			for(int i=0 ; i<t ; i++) {
				ret += "만세"+(i)+" ";
			}
			return ret;
		};
		System.out.println(f1.apply(3));
		
		// 기존에 존재하는 함수형인터페이스 활용 -> 자원낭비 감소
		Function<Integer,String> f2 = (t)->{
			String ret = "f2 : ";
			for(int i=0 ; i<t ; i++) {
				ret += "만세"+(i+1)+" ";
			}
			return ret;
		};
		System.out.println(f2.apply(3));
	}
}
@FunctionalInterface
interface func{
	public String apply(int t);
}

