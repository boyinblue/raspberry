#!/bin/bash

# Get Serial Number Of Rpi
hostname=$(hostname)

serial_number_path="tmp/serial_number.txt"
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

function get_serial_number
{
  # Case1. Raspberry Pi
  serial_number=$(cat /proc/cpuinfo | grep Serial | awk '{print $3}')
  if [ "${serial_number}" != "" ]; then
    return
  fi

  # Case2. General Purpose PC
  # Case2-1. If serial number file is exist
  if [ ! -e "${serial_number_path}" ]; then
    sudo dmidecode -s system-serial-number | tee "${serial_number_path}"
  fi
  serial_number=$(cat "${serial_number_path}")

  # Case2-2. If serial number is empty
  if [ "${serial_number}" == "" ]; then
    sudo dmidecode -s system-serial-number | tee "${serial_number_path}"
    serial_number=$(cat "${serial_number_path}")
  fi

  if [ "${serial_number}" == "To Be Filled By O.E.M." ]; then
    serial_number="None"
  fi
}

function get_issue_id
{
  echo "========================"
  echo "get_issue_id"
  echo "========================"
  issues=$(hub issue -f%I\|%t%n)
  echo "${issues}"
  echo "========================"
  echo ""
  
  OLDIFS=$IFS
  IFS=$'\n'
  for line in $issues
  do
    if [[ "$line" == *"$1"* ]]; then
      issue_id=${line%%\|*}
      echo "issue_id : ${issue_id}"
    fi
  done
  IFS=$OLDIFS

  return $issue_id
}

function new_issue
{
  echo "Create Issue : ${1} ${2}"
  input_file=${1}
  msn=${2}

  body=$(cat ${input_file})
  body=${body//\"/\\\"}

  json="{ \"title\" : \"[${hostname}] ${msn}\",
          \"body\" : \"${body}\",
          \"assignees\" : [\"${id}\"] }"
  echo ${json} | tee ${output_file}

  #echo "{ \"body\" : \"${body}\" }" | \

  set -x
  cat ${output_file} | \
    curl \
    -X POST \
    -u ${id}:${token} \
    -H "Accept: application/vnd.github.v3+json" \
    --data-binary @- \
    https://api.github.com/repos/${id}/raspberry/issues
  set +x
}

function update_issue
{
  echo "Update Issue : ${1} ${2} ${3}"
  input_file=${1}
  issue_number=${2}
  msn=${3}
#  output_file=${input_file/.*/.json}

  body=$(cat ${input_file})
  body=${body//\"/\\\"}

  json="{ \"title\" : \"[${hostname}] ${msn}\",
          \"body\" : \"${body}\" }"
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

# Check Serial Number
get_serial_number
if [ "$serial_number" == "" ]; then
  echo "Cannot get serial number!"
  exit 1
fi
public_ip_file="IP_${serial_number}.txt"
public_ip_temp_file="tmp/IP_${serial_number}.txt"

# Check hub package works
echo "Check hub version"
hub_version=$(hub --version)
if [ "${?}" != "0" ]; then
  echo "Cannot run hub."
  exit 2
fi

# Get Actul Public IP
public_ip=$(curl ifconfig.me)

# Get Previous Publiuc IP
if [ -e "${public_ip_temp_file}" ]; then
  public_ip_prev=$(cat ${public_ip_temp_file})
fi

# If IP is changed?
if [ "${public_ip}" != "${public_ip_prev}" ]; then
  # Add GitHub Repository
  echo "${public_ip}" > ${public_ip_file}
  git add ${public_ip_file}
  git commit -m "Update public ip file auto"
  git push

  # Update GitHub Issue
  get_credential
  get_issue_id "$serial_number"
  issue_id=${?}
  if [ "$issue_id" == "0" ]; then
    new_issue ${public_ip_file} ${serial_number}
  else
    update_issue ${public_ip_file} ${issue_id} ${serial_number}
  fi

  # Send Email
  cp email_header.txt "${email_content}"
  echo "<b>${public_ip}</b>" >> "${email_content}"
  cat "${email_content}" | ssmtp -t -v
  echo "${public_ip}" > "${public_ip_temp_file}"
fi

