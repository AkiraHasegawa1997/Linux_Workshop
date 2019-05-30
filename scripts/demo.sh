#!/usr/bin/env bash

# 引数チェック
if [ -z "$1" ]; then
  echo "No name supplied";
  exit 1;
fi

# パスワード発行
(
  printf "$1 "; 
  tr -dc 'a-zA-Z0-9&%$#' < /dev/urandom \
    | fold -w 32 | head -n 1;
) | tee -a demo.out
