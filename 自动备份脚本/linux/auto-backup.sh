echo "欢迎使用自动备份存档工具"

if [ ! -f "./PalServer.sh" ]; then
	echo "请确保你将该脚本放置在帕鲁服务器目录下后运行"
	exit 1
fi

while true; do
    now_dir_name="$(date +"%Y-%m-%d/%H_%M")/"
    echo "$(date +"%Y-%m-%d %H:%M:%S />") 创建目录：$(pwd)/auto-backup/${now_dir_name}"
    mkdir -p ./auto-backup/${now_dir_name}
    if cp -r ./Pal/Saved/SaveGames/* ./auto-backup/${now_dir_name}; then
        echo "$(date +"%Y-%m-%d %H:%M:%S />") 备份成功"
    else
        echo "$(date +"%Y-%m-%d %H:%M:%S />") 备份失败 请检查错误信息"
        exit 1
    fi
    sleep 30m
done
