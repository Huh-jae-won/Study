package hello.hellospring.controller;
import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

@Controller // controller선언 : 컨테이너에 담아줌
public class MemberController {
    private final MemberService memberService;

    @Autowired // 멤버컨트롤러에 멤버서비스를 연결
    // but controller선언된 멤버컨트롤러는 이미 객체화되있음 but 멤버서비스는 놉(단순 자바 클래스이므로)
    // MemberService에 @Service를 작성
    // MemberRepository의 구현체인 MemoryMemberRepository에 @Repository작성
    // -> 컴포넌트 스캔 방식
    public MemberController(MemberService memberService){
        this.memberService = memberService;
    }
    // 직접 스프링빈 등록방식 -> SpringConfig파일에서 작성
}
