# 0x05. Processes and signals
## General
What is a PID
What is a process
How to find a process’ PID
How to kill a process
What is a signal
What are the 2 signals that cannot be ignored
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

# Tasks
## 0. What is my PID
mandatory

Write a Bash script that displays its own PID.

### Tests
-  <code>./0-what-is-my-pid</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 0-what-is-my-pid
    

## 1. List your processes
mandatory

Write a Bash script that displays a list of currently running processes.

Requirements:
-  Must show all processes, for all users, including those which might not have a TTY
-  Display in a user-oriented format
-  Show process hierarchy

### Tests
-  <code>./1-list_your_processes | head -50</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 1-list_your_processes
    

## 2. Show your Bash PID
mandatory

Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:
-  You cannot use pgrep
-  The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)

### Tests
-  <code>./2-show_your_bash_pid</code>
 
Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 2-show_your_bash_pid
    

## 3. Show your Bash PID made easy
mandatory

Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:
-  You cannot use ps

### Tests
-  <code>./3-show_your_bash_pid_made_easy</code>
-  <code>./3-show_your_bash_pid_made_easy</code>
 
Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 3-show_your_bash_pid_made_easy
    

## 4. To infinity and beyond
mandatory

Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:
-  In between each iteration of the loop, add a sleep 2

### Tests
-  <code>./4-to_infinity_and_beyond</code>
    -  Note that I ctrl+c (killed) the Bash script in the example.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 4-to_infinity_and_beyond
    

## 5. Don't stop me now!
mandatory

We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:
-  You must use kill

# Terminal #0
## Tests
-  <code>./4-to_infinity_and_beyond</code>

# Terminal #1
## Tests
-  <code>./5-dont_stop_me_now</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 5-dont_stop_me_now
    

## 6. Stop me if you can
mandatory

Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:
-  You cannot use kill or killall

# Terminal #0
### Tests
-  <code>./4-to_infinity_and_beyond</code>

# Terminal #1
### Tests
-  <code>./6-stop_me_if_you_can</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 6-stop_me_if_you_can
    

## 7. Highlander
mandatory

Write a Bash script that displays:
-  To infinity and beyond indefinitely
-  With a sleep 2 in between each iteration
-  I am invincible!!! when receiving a SIGTERM signal
-  Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

# Terminal #0
### Tests
-  <code>./7-highlander</code>

# Terminal #1
### Tests
-  <code>./67-stop_me_if_you_can</code>
-  <code>./67-stop_me_if_you_can</code>
-  <code>./67-stop_me_if_you_can</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 7-highlander
    

## 8. Beheaded process
mandatory

Write a Bash script that kills the process 7-highlander.

# Terminal #0
## Tests
<code>./7-highlander</code>
 
# Terminal #1
## Tests
-  <code>./8-beheaded_process</code>

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 8-beheaded_process
    

## 9. Process and PID file
#advanced

Write a Bash script that:
-  Creates the file /var/run/myscript.pid containing its PID
-  Displays To infinity and beyond indefinitely
-  Displays I hate the kill command when receiving a SIGTERM signal
-  Displays Y U no love me?! when receiving a SIGINT signal
-  Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

## Tests
-  <code>./100-process_and_pid_file</code>
-  Executing the <code>100-process_and_pid_file</code> script and killing it with <code>ctrl+c</code>.

# Terminal #0
## Tests
-  <code>./100-process_and_pid_file</code>
 
# Terminal #1
## Tests
-  <code>sudo pkill -f 100-process_and_pid_file</code>
-  Starting 100-process_and_pid_file in the terminal #0 and then killing it in the terminal #1.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 100-process_and_pid_file
    

## 10. Manage my process
#advanced

Read:
-  & <link>https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html</link>
-  init.d <link>https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/</link>
-  Daemon <link>https://en.wikipedia.org/wiki/Daemon_%28computing%29</link>
-  Positional parameters <link>https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html</link>

-  <strong>man:</strong> sudo

Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: start, restart and stop. The most popular way of doing so on Unix system is to use the init scripts.

Write a manage_my_process Bash script that:
-  Indefinitely writes I am alive! to the file /tmp/my_process
-  In between every I am alive! message, the program should pause for 2 seconds
-  Write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)

Requirements:
-  When passing the argument start:
-  Starts manage_my_process
-  Creates a file containing its PID in <code>/var/run/my_process.pid</code>
-  Displays manage_my_process started
-  When passing the argument stop:
-  Stops manage_my_process
-  Deletes the file <code>/var/run/my_process.pid</code>
-  Displays manage_my_process stopped
-  When passing the argument restart
-  Stops manage_my_process
-  Deletes the file <code>/var/run/my_process.pid</code>
-  Starts manage_my_process
-  Creates a file containing its PID in <code>/var/run/my_process.pid</code>
-  Displays manage_my_process restarted
-  Displays Usage: manage_my_process {start|stop|restart} if any other argument or no argument is passed
-  Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing <code>./101-manage_my_process</code> start, in our case it will simply create a new process instead of saying that it is already started.

### Tests
-  <code>./101-manage_my_process</code>
-  <code>./101-manage_my_process start</code>
-  <code>tail -f -n0 /tmp/my_process</code>
-  <code>sudo ./101-manage_my_process stop</code>
-  <code>cat /var/run/my_process.pid</code>
- <code>tail -f -n0 /tmp/my_process</code>
 
Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 101-manage_my_process, manage_my_process
    

## 11. Zombie
#advanced
Read what a zombie process is <link>https://zombieprocess.wordpress.com/what-is-a-zombie-process/</link>.

Write a C program that creates 5 zombie processes.

Requirements:
-  For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
-  Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
-  When your code is done creating the parent process and the zombies, use the function bellow
    int infinite_while(void)
    {
        while (1)
        {
            sleep(1);
        }
        return (0);
    }
Example:

# Terminal #0
-  <code>gcc 102-zombie.c -o zombie</code>
-  <code>./zombie</code>

# Terminal #1
-  <code>ps aux | grep -e 'Z+.*<defunct>'</code>
 
In Terminal #0, I start by compiling 102-zombie.c and executing zombie which creates 5 zombie processes. In Terminal #1, I display the list of processes and look for lines containing <code>Z+.*<defunct></code> which catches zombie process.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x05-processes_and_signals
    File: 102-zombie.c

