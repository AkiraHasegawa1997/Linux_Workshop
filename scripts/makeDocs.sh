#!/usr/bin/env bash

# テンプレートの置いてあるディレクトリに移動
cd "$(dirname $0)/../templates"

# テンプレートのファイル全てに対して処理を行う
for i in *.txt; do
  # 色付きファイルを生成
  mkdir -p ../exercises/${i%.txt}
  ../scripts/replace.py c < $i > ../exercises/${i%.txt}/$i

  # 色なしファイルを生成
  mkdir -p ../exercises_plain/${i%.txt}
  ../scripts/replace.py p < $i > ../exercises_plain/${i%.txt}/$i
done
