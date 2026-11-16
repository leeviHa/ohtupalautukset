*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Create User
    [Arguments]  ${username}  ${password}
    Input  new
    Input  ${username}
    Input  ${password}
    Run Application
