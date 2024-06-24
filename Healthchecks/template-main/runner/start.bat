wsl docker run --rm --name runner^
    -e DISPLAY=:0 ^
    -v /tmp/.X11-unix:/tmp/.X11-unix ^
    -v "$PWD"/WeT/mount:/test ^
    runner:playwright

   