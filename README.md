# loopfail
循环执行一个命令 直到成功为止 适合在强内执行各种容易失败的git蛋疼命令和其他的下载容易失败的命令

你要是图一时之快，那你就`python loopfail/_loopfail.py xxx` 这个`xxx`是你要执行的命令，比如

`python loopfail/_loopfail.py git push origin main`

`python loopfail/_loopfail.py pip install theano`

不过更好的办法是，把这个弔脚本目录添加到环境变量里头去，比如在windows下添加到环境变量中之后，你就可以直接`loopfail xxx`了，更直观易记。linux同理
