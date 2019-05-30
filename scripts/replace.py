#!/usr/bin/env python3
import sys

def replaceColored(str):
  return str.replace("<%","[33m").replace("%>","[0m").replace("<$","[92m‣ ")\
      .replace("$>","[0m").replace("<#","[35m").replace("#>","[0m")\
      .replace("<+","[96m").replace("+>","[0m")\
      .replace("===","━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def replacePlain(str):
  return str.replace("<%","").replace("%>","").replace("<$","‣ ").replace("$>","")\
      .replace("<#","").replace("#>","").replace("<+","").replace("+>","")\
      .replace("===","━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def err():
    print("Usage: ./replace.py c/p")
    exit(1)

if __name__=='__main__':
  args = sys.argv
  if len(args) != 2:
    err()
  else:
    if args[1] == 'p' or args[1] == 'p':
      r = replacePlain
    elif args[1] == 'c' or args[1] == 'C':
      r = replaceColored
    else:
      err()

  sin = []
  while True:
    try:
      sin.append(input())
    except EOFError:
      break
  
  print(*[r(i) for i in sin], sep = '\n')
