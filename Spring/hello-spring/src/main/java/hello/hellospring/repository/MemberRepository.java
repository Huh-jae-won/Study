package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberRepository {
    Member save(Member member);
    Optional<Member> findById(Long id);
    // 반환값 null때 optional을 활용하여 반환하는 방법
    Optional<Member> findByName(String name);
    List<Member> findAll();

}
