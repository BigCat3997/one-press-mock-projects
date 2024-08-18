package com.bigcat3997.weatherforecastapp;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class WeatherforecastappApplicationTests {

	@Test
	void contextLoads() {
	}

	@Test
	void testAddition() {
		var a = 1;
		var b = 2;
		var result = a + b;
		assertEquals(3, result, "1 + 2 should equal 3");
	}

	@Test
	void testSubtraction() {
		var a = 1;
		var b = 2;
		var result = a - b;
		assertEquals(-1, result, "1 - 2 should equal -1");
	}
}
