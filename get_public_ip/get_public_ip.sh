#!/bin/bash

# Get Serial Number Of Rpi
serial_number=$(cat /proc/cpuinfo | grep Serial | awk '{print $3}')

public_ip_file="IP_${serial_number}.txt"
public_ip_temp_file="tmp/IP_${serial_number}.txt"
email_content="tmp/email.txt"
output_file="tmp/issue_update.json"

id=""
token=""

function get_credential
{
	credential=$(cat ~/.git-credentials)

	#get id from credential
	id=${credential##https://}
	id=${id%%:*}
	echo "id : ${id}"

	#get token fron credential
	credential=${credential##https://${id}:}
	token=${credential%%@*}
	echo "token : ${token}"
}

function get_issue_id
{
  issues=$(hub issue -f%I\|%t%n)
  
  for line in $issues
  do
    if [[ "$line" == *"$1"* ]]; then
      issue_id=${line%%\|*}
      return $issue_id
    fi
  done

  return 0
}

function new_issue
{
  echo "Create Issue : ${1} ${2}"
  input_file=${1}
  msn=${2}

  body=$(cat ${input_file})
  body=${body//\"/\\\"}

  json="{ \"title\" : \"${msn}\",
          \"body\" : \"${body}\",
          \"assignees\" : [\"${id}\"] }"
  echo ${json} | tee ${output_file}

  #echo "{ \"body\" : \"${body}\" }" | \

  cat ${output_file} | \
    curl \
    -X POST \
    -u ${id}:${token} \
    -H "Accept: application/vnd.github.v3+json" \
    --data-binary @- \
    https://api.github.com/repos/${id}/raspberry/issues
}

function update_issue
{
  echo "Update Issue : ${1} ${2}"
  input_file=${1}
  issue_number=${2}
#  output_file=${input_file/.*/.json}

  body=$(cat ${input_file})
  body=${body//\"/\\\"}

  json="{ \"body\" : \"${body}\" }"
  echo ${json} > ${output_file}

  #echo "{ \"body\" : \"${body}\" }" | \

  cat ${output_file} | \
    curl \
    -u ${id}:${token} \
    -X PATCH \
    -H "Accept: application/vnd.github.v3+json" \
    --data-binary @- \
    https://api.github.com/repos/${id}/raspberry/issues/${issue_number}
}

git pull

mkdir -p tmp

if [ "$serial_number" == "" ]; then
  echo "Cannot get serial number!"
  echo "This script can be executed only on Raspberry Pi machine"
  exit 1
fi

# Get Actul Public IP
public_ip=$(curl ifconfig.me)

# Get Previous Publiuc IP
if [ -e ${public_ip_temp_file} ]; then
	public_ip_prev=$(cat ${public_ip_temp_file})
fi

# If IP is changed?
if [ "${public_ip}" != "${public_ip_prev}" ]; then
	# Add GitHub Repository
	echo ${public_ip} > ${public_ip_file}
	git add ${public_ip_file}
	git commit -m "Update public ip file auto"
	git push

	# Send Email
	cp email_header.txt "${email_content}"
	echo "<b>${public_ip}</b>" >> "${email_content}"
	cat "${email_content}" | ssmtp -t -v
	echo "${public_ip}" > "${public_ip_temp_file}"

	# Update GitHub Issue
	get_credential
    get_issue_id "$serial_number"
    issue_id=${?}
    if [ "$issue_id" == "0" ]; then
        new_issue ${public_ip_file} ${serial_number}
    else
        update_issue ${public_ip_file} ${issue_id}
    fi
fi

