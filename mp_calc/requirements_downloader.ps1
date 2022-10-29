foreach($line in [System.IO.File]::ReadLines("requirements.txt"))
{
       Start-Process -FilePath "pip" -ArgumentList "install $line"
}
