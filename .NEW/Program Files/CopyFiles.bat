title copy data files

echo Copying files
xcopy "FixedData\PlayerProperties" "VariableData\Player" /E /V /Y
rd "VariableData\EnemyHealth" /s /q
md "VariableData\EnemyHealth"