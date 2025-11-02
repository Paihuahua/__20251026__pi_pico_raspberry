# 這是大標題
## 這是次標題
### 這是次次標題
#### 這是次次次次標題

下面是git初始化設定

```base
git config --global user.name "Paihuahua"
git config --global user.email "a55877a@gmail.com"
git config --global pull.rebase false
```

```
sudo apt update && sudo apt upgrade -y
sudo apt install mosquitto mosquitto-clients -y
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
systemctl status mosquitto
```


'''
分兩個terminal
mosquitto_sub -h localhost -t 客廳/溫度
mosquitto_pub -h localhost -t 客廳/溫度 -m "25度"
'''
