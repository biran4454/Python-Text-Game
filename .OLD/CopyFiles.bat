title copy data files
echo Removing directory
rd "variable data files" /s /q
echo Making directory
md "variable data files"
echo Copying files
xcopy "variable data file defaults" "variable data files" /E /V /Y
echo Data files copied