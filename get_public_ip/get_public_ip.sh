#!/bin/bash

public_ip_temp_file="tmp/public_ip.txt"
email_content="tmp/email.txt"

mkdir -p tmp

public_ip=$(curl ifconfig.me)

public_ip_prev=$(cat ${public_ip_temp_file})

if [ "${public_ip}" != "${public_ip_prev}" ]; then
	cp email_header.txt "${email_content}"
	echo "<b>${public_ip}</b>" >> "${email_content}"
	cat "${email_content}" | ssmtp -t -v
	echo "${public_ip}" > "${public_ip_temp_file}"
fi
