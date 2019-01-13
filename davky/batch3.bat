@echo off
echo Making folder with your username in c:\...
md c:\%username%
if %errorlevel% == 0 echo Folder %username% successfully created
if %errorlevel% == 1 GOTO end
echo Making text file with tree structure...
tree /a c:\ >>tree.txt
echo Making text file with hidden files with its attributes...
dir c:\Windows /ah-d /s >>hidden.txt
echo Moving text files into the folder...
move /-y tree.txt c:\%username%\tree.txt
move /-y hidden.txt c:\%username%\hidden.txt
:end
pause