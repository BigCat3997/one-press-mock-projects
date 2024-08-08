package com.bigcat3997.weatherforecastapp.controllers;

import java.util.HashMap;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.bigcat3997.weatherforecastlib.utils.LibraryUtil;

@RestController
@RequestMapping
public class HomeController {

    @GetMapping("/version")
    public String version() {
        LibraryUtil.showMessage("Show version of weather forecast app.");
        return "1.0.0";
    }

    @GetMapping("/info")
    public HashMap<String, String> info() {
        LibraryUtil.showMessage("Show info of weather forecast app.");
        var info = new HashMap<String, String>();
        info.put("name", "Weather Forecast App");
        info.put("version", "1.0.0");
        info.put("description", "This is a simple weather forecast app.");
        return info;
    }
}