echo starting build....

:: added manual python download because of authentication issue I could not resolve
wsl docker pull python:3.10

:: Build the docker 
wsl docker build . -t runner:playwright

echo build finished