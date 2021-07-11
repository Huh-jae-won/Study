package 실전Java;

import java.util.function.Consumer;

public class N104_Lambda_Consumer_01 {
	public static void main(String[] args) {
		// Consumer의 accept(T t) : para(o) , ret(x)
		Consumer<String> c = (x)->{
			System.out.printf("Consumer의 accept(T %s) : para(o) , ret(x)\n",x);
		};
		c.accept("aa");
		
		
	}
}
