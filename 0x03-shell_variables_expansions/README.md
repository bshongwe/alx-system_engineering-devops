# 0x03. Shell, init files, variables and expansions
General

    What happens when you type $ ls -l *.txt

## Shell Initialization Files

    What are the /etc/profile file and the /etc/profile.d directory
    What is the ~/.bashrc file

## Variables

    What is the difference between a local and a global variable
    What is a reserved variable
    How to create, update and delete shell variables
    What are the roles of the following reserved variables: HOME, PATH, PS1
    What are special parameters
    What is the special parameter $??

## Expansions

    What is expansion and how to use them
    What is the difference between single and double quotes and how to use them properly
    How to do command substitution with $() and backticks

## Shell Arithmetic

    How to perform arithmetic operations with the shell

## The alias Command

    How to create an alias
    How to list aliases
    How to temporarily disable an alias


# Task 0.
## mandatory

Create a script that creates an alias.

    Name: ls
    Value: rm *

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 0-alias


# Task 1. Hello you
## mandatory

Create a script that prints hello user, where user is the current Linux user.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 1-hello_you


# Task 2.
## mandatory

Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 2-path


# Task 3.
## mandatory

Create a script that counts the number of directories in the PATH.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 3-paths


# Task 4.
## mandatory

Create a script that lists environment variables.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 4-global_variables


# Task 5.
## mandatory

Create a script that lists all local variables and environment variables, and functions.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 5-local_variables


# Task 6. Local variable
## mandatory

Create a script that creates a new local variable.

    Name: BEST
    Value: School

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 6-create_local_variable


# Task 7.
## mandatory

Create a script that creates a new global variable.

    Name: BEST
    Value: School

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 7-create_global_variable


# Task 8.
## mandatory

Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.


Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 8-true_knowledge


# Task 9.
## mandatory

Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.

    POWER and DIVIDE are environment variables

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 9-divide_and_rule


# Task 10.
## mandatory

Write a script that displays the result of BREATH to the power LOVE

    BREATH and LOVE are environment variables
    The script should display the result, followed by a new line

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 10-love_exponent_breath


# Task 11.
## mandatory

Write a script that converts a number from base 2 to base 10.

    The number in base 2 is stored in the environment variable BINARY
    The script should display the number in base 10, followed by a new line

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 11-binary_to_decimal


# Task 12.
## mandatory

Create a script that prints all possible combinations of two letters, except oo.

    Letters are lower cases, from a to z
    One combination per line
    The output should be alpha ordered, starting with aa
    Do not print oo
    Your script file should contain maximum 64 characters

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 12-combinations


# Task 13.
## mandatory

Write a script that prints a number with two decimal places, followed by a new line.

The number will be stored in the environment variable NUM.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 13-print_float


# Task 14.
## advanced

Write a script that converts a number from base 10 to base 16.

    The number in base 10 is stored in the environment variable DECIMAL
    The script should display the number in base 16, followed by a new line

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 100-decimal_to_hexadecimal


# Task 15.
## advanced

Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 101-rot13


# Task 16.
## advanced

Write a script that prints every other line from the input, starting with the first line.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 102-odd


# Task 17.
## advanced

Write a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.

    WATER is in base water
    STIR is in base stir.
    The result should be in base bestchol

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x03-shell_variables_expansions
    File: 103-water_and_stir



