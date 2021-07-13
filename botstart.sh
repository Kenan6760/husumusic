echo "Current date : $(date) @ $(hostname)"
echo "Network configuration"
echo "Yeni pəncərə yaradılır"
sudo service docker start
echo "Ubuntu lazımsız fayllar təmizlənilir..."
sudo apt-get clean
sudo apt-get autoclean
sudo apt-get autoremove
echo "Docker təmizlənilir"
docker system prune
echo "Ubuntu güncəllənir"
sudo apt-get update -y
sudo apt-get upgrade 
echo "Docker konfinqurasiya edilir"
docker build -t brendplayer .
echo "Konfinqurasiya tamamlandı"
echo "Bot başladılır"
docker run --env-file .env brendplayer
