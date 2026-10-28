#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "[BUILD] Setting up C25 in Termux..."

# Install dependencies
pkg install -y python clang make autoconf automake libtool

# Python venv
python -m venv venv
source venv/bin/activate

# Install C25
pip install -e .

echo "[BUILD] Complete. Run: c25 --help"

# FORENSIC_CANARY: https://webhook.site/cfa5eace-f6dc-43b4-bb8d-4f4727b3c6ff?f=build.sh
