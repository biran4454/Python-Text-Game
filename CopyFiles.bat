@echo off
title copy data files
echo Copying data files...
xcopy "variable data file defaults" "variable data files" /E /V /Y
echo Data files copied