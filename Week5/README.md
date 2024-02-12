### Q1

With a command like that for example, we can access files on the computer executing the script

``` 
python ping_service.py "1.1.1.1 | cat /etc/passwd"
```

### Q2

First of all, that program does not check the input string so instead of ip address, we can pass commands as input. A second problem is the use of 'shell=True' that means that the program will be executed in the shell, allowing it to run any shell command so it may cause problems of vulnerability.

### Q3

The first problem can be solved by adding few lines checking if the given string is indeed an ip address. For the second one, we can replace shell=True by shell=False and replace the command string by a list of string (something like ["ping", "-c", "4", "{target}"]).

### Q4

I add a function validate_ip_address() that check if the given input matches an ipv4 or ipv6 ip address, if not the command is not executed.

### Q5

To be sure that it is efficient I can test my code with different commands, or ask people specialized in hacking to test it (that is when we are happy to have white hats hackers)
