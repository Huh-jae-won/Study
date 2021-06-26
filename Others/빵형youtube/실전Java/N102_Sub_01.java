package 실전Java;

public class N102_Sub_01 {

	public static void main(String[] args) {
		Runnable r = new Runnable() {
			@Override
			public void run() {
				System.out.println("익명내부클래스 실행11");
				return;
			}
		};
	}

}
