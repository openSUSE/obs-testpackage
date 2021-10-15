#!/bin/bash
ls -la /gh-actions
zypper -n install make
make -C /gh-actions test
