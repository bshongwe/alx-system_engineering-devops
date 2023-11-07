# Command line for the win
## SFTP Procedure

1. Used VS Code as the use of my Ubuntu OS terminal seemed to have unresolved issues
-	Navigate to the intranet sandbox selection area
-	click on the SFTP button (to attain the access credentials)

2. Uploading
-	After answering each question, a screenshot was taken (see Task-by-task_snaps directory)
	-	Each screenshot was saved locally (a selected folder on my laptop)
	-	(Note that the required .png files are at the root of the project directory, renamed as specified)
-	Upload paths specifics:
	-	my path was home/dev/pictures/ALX/
	-	my upload path was /alx-system_engineering-devops/command_line_for_the_win
-	In the VS Code terminal, since connected to Git Hub, I pasted the SFTP credentials copied from the intranet
	-	the SFTP interface was invoked, thereafter, using the put command, uploaded the pictures
	-	Note that git config. credentials have already been set due to my VS Code being linked with my Git Hub account
	-	Thus, alternatively, git config. might have to be done to synch local git (laptop) with cloud git (Git Hub)
-	Verification of project screenshot in sandbox:
	-	logg into sandbox via the intranet
	-	using shell navigation commands, navigate to the command_line_for_the_win directory (see bullet 2 of upload paths specifics)
	-	using the ls command, verify contents
-	Uploading from Sandbox to Git Hub:
	-	use git commands:
		-	git add .
		-	git commit - "meaningful message"
		-	git push
-	Verification of project contents on Git Hub:
	-	log onto Git Hub and navigate to alx-system_engineering-devops/command_line_for_the_win
