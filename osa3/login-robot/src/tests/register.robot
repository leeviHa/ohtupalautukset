*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User  kalle  kalle123
    Output Should Contain  New user registered    

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Create User  kalle  kissa123
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Create User  ka  kalle123
    Output Should Contain  Username needs to be at least 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Create User  kalle123  kalle123
    Output Should Contain  Username must only contain letters

Register With Valid Username And Too Short Password
    Create User  kalle  kissa12
    Output Should Contain  Password needs to be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  kalle  kissakissa
    Output Should Contain  Password cannot contain only letters

