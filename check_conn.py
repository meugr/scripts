#!/usr/bin/python3

"""
Simple script for run in systemd.service
Checking internet connect.

Run as check_conn.py $SERVICE_NAME $CUSTOM_IP_FOR_PING(optional)
"""

from subprocess import Popen, DEVNULL
from typing import List
from time import sleep
import sys


def run_cmd(cmd: str) -> int:
    """Run shell command && return exit code"""
    proc = Popen(cmd, shell=True, stdout=DEVNULL, stderr=DEVNULL)
    proc.wait()
    return proc.returncode


def ping(hosts: List[str]) -> bool:
    """Returns True if any host (str) responds to a ping request."""
    for host in hosts:
        if run_cmd(f'ping -W 2 -c 1 {host}') == 0:
            return True
    return False


if __name__ == "__main__":
    try:
        service = sys.argv[1]

        hosts = ['1.1.1.1', '8.8.8.8']
        try:
            hosts.append(sys.argv[2])
        except IndexError:
            pass
        iteration = 7

        print(f'Start polling connection for {service}', flush=True)
        while True:
            for i in range(iteration):
                answer = ping(hosts)
                if answer:
                    break
                timeout = int(1.5**i)
                print(f'Hosts not answer. Retrying through {timeout} sec...', flush=True)
                if i <= iteration - 1:
                    sleep(timeout)
            else:
                print(f'Remote hosts not answered. Restart {service}', flush=True)
                run_cmd(f'systemctl restart {service}')
            sleep(10)
    except IndexError:
        print('Invalid arguments. Try "check_conn.py systemd_unit host(optional)"', flush=True)
