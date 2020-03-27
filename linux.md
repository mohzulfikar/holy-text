# Useful Linux Command Line Cheatsheet
## The Basics
###Trivial Knowledge:
You can list all available shell in linux using this command
   $ cat /etc/shells

I reccomend to use zshell (+oh-my-zsh) among the other shells with firacode as the monospace font. 

For windows users, you can enable the wsl feature and install linux distro via Microsoft Store, and for the terminal you can use Hyper or Windows Terminal (make sure that the terminal use wsl.exe not bash.exe) 

The tutorial how to setup a good terminal is coming in the future... 

### Basic Command:

- tee -> like t junction, save output stream to a file and forward it into next command as std input
- tty -> print the file name of the terminal connected to standard input
- pwd -> print working directory
- xargs -> build and execute command lines from standard input
- echo -> like print function in the other language
- cd -> change directory
- ls -> list directory contents
    demo: list directory & its file ft. braces expansion
          ls {jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec}_{2017..2022}
    flag : -a list all including hidden file(s) & directories
           -l list with detailed view/long listing format (permission, size, date, etc.)
           -h human readable size (not in bytes)
           -F if directories have a tail '/'
           -R print recursively into subfolder
            
### Navigating :
- touch -> make a file
    usage: touch file
           touch ~/Documents/file
           echo "hello" > hello.txt
           
    demo : making many file using command
        touch {jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec}_{2017..2022}/file{1..100}
        making a file in random folder range
        touch jerami/folder$(shuf -i 1-500 -n 1)/jarum.txt
        
- mkdir -> make directory
    usage: mkdir folder
           mkdir <destination>
           mkdir -p <path>
    flag : -p create entire path even if it doesnt exist
    protip: AVOID USING SPACE(S)
    demo: making many folder using the command
        mkdir {jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec}_{2017..2022}
        
- rm -> remove file(s) or directory
    usage : rm
            rm -r delfolder/
    flag : -r recursively delete folder and its content WITHOUT asking the permission
           -i interactive, asking permission before delete [can be annoying]
           
- rmdir -> remove empty directories
    usage : rmdir deleteme/*
    
- cp -> copy
    usage: cp file1 file2
           cp <file> <destination>
           cp <file1> <file2>.. <destination>
    flag : -r recursively copy folder and its content
    
- mv -> moving & renaming file or directory
    usage : mv <source> <target>
     demo : mv oldfilename newfilename       <-- renaming
            mv oldfoldername/ newfoldername  <-- renaming
            mv newfolder/ ~/Documents/
            mv ~/Document/newfolder/ ./jackpot
            
- locate -> locate/search for file
    usage : locate <path_pattern>
            locate 
    flag : -i turn on case insensitive
           --limit <number> limit result to number
           -S database
           -e <.extension> check existing file that still valid
           --follow
           --existing
           
- upatedb -> update database of file and directory
        needs administrator previleges (sudo)
        
- find -> list every single file(s) and directories
    usage : find <base directories>
                 the default is current folder
            find . -maxdepth 1
            find . -type f -size +100k -size -5M -exec cp {} <destination> \;
    flag : -maxdepth limit depth of folder
           -type <f> for file(s), <d> for directories
           -name "<pattern>" find the path of file(s) that match to the pattern [case sensitive]
           -iname "<pattern>" case insensitive
           -size <+for greater, -for less>k/M/G specify the size of find results
           -o or operator
           -exec <command> \; execute command
           -ok interactive y/n
    demo : menemukan jarum dalam jerami
            find jerami/ -type f -name "jarum" -exec mv {} ~/Desktop \;
            
- sort -> sorting the input stream
    usage : sort <text>
    flag : -r reverse order vertically
           -n sort numerically (by value)
           -u sort uniquely
           -k key definition for sort tabular data
    demo : ls -l /home | head -n 15 | sort -k 5n non-human readable
           ls -lh /home | head -n 15 | sort -k 5h human readable size
           ls -lh /home | head -n 15 | sort -k 6M month coloumn
           
- grep -> search in data
    usage : grep <search_pattern> <source_file1>..
    flag : -c count line that contains <pattern>
           -i case insensitive
           -v show line that not contains <patten>
    demo : grep e hello.txt

- tar -> create a tarball
    usage : tar <flag(s)> <archive_name> <file>..
    flag : -c create new archive 
           -x extract from archive
           -v verbose, speak to user
           -f accept file(s)
           -t test label, check what's inside
           -f file, must with -t flag (-tf)
    demo : tar -cvf taracrchive.tar  file[1-3].txt
           tar -xvf taracrchive.tar
           tar -cvzf archive.tar.gz file[1-3].txt -> compress
           tar -xvzf archive.tar.gz -> extract
           tar -cvjf archive.tar.bz2 file[1-3].txt
           tar -xvjf archive.tar.bz2

- gzip -> compress tarball, faster less compression [.tar.gz]
    gunzip -> uncompress

- bzip2 -> compress tarbal, slower more compression [.tar.bz]
    bunzip2 -> uncompress
    
- zip -> zip file
    demo : zip something.zip file1 file2 file3..
- unzip -> unzip file

- wc -> newline, word, and byte count 
    flag : -l count line

- sudo -> Super User Do - (Like run as administrator on windows but more powerfull)

- cat -> concatenate file(s) including audio etc.
    usage : cat <file(s)>
            cat file[1-5].txt > join.txt

- tac -> reverse output (first become last vice versa [vertically]) of cat, even if it's an audio file!
- rev -> reverse output horizontally by line (if it's a text)

- less -> pager a file like man page

- head -> list first X line [10 by default]
    flag : -n <X> specify how many line(s) to show
- tail -> list last X line [10 by default]
    flag : -n <X> specify how many line(s) to show
    
    
- file -> detect file type (with header)
    usage: file <fileName>
    
- strings -> cat all string variable (printable) and direct it to standard output
    usage: string <fileName>
  
  .
  .
  .
  More coming soon

###Edit on Nano:
nano -> text editor on terminal
CONFIG FILE : /etc/nanorc
shorcuts =>
    ^X = exit
    ^O = save
    ^R = insert content from another file
    ^W = search word case insensitive
    ^\ = replace
    ^K = cut line
    ^U = paste
    ^J = justify text
    ^T = spell checker
    ^C = current position [line&coloumn]
    ^_ = go to the line 'xx'
    M-6 = copy
    M-A = highlight
    M-U = undo
    M-E = redo
    M- => Alt/cmd/esc key, stands for modify-
    ^ => ctrl / control key


###Using VI(iMproved):
VIM -> very powerful cli text editor
Basic command:
    V = enter visual mode
    I = enter insert mode
    Esc = exit current mode or abort command
    :w = save current file
    :q = quit vim
    :q! = quit without saving
    :wq = save and quit vim
    :set nu = set visible number on each line
    :set nonu = unset the line numbering
    gg = go to first byte
    y = yank or copy (while on visual mode) 
    "+y = yank to os clipboard (require extension or use gvim instead)
    p = paste
    dd = delete a line
   

##[File Permissions]
Read : view file(s), or only view content(s) of folder(s)

Write : can edit file, or delete/add file to folder(s)

Execute : can run the file (script)
Modify permissions: we can modify the permissions of file
    >> Read is 4
    >> Write is 2
    >> Execute is 1

##[Features & Symbols]
Tilda [~] : home/
Redirection: create a file based on the command output stream data
    demo = ls -lh > out.txt , overwrite file if exist
           ls -lh >> out.txt , not overwrite the file instead print in newline
          => advanced: we can redirect from standard input and error too using 0 or 2 before '>'
    demo = ./script 0> text
           cat file_that_doesnt_exist 2> err.txt
          => also we can use '<' operator for passing input to a script or command
    demo = sort < names.txt

Braces expansion: for find/search/create file/directory with some pattern
    demo = 
wildcards :
*  = Match 1 or more char  => file* = fileA = fileSOMETHING = file.<extensions>
?  = Match only 1 any char  => file? = file1 = fileA =/= fileAB
[] = Match in the bracket only  => file[1-3] = file1 = file 2 =/= file 4

###[protip]
to view hidden folder use ls -a command
file with '.' prefix = hidden
.  = current folder
.. = parent folder
