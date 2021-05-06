package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.List;

class MemoryMemberRepositoryTest {

    MemoryMemberRepository repository = new MemoryMemberRepository();

    @AfterEach  // callback method
    public void afterEach(){
        repository.clearStore();
    }

    @Test
    public void save(){
        Member member = new Member();
        member.setName("Spring");

        repository.save(member);


        Member person = repository.findById(member.getId()).get();
        System.out.println("person= " + (person==member));
        Assertions.assertThat(member).isEqualTo(person);
    }
    @Test
    public void findByName(){
        Member member1 = new Member();
        member1.setName("Spring");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("Summer");
        repository.save(member2);

        Member person1 = repository.findByName("Spring").get();

        Assertions.assertThat(person1).isEqualTo(member1);
    }
    @Test
    public void findALl(){
        Member member1 = new Member();
        member1.setName("Spring");
        repository.save(member1);
        
        Member member2 = new Member();
        member2.setName("summer");
        repository.save(member2); 
        
        Member member3 = new Member();
        member3.setName("Fall");
        repository.save(member3);

        List<Member> result = repository.findAll();
        Assertions.assertThat(result.size()).isEqualTo(3);
    }

}
