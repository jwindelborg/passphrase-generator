#!/usr/bin/env bash

sort word_list | uniq -c | sort -nr | grep -v
