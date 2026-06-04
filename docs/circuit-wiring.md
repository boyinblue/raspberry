# Raspberry 회로 구성 문서 (소스 코드 기준)

이 문서는 코드에 하드코딩된 BCM GPIO 번호를 기준으로 회로 연결을 정리한 문서입니다.
기준 파일은 service/service.py, pwr/pwr.py, pwr/light.py, sensor/sensor.py, led/led.py, buzzer/buzzer.py 및 각 모듈 테스트 스크립트입니다.

## 1) 서비스 기본 회로 (service/service.py)

서비스 시작 시 실제로 사용하는 기본 핀 정의:

- light: BCM 24
- sensor_light: BCM 25
- ir_sensor: BCM 26
- sw1: BCM 4
- sw2: BCM 27
- sw3: BCM 6
- sw4: BCM 19
- buzzer: BCM 13
- pwr 제어: BCM 12 (pwr.pwr_init 기본값)
- RGB LED: BCM 21/20/16 (led.led_init 기본값)

### 기능별 연결표

| 기능 | BCM GPIO | 물리 핀(40핀 헤더) | 코드 근거 |
|---|---:|---:|---|
| Main Light 출력 | 24 | 18 | service/service.py + pwr/light.py |
| Sensor Light 출력 | 25 | 22 | service/service.py + pwr/light.py |
| IR Sensor 입력 | 26 | 37 | service/service.py + sensor/sensor.py |
| SW1 입력 (low active) | 4 | 7 | service/service.py + sensor/sensor.py |
| SW2 입력 (low active) | 27 | 13 | service/service.py + sensor/sensor.py |
| SW3 입력 (low active) | 6 | 31 | service/service.py + sensor/sensor.py |
| SW4 입력 (low active) | 19 | 35 | service/service.py + sensor/sensor.py |
| Buzzer 출력 | 13 | 33 | service/service.py + buzzer/buzzer.py |
| Power 제어 출력 (low active) | 12 | 32 | pwr/pwr.py |
| LED R 출력 | 21 | 40 | led/led.py |
| LED G 출력 | 20 | 38 | led/led.py |
| LED B 출력 | 16 | 36 | led/led.py |

## 2) 신호 극성(Active Level) 요약

코드 기준 전기적 동작 레벨:

- Main Light, Sensor Light: low active
  - LightCtrl(..., True)로 생성됨
  - 출력 LOW일 때 ON, HIGH일 때 OFF
- SW1~SW4: low active 입력
  - Sensor(pin, True) 사용
  - 입력 LOW를 눌림(ON)으로 해석
- Power 제어(BCM 12): low active
  - pwr_on()에서 LOW 출력
  - pwr_off()에서 HIGH 출력
- Buzzer(BCM 13): active high
  - True 출력 시 ON, False 시 OFF
- RGB LED(21/20/16): active high
  - True 출력 시 ON

## 3) 기본 배선 가이드

서비스 운용 기준 최소 연결:

- 출력 계열
  - BCM24 -> Main Light 제어 입력
  - BCM25 -> Sensor Light 제어 입력
  - BCM13 -> Active Buzzer 제어 입력
  - BCM12 -> 외부 전원 제어(릴레이/트랜지스터) 입력
  - BCM21/20/16 -> RGB LED 각 채널
- 입력 계열
  - BCM26 <- IR sensor 출력
  - BCM4/27/6/19 <- 스위치 4개
- 공통
  - 센서, 스위치, 릴레이, LED, 버저와 Raspberry Pi GND 공통 연결
  - 입력 센서는 GPIO 허용 전압(3.3V) 준수

## 4) 모듈별 테스트 스크립트 핀 (서비스와 별도)

아래 스크립트들은 서비스 기본 회로와 핀이 다를 수 있습니다.

| 모듈 | 핀 |
|---|---|
| sensor/sensor_main.py | IR sensor: BCM 18 |
| sensor_light/sensor_light.py | sensor: BCM 18, light: BCM 22 |
| serbo_motor/serbo_motor.py | servo: BCM 19 (기본값) |
| step_motor/step_motor.py | BCM 26, 19, 13, 6 |

## 5) 핀 충돌 주의

서비스와 모듈 테스트를 동시에 돌리면 충돌 가능:

- BCM13: 서비스 buzzer / step_motor 코일
- BCM19: 서비스 sw4 / servo / step_motor 코일
- BCM26: 서비스 ir_sensor / step_motor 코일
- BCM6: 서비스 sw3 / step_motor 코일

권장:

- 서비스 운용 회로와 모터 테스트 회로는 분리
- 모터 테스트 시 서비스 중지 후 실행

## 6) 소스 기준 요약

- 본 프로젝트는 대부분 BCM 모드(GPIO.setmode(GPIO.BCM))를 사용
- 서비스 운용 회로는 service/service.py의 pin_nums가 기준
- 출력 액티브 레벨은 각 모듈 구현(pwr/light/buzzer/led)에서 최종 확인

## 7) 라즈베리파이 5 40핀 핀맵 (물리 핀 기준)

아래는 라즈베리파이 5의 표준 40핀 헤더 핀맵입니다.
`*` 표시는 현재 서비스에서 사용하는 핀입니다.

```
물리핀(왼쪽)                          물리핀(오른쪽)
 1  3V3                           2  5V
 3  GPIO2 / SDA1                  4  5V
 5  GPIO3 / SCL1                  6  GND
 7  GPIO4 *SW1                    8  GPIO14 / TXD
 9  GND                          10  GPIO15 / RXD
11  GPIO17                       12  GPIO18
13  GPIO27 *SW2                  14  GND
15  GPIO22                       16  GPIO23
17  3V3                          18  GPIO24 *Main Light
19  GPIO10 / MOSI                20  GND
21  GPIO9 / MISO                 22  GPIO25 *Sensor Light
23  GPIO11 / SCLK                24  GPIO8 / CE0
25  GND                          26  GPIO7 / CE1
27  GPIO0 / ID_SD                28  GPIO1 / ID_SC
29  GPIO5                        30  GND
31  GPIO6 *SW3                   32  GPIO12 *Power
33  GPIO13 *Buzzer               34  GND
35  GPIO19 *SW4                  36  GPIO16 *LED B
37  GPIO26 *IR Sensor            38  GPIO20 *LED G
39  GND                          40  GPIO21 *LED R
```

### 서비스 사용 핀 빠른 요약

- 입력: BCM 4, 27, 6, 19, 26
- 출력: BCM 24, 25, 13, 12, 21, 20, 16

### 배선 시 주의

- 스위치/센서는 `low active` 설정이 있으므로 기본 풀업/풀다운 회로를 의도대로 맞춰야 함
- 외부 모듈(릴레이, 버저, 센서)과 Raspberry Pi의 GND는 반드시 공통으로 연결
- GPIO는 3.3V 로직 기준이므로 5V 직접 입력 금지
