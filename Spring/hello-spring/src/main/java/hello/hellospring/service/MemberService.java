package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;

import java.util.List;
import java.util.Optional;

public class MemberService {
    private final MemberRepository memberRepository;

    public MemberService(MemberRepository memberRepository) {
        // 생성자 사용 -> 외부 멤버리포지토리를 넣어줌 : Dependency Injection (= DI)
        this.memberRepository = memberRepository;
    }

    /** 회원가입 **/
    public Long join(Member member){
        // 동명이인은 가입 불가
        validateDupName(member);

        memberRepository.save(member);
        return member.getId();
    }

    private void validateDupName(Member member) {
        memberRepository.findByName(member.getName())
                .ifPresent(m->{
            System.out.println("valiDupName = " + m.getName());
            throw new IllegalStateException("이미 존재하는 회원입니다.");
        });
    }
    /** 전체 회원 조회 **/
    public List<Member> findMembers(){
        return memberRepository.findAll();
    }

    public Optional<Member> findOne(Long memberId){
        return memberRepository.findById(memberId);
    }
}
