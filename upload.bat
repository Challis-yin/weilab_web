set v=%date:~0,4%%date:~5,2%%date:~8,2%
git add .
git commit -m "ycl%v%"
git pull
git push

docker build -f Dockerfile -t weilabweb:%v% .
docker save weilabweb:%v% >1.tar
scp 1.tar root@149.129.89.106:/root
echo “上传完成，请登录服务器目录运行runweilabweb.sh”
del 1.tar
pause