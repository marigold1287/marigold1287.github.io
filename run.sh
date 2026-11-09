#!/bin/bash
set -e

cd "$(dirname "$0")"


source .venv/bin/activate

exec mkdocs serve -a 127.0.0.1:5000
