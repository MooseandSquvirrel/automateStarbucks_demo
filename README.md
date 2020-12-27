<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the upComingEventResults_demo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, upComingEventResults_demo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/MooseandSquvirrel/automateStarbucks_demo.git">
    <img src="images/coffee-cup.png" alt="Gift Card Logo" width="80" height="80">
  </a>

  <h3 align="center">Automate Gift Card Payouts</h3>

  <p align="center">
    A Selenium command-line program to automate the form filling.
    <br />
    <a href="https://github.com/MooseandSquvirrel/automateStarbucks_demo.git"><strong>Explore the docs »</strong></a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![](images/gift.jpg)

This command-line program was created with Selenium Webdriver inorder to automate
a very time consuming and tedious task for a marketing team. They had to pay out winners for promotional events they ran to increase user onboarding, activity, and engagement. Unfortunately, the online form filling for winners took hours and hours.

I built this application to take in arguments of: emails, gift card prices and more.
When it has the info it needs it starts up WebDriver and automates all the form filling. This saved the team many hours of work each week when payout time came.

NOTE: Starbucks has since updated their website in a way that prevents this particular piece of code being usable at this point in time.

### Built With

* [Python 3](https://www.python.org/)
* [Selenium](https://www.selenium.dev/) / [Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/)


<!-- GETTING STARTED -->
## Getting Started

This program was not meant for being open-sourced and therefore
is not for use in it's full functionality to be reproduced locally. However, it can be used as a starting point for Selenium web automation with command-line argument input. 

If you'd like to download the code to have the template for a simple out of the box command-line interface for Selenium programs you're working on, or to just review the code, feel free to clone the repo!

### Prerequisites

* Make sure to have Python 3, Selenium, WebDriver packages:
  ```sh
  pip install selenium
  pip install webdriver-manager
  ```
* Make sure to have the <a href="https://chromedriver.chromium.org/downloads">WebDriver executable</a> for your Chrome version and add it to your PATH.
* **For a tutorial on this process of Selenium / Webdriver set-up, please visit <a href="https://medium.com/@andygardnerucla/automate-your-work-with-selenium-2578d5bf61a8"> my Selenium tutorial!</a>**

### Installation

1. Git clone.
   ```sh
   git clone https://github.com/MooseandSquvirrel/automateStarbucks_demo.git
   ```
2. Run the program.
   ```sh
   python3 payoutS_demo.py
   ```
* NOTE: If Webdriver executable is downloaded for your version of Chrome and added to PATH, and all packages downloaded, it will execute. However, it will no longer
be accessing the proper elements of the pages, since the Starbucks Giftcards site has gone through a major update.

<!-- USAGE EXAMPLES -->
## Usage

A template for creating Selenium command-line programs to automate form filling.

_To view the code: [Documentation](https://github.com/MooseandSquvirrel/automateStarbucks_demo.git)_



<!-- CONTACT -->
## Contact

Andy Gardner - web.dev.bud1@gmail.com

Project Link: [https://github.com/MooseandSquvirrel/automateStarbucks_demo.git](https://github.com/MooseandSquvirrel/automateStarbucks_demo.git)

### Attributes

<div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
