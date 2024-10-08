package com.bigcat3997.application;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.bigcat3997.library.service.MyService;

@SpringBootApplication(scanBasePackages = "com.bigcat3997.library")
@RestController
public class WeatherForecastApplication {

	private final MyService myService;

	public WeatherForecastApplication(MyService myService) {
		this.myService = myService;
	}

	@GetMapping("/")
	public String home() {
		return myService.message();
	}

	public static void main(String[] args) {
		SpringApplication.run(WeatherForecastApplication.class, args);
	}
}
