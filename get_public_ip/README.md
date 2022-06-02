---
title: 라즈베리파이의 공인 IP를 확인하여 변경되었을 경우 관리자에게 알려줌
description: 라즈베리파이의 공인 IP를 확인해서 변경되었을 경우 해당 내용을 메일로 전송하고 또한 GitHub의 이슈 리스트에 자동으로 업데이트하는 스크립트입니다.
---


라즈베리파이의 공인 IP 변경 알림 서비스
===


#### 목적


라즈베리파이로 서버를 구성한 상태에서 공인 IP가 변경될 경우 이를 관리자에게 알려주시 위함입니다. IP가 변경되었을 경우에는 아래 2가지 방법으로 관리자에게 알려줍니다. 


- GitHub에 이슈를 등록합니다. 
- 지정된 이메일로 변경된 IP를 전송합니다. 


#### 환경 설정


아래 2가지 환경이 구성되어야 한다.


- hub 패키지가 설치되어 있어야 한다. (GitHub에 IP 업데이트)
- ssmtp 설정이 되어 있어야 한다. (이메일 전송)


#### ssmtp 설정 방법




