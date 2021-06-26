package 실전Java;

import java.util.function.Supplier;

public class N103_Lambda_Supplier_02 {
	public static void main(String[] args) {
		MessageCenter mc = new MessageCenter("Lambda");
		Supplier<MessageCenter> param = ()->mc;
		MessageCenter main = getMsg(()->mc);
		System.out.println(main);
	}
	public static MessageCenter getMsg(Supplier<MessageCenter>mc) {
		return mc.get();
	}
}

class MessageCenter{
	private final String msg;

	public MessageCenter(String msg) {
		this.msg = msg;
	}

	@Override
	public String toString() {
		return "MC[msg=" + msg + "]";
	}
	
	
}