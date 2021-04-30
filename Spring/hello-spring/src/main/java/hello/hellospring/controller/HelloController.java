package hello.hellospring.controller;

import org.springframework.stereotype.Controller;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {
    @GetMapping("hello")
    public String hello(Model model) {
        model.addAttribute("data","hello!!");
        return "hello";
    }
    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam(name="name",required = false) String name, Model model ){
        // 외부에서 입력 받아옴 : request false -> 선택
        model.addAttribute("name",name);
        return "hello-template";    // hello-template.html로 이동
    }

    @GetMapping("hello-string")
    @ResponseBody   // http body부분에 내가 직접 넣어주겠다 
                    // -> localhost8080/hello-string?name=""의 페이지 소스보기 하면 비교가능
    public String helloString(@RequestParam("name") String name){
        return "hello " + name;
    }

    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name){
        Hello hlo = new Hello();
        hlo.setName(name);
        // Json형태의 페이지소스를 확인할 수 있다
        return hlo; // Json형태로 반환 -> 요즘은 거의다 이런 방식으로
    }

    static class Hello{
        private String name;

        public String getName() {
            return name;
        }
        public void setName(String name) {
            this.name = name;
        }

    }

}