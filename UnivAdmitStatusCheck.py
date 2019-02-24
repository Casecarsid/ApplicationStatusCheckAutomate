#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat Feb 16 18:58:26 2019
    
    @author: siddhantkeshkar
    """
def login(emailid,pswd):
    browser.find_element_by_id("email").send_keys(emailid)
    browser.find_element_by_id("password").send_keys(pswd)
    return ;

from selenium import webdriver
chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)

browser.get('https://choose.umn.edu/account/login?r=https%3a%2f%2fchoose.umn.edu%2fapply%2f')
login("enter_your_email_id_here","enter_your_password_here")
browser.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr/td[1]/div/button").click()
print("UMN TWIN CITIES - "+browser.find_element_by_xpath("//*[@id='content']/table/tbody/tr/td[2]").text)

browser.get('https://apply.grad.ucdavis.edu/account/login')
login("enter_your_email_id_here","enter_your_password_here")
browser.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr/td[1]/div/button").click()
print("UC Davis - "+browser.find_element_by_xpath("//*[@id='content']/table/tbody/tr/td[2]").text)

browser.get('https://app.applyyourself.com/AYApplicantLogin/fl_ApplicantConnectLogin.asp?id=umdgrad')
browser.find_element_by_id("ay-login").send_keys("enter_your_username_here")
browser.find_element_by_id("ay-password").send_keys("enter_your_password_here")
browser.find_element_by_xpath("//*[@id='ay-loginSubmit']").click()
print("UMCP - "+browser.find_element_by_xpath("//*[@id='appList']/li/ul/li[1]/ul/li[2]/h4").text)

browser.get('https://apply.gsas.nyu.edu/account/login?r=https%3a%2f%2fapply.gsas.nyu.edu%2fapply%2f')
login("enter_your_email_id_here","enter_your_password_here")
browser.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr/td[1]/div/button").click()
print("NYU - "+browser.find_element_by_xpath("//*[@id='content']/table/tbody/tr/td[2]").text)

browser.get('https://www.applyweb.com/cgi-bin/ustat?formcode=nugrad&newXactMode=no_active_terms')
browser.find_element_by_id("j_username").send_keys("enter_your_email_id_here")
browser.find_element_by_id("j_password").send_keys("enter_your_password_here")
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/form/div[3]/button").click()
print("NWU - "+browser.find_element_by_xpath("//*[@id='ufe-content']/div[1]/div[2]/div[1]/div/div[2]/span").text)

browser.get('https://my.ucsc.edu/psp/csprd/?cmd=login&languageCd=ENG&')
browser.find_element_by_id("username").send_keys("enter_your_username_here")
browser.find_element_by_id("password").send_keys("enter_your_password_here")
browser.find_element_by_xpath("/html/body/div/div/div/div/div[1]/form/div[4]/button").click()
browser.find_element_by_id("shibSubmit").click()
print("UCSC - "+browser.find_element_by_xpath("//*[@id='PTGP_APP_WRK_PTGP_TILE_LIVDAT_1$3$']").text+" Unread Messages")

browser.get('https://grad.apply.colorado.edu/account/login?r=https%3a%2f%2fgrad.apply.colorado.edu%2fapply%2f')
login("enter_your_email_id_here","enter_your_password_here")
browser.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr/td[1]/div/button").click()
print("CU Boulder - "+browser.find_element_by_xpath("//*[@id='content']/table/tbody/tr/td[2]").text)

browser.close()
