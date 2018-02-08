package com.intuit.developer.sample.controller;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import com.intuit.developer.sample.client.OAuth2PlatformClientFactory;

/**
 * @author dderose
 *
 */
@Controller
public class HomeController {
	
	
	@Autowired
	OAuth2PlatformClientFactory factory;
	
	    
	@RequestMapping("/")
	public String home(HttpSession session) {
		session.setAttribute("access_token", factory.getPropertyValue("accessToken"));
        session.setAttribute("refresh_token", factory.getPropertyValue("refreshToken"));
        session.setAttribute("realmId", factory.getPropertyValue("companyid"));
		return "home";
	}
	
	

}
