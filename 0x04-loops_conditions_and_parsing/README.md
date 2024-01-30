# 0x04. Loops, conditions and parsing
## Background Context

### Resources
Read or watch:
-  Loops sample <link>https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html</link>
-  Variable assignment and arithmetic <link>https://tldp.org/LDP/abs/html/ops.html</link>
-  Comparison operators <link>https://tldp.org/LDP/abs/html/comparison-ops.html</link>
-  File test operators <link>https://tldp.org/LDP/abs/html/fto.html</link>
-  Make your scripts portable <link>https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html</link>

#### man or help:
-  env
-  cut
-  for
-  while
-  until
-  if

## General
-  How to create SSH keys
-  What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
-  How to use while, until and for loops
-  How to use if, else, elif and case condition statements
-  How to use the cut command
-  What are files and other comparison operators, and how to use them
-  Allowed editors: vi, vim, emacs
-  All your files will be interpreted on Ubuntu 20.04 LTS
-  All your files should end with a new line
-  A README.md file, at the root of the folder of the project, is mandatory
-  All your Bash script files must be executable
-  You are not allowed to use awk
-  Your Bash script must pass Shellcheck (version 0.7.0) without any error
-  The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
-  The second line of all your Bash scripts should be a comment explaining what is the script doing

## Shellcheck
Shellcheck <link>https://github.com/koalaman/shellcheck</link> is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

Shellcheck is available on the school’s computers. If you want to use it on your own computer, here is how to install it <link>https://github.com/koalaman/shellcheck#installing</link>.

For all feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code SC2034, you can browse <link>https://github.com/koalaman/shellcheck/wiki/SC2034</link>.

# Tasks
## 0. Create a SSH RSA key pair
mandatory

Read for this task:
-  Linux and Mac OS users <link>https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys</link>
-  Windows users <link>https://docs.rackspace.com/docs/generating-rsa-keys-with-ssh-puttygen</link>
-  man: ssh-keygen

You will soon have to manage your own servers concept page hosted on remote data centers <link>https://www.youtube.com/watch?v=iuqXFC_qIvA&t=46s/link>. We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

Requirements:
-  Share your public key in your answer file 0-RSA_public_key.pub
-  Fill the SSH public key field of your intranet profile with the public key you just generated
-  Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
-  If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase
-  SSH and RSA keys will be covered in depth in a later project.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 0-RSA_public_key.pub
    

## 1. For Best School loop
mandatory

Write a Bash script that displays Best School 10 times.

Requirement:
-  You must use the for loop (while and until are forbidden)

### Tests
-  <code>head -n 2 1-for_best_school</code>
-  <code>./1-for_best_school</code>

Note that:
-  The first line of my Bash script starts with #!/usr/bin/env bash
-  The second line of my Bash scripts is a comment explaining what it is doing

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 1-for_best_school
    

## 2. While Best School loop
mandatory

Write a Bash script that displays Best School 10 times.

Requirements:
-  You must use the while loop (for and until are forbidden)

### Tests
-  <code>./2-while_best_school</code>
 
Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 2-while_best_school
    

## 3. Until Best School loop
mandatory

Write a Bash script that displays Best School 10 times.

Requirements:
-  You must use the until loop (for and while are forbidden)

### Tests
-  <code>./3-until_best_school</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 3-until_best_school
    

## 4. If 9, say Hi!
mandatory

Write a Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line.

Requirements:
-  You must use the while loop (for and until are forbidden)
-  You must use the if statement

### Tests
-  <code>./4-if_9_say_hi</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 4-if_9_say_hi
    

## 5. 4 bad luck, 8 is your chance
mandatory

Write a Bash script that loops from 1 to 10 and:
-  displays bad luck for the 4th loop iteration
-  displays good luck for the 8th loop iteration
-  displays Best School for the other iterations

Requirements:
-  You must use the while loop (for and until are forbidden)
-  You must use the if, elif and else statements

### Tests
-  <code>./5-4_bad_luck_8_is_your_chance</code>

For the most curious:
-  8 in the Chinese culture
-  4 in the Chinese culture

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 5-4_bad_luck_8_is_your_chance
    

## 6. Superstitious numbers
mandatory

Write a Bash script that displays numbers from 1 to 20 and:
-  displays 4 and then bad luck from China for the 4th loop iteration
-  displays 9 and then bad luck from Japan for the 9th loop iteration
-  displays 17 and then bad luck from Italy for the 17th loop iteration

Requirements:
-  You must use the while loop (for and until are forbidden)
-  You must use the case statement

### Tests
-  <code>./6-superstitious_numbers</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 6-superstitious_numbers
    

## 7. Clock
mandatory

Write a Bash script that displays the time for 12 hours and 59 minutes:
-  display hours from 0 to 12
-  display minutes from 1 to 59

Requirements:
-  You must use the while loop (for and until are forbidden)
-  Note that in this example, we only display the first 70 lines using the head command.

### Tests
-  <code>./7-clock | head -n 70</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 7-clock
    

## 8. For ls
mandatory

Write a Bash script that displays:
-  The content of the current directory
-  In a list format
-  Where only the part of the name after the first dash is displayed (refer to the example)

Requirements:
-  You must use the for loop (while and until are forbidden)
-  Do not display hidden files

### Tests
-  <code>ls</code>
-  <code>./8-for_ls</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 8-for_ls
    

## 9. To file, or not to file
mandatory

Write a Bash script that gives you information about the school file.

Requirements:
-  You must use if and, else (case is forbidden)
-  Your Bash script should check if the file exists and print:
    -  if the file exists: school file exists
    -  if the file does not exist: school file does not exist
-  If the file exists, print:
    -  if the file is empty: school file is empty
    -  if the file is not empty: school file is not empty
    -  if the file is a regular file: school is a regular file
    -  if the file is not a regular file: (nothing)

### Tests
-  <code>file school</code>
-  <code>./9-to_file_or_not_to_file</code>
-  <code>touch school/code>
-  <code>./9-to_file_or_not_to_file</code>
-  <code>echo 'betty' > school</code>
-  <code>./9-to_file_or_not_to_file</code>
-  <code>rm school</code>
-  <code>mkdir school</code>
-  <code>./9-to_file_or_not_to_file</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 9-to_file_or_not_to_file
    

## 10. FizzBuzz
mandatory

Write a Bash script that displays numbers from 1 to 100.

Requirements:
-  Displays FizzBuzz when the number is a multiple of 3 and 5
-  Displays Fizz when the number is multiple of 3
-  Displays Buzz when the number is a multiple of 5
-  Otherwise, displays the number in a list format

### Tests
-  <code>./10-fizzbuzz | head -20</code>
 
Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 10-fizzbuzz
    

## 11. Read and cut
#advanced
-  help: read

Write a Bash script that displays the content of the file /etc/passwd.

Your script should only display:
-  username
-  user id
-  Home directory path for the user

Requirements:
-  You must use the while loop (for and until are forbidden)

### Tests
-  <code>./100-read_and_cut</code>
 
Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 100-read_and_cut
    

## 12. Tell the story of passwd
#advanced

Read:
-  IFS (internal field separator) <link>https://tldp.org/LDP/abs/html/internalvariables.html</link>
-  Understanding /etc/passwd <link>https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/</link>

The file /etc/passwd has already been covered in a previous project (0x02. Shell, I/O Redirections and filters) and you should be familiar with it. Today we will make up a story based on it.

Write a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.

Format: The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO

Requirements:
-  You must use the while loop (for and until are forbidden)

### Tests
-  <code>./101-tell_the_story_of_passwd</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 101-tell_the_story_of_passwd
    

## 13. Let's parse Apache logs
#advanced

Apache <link>https://en.wikipedia.org/wiki/Apache_HTTP_Server</link> is among the most popular web servers in the world, serving 50% of all active websites, no doubt that you will have to interact with it within your career.

As a Full-Stack Software Engineer, you have to master the art of parsing log files. Today we will do a simple parsing of Apache log access files.

Today the Customer Support department reported that a user reported that the site is being “buggy”. Not being a detailed description, you want to have a look at the Apache logs and gather data about the traffic.

Write a Bash script that displays the visitor IP along with the HTTP status code <link>https://en.wikipedia.org/wiki/List_of_HTTP_status_codes</link> from the Apache log file.

Requirement:
-  Format: IP HTTP_CODE in a list format
-  You must use awk
You-  are not allowed to use while, for, until and cut
-  Download and commit the apache-access.log file along with your answers files

### Tests
-  <coode>./102-lets_parse_apache_logs | tail -n 10</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 102-lets_parse_apache_logs
    

## 14. Dig the data
#advanced

Now that you’ve parsed the Apache log file, let’s sort the data so you can get a better idea of what is going on.
Using what you did in the previous exercise, write a Bash script that groups visitors by IP and HTTP status code, and displays this data.

Requirements:
-  The exact format must be:
    -  OCCURENCE_NUMBER IP HTTP_CODE
-  In list format
-  Ordered from the greatest to the lowest number of occurrences
-  You must use awk
-  You are not allowed to use while, for, until and cut

### Tests
-  <code>./103-dig_the-data | head -n 10</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x04-loops_conditions_and_parsing
    File: 103-dig_the-data

