package hello.hellospring.controller;

import org.springframework.stereotype.Controller;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

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
        return "hello-template";
    }
}