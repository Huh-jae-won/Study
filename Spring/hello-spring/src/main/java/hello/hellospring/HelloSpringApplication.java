package hello.hellospring;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HelloSpringApplication {

	public static void main(String[] args) {
		SpringApplication.run(HelloSpringApplication.class, args);
	}

	// Controller 통해서 외부 요청받고
	// Service에서 비즈니스 모델 만들고
	// Repository에서 데이터를 저장
}
