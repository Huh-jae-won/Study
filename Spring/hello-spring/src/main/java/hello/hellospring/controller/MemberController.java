package hello.hellospring.controller;

import hello.hellospring.domain.Member;
import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

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

    @GetMapping("/members/new")
    public String createForm(){
        return "members/createMemberForm";
    }
    @PostMapping("/members/new")
    public String create(MemberForm form){
        Member member = new Member();
        member.setName(form.getName());

        memberService.join(member);
        return "redirect:/"; // 다시 홈화면으로 돌려보냄
    }

    @GetMapping("/members")
    public String list(Model model){
        List<Member> members = memberService.findMembers();
        model.addAttribute("members", members);
        return "members/memberList";
    }
}
