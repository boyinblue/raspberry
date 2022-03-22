#!/bin/bash

public_ip_file="public_ip.txt"
public_ip_temp_file="tmp/public_ip.txt"
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

function update_issue
{
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
	update_issue ${public_ip_file} 1
fi

