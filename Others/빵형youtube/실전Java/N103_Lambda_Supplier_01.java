package 실전Java;

import java.util.function.Supplier;

public class N103_Lambda_Supplier_01 {
	public static void main(String[] args) {
		// Runnable의 run() : para(x) , ret(x)
		// Supplier의 get() : para(x) , ret(o)
		Runnable r1 = ()->{
			System.out.println("Runnable의 run() : para(x) , ret(x)");
		};
		Supplier<String> s1 = ()->/*"한줄asdasd"도 가능*/{
			String ret = "Supplier의 get() : para(x) , ret(o)";
			return ret;
		};
		r1.run();
		System.out.println(s1.get());
	}

}
