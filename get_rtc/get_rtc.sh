#!/bin/bash
#current_time=$(ssh parksejin@15.40.187.106 "date '+%Y-%m-%d %H:%M:%S'")
#current_time=$(ssh parksejin@175.118.12.219 "date '+%Y-%m-%d %H:%M:%S'")

ips=("15.26.228.11" "www.dhqhrtnwl.shop")

function get_rtc
{
  ip="${1}"

  echo "ping -c 1 $ip"
  ping -c 1 "${ip}"

  if [ "$?" == "0" ]; then
    current_time=$(ssh parksejin@${ip} "date '+%Y-%m-%d %H:%M:%S'")
    timedatectl set-time "$current_time"
    echo "RTC setting completed"
    exit 0
  fi
}

if [ "${1}" != "" ]; then
  ip="${1}"
  echo "Checking IP ${ip}"
  get_rtc "${ip}"
  exit 0
fi

for ip in ${ips[@]}
do
  echo "Checking IP ${ip}"
  get_rtc "${ip}"
done
