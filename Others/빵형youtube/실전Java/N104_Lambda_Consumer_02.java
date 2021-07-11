package 실전Java;

import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;

public class N104_Lambda_Consumer_02 {
	public static void main(String[] args) {
		List<Employee> empList = Arrays.asList(
			new Employee(1,"가",2400),
			new Employee(2,"나",2600),
			new Employee(3,"다",2800),
			new Employee(4,"라",3000)
		);
		
		Consumer<Employee> c = (x)->{
			x.setSalary(x.getSalary()*2);
		};
		
		System.out.println("<<연봉 2배 인상>> ver.1");
		doubleSalary(empList, c.andThen(x->System.out.println(x)));
		// doubleSalary(empList, c.andThen(System.out::println)); 가능 : 메소드 참조 
		
		System.out.println("<<연봉 2배 인상>> ver.2");
		empList.forEach( (x)->{
			x.setSalary(x.getSalary()*2);
			System.out.println(x);
		} );
	}
	private static void doubleSalary(List<Employee> empList,Consumer<Employee> c) {
		for(Employee e : empList) {
			c.accept(e);
		}
	}
}

class Employee{
	private int no;
	private String name;
	private double salary;
	public Employee(int no, String name, double salary) {
		this.no = no;
		this.name = name;
		this.salary = salary;
	}
	public int getNo() {
		return no;
	}
	public void setNo(int no) {
		this.no = no;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getSalary() {
		return salary;
	}
	public void setSalary(double salary) {
		this.salary = salary;
	}
	@Override
	public String toString() {
		return "Employee [no=" + no + ", name=" + name + ", salary=" + salary + "]";
	}
	
	
}
