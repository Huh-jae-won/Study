package 실전Java;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.function.Predicate;


public class N106_Lambda_Predicate_01 {
	public static void main(String[] args) {
		// Predicate의 test(T t) : para(o) , ret(boolean)
		
		// 홀수인지 확인하는 프로그램 작성
		Predicate<Integer> isOdd = (i)->{
			return (i%2==1);
		};
		Predicate<Integer> isEven1 = isOdd.negate();
		Predicate<Integer> isEven2 = Predicate.not(isOdd);
		
		Scanner sc = new Scanner(System.in);
		int  n= 3;
		System.out.printf("%d는 홀수인가요? : %b\n",n,isOdd.test(n));
		System.out.printf("%d는 짝수인가요? : %b\n",n,isEven1.test(n));
		System.out.printf("%d는 짝수인가요? : %b\n",n,isEven2.test(n));
		System.out.println();
		// 로또 당첨 번호 5, 12, 25, 26, 38, 45
		List<Integer> luckNoList = Arrays.asList(5, 12, 25, 26, 38, 45);
		
		Predicate<List<Integer>> isLucky1  = Predicate.isEqual(luckNoList);
		Predicate<List<Integer>> isLucky2  = (l)->{
			if(l.containsAll(luckNoList) && luckNoList.containsAll(l))
				return true;
			return false;
		};
		List<Integer> myList = Arrays.asList(5, 12, 25, 26, 45, 38);
		System.out.println(luckNoList.containsAll(myList));
		System.out.printf("로또 당첨? : %b\n",isLucky1.test(myList));
		System.out.printf("로또 당첨? : %b\n",isLucky2.test(myList));
		
	}
}
