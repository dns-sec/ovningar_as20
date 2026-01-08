#!/bin/bash
#
# Detta script samlar in systeminformation - RECON
#
# Kan användas för följande attacker:
# Privilegiekartläggning / Post-exploitation recon
# eller exempelvis
# Nätverksrecon inför lateral rörelse
#
# Author: Frans Schartau
# Last Update: 2025-01-01


echo
echo "=== SYSTEMINFO ==="
uname -a

echo
echo "=== AKTUELL ANVÄNDARE ==="
echo $USER

echo
echo "=== ANVÄNDARE MED SHELL ==="
grep "sh$" /etc/passwd

echo
echo "=== NÄTVERK ==="
ip a | grep inet

echo
echo "Distribution:"
echo
cat /etc/os-release | grep -E '^(NAME|VERSION)='
echo -n "Uptime:  "
uptime -p
echo -n "Datum & tid:  "
date
echo

