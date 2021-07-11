package 실전Java;

import java.util.function.Function;

public class N105_Lambda_Function_01 {
	public static void main(String[] args) {
		// Function의 apply(T t) : para(o) , ret(o)
		Function<Integer,String> f1 = (i)->{
			String ret = "";
			switch (i) {
			case 1 :
				ret = "one";
				break;
			case 2 :
				ret = "two";
			case 3 :
				ret = "three";
				break;
			case 4 : 
				ret = "four";
			default:
				ret = "other";
				break;
			}
			return ret; 
		};
		System.out.println(f1.apply(3));
		Function<Integer,String> f2 = (i)->{
			String ret = "";
			for(AlphaNum a : AlphaNum.values()) {
				if(i == a.getNum()) {
					ret = a.toString();
					break;
				}
			}
			return ret;
		};
		System.out.println(f2.apply(5));
	}
	
}

enum AlphaNum {
	one(1), two(2), three(3), four(4), five(5);
	private final int num;
	private AlphaNum(int num) {
		this.num = num;
	}
	public int getNum() {
		return num;
	}
}
