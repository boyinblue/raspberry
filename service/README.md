---
title: 라즈베리파이 서비스 등록 방법
description: 우분투 리눅스에 라즈베리파이 서비스를 등록하는 방법에 대해서 설명
---

라즈베리파이 서비스 등록 방법
===


본 페이지에서는 우분투 리눅스에 라즈베리파이 서비스를 
등록하는 방법에 대해서 설명합니다. 


### 서비스 등록


아래 명령을 통해서 raspberry_monitor.service 파일을 생성합니다. 


```bash
$ sudo vi /etc/systemd/system/raspberry_monitor.service
```


아래의 내용을 입력합니다. (raspberry_monitor.service 파일 참조)


```
[Unit]
Description=Raspberry Pi Monitoring Service

[Service]
Type=simple
user=root
ExecStart=python3 service.py
ExecStop=pkill -f 'python3 service.py'
Restart=on-failure
RestartSec=60
WorkingDirectory=/home/parksejin/project/raspberry/service

[Install]
WantedBy=multi-user.target
```


데몬 리로드 합니다.


```bash
$ sudo systemctl daemon-reload
```


서비스를 활성화(enable) 합니다.


```
$ sudo systemctl enable raspberry_monitor
```


서비스를 시작합니다.


```
$ sudo systemctl start raspberry_monitor
```


서비스를 종료합니다.


```
$ sudo systemctl stop raspberry_monitor
```


서비스 상태를 확인합니다. 


```
$ sudo systemctl status raspberry_monitor
```


### 패키지 설치


서비스 실행을 위해서는 몇가지 패키지들이 필요합니다. 


```bash
$ sudo apt-get install python3
```


GPIO 제어를 위해서 python3-rpi.gpio 패키지가 필요합니다. 


```bash
$ sudo apt-get install python3-rpi.gpio
```



