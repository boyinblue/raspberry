#!/bin/bash
#current_time=$(ssh parksejin@15.26.208.40 "date '+%Y-%m-%d %H:%M:%S'")
current_time=$(ssh parksejin@175.118.12.219 "date '+%Y-%m-%d %H:%M:%S'")
#current_time=$(ssh parksejin@15.38.179.105 "date '+%Y-%m-%d %H:%M:%S'")
timedatectl set-time "$current_time"
