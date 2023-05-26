files=$(ls)
main=index.html
cat /dev/null > $main
echo '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>文件目录</title></head><body><h1>文件目录</h1><ul>' > $main
for i in $files; do
  if [ $i != 'CNAME' ] && [ $i != 'index.html' ] && [ $i != 'getindex.sh' ] && [ $i != 'main.html' ]; then
    echo '<li><a href="'$i'">'$i'</a></li>' >> $main
  fi
done
echo '</ul></body></html>' >> $main
echo '首页文件生成完毕'
