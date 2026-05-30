#!/bin/bash
# Daily cron wrapper — called by launchd/cron at 9am
# Handles environment, logging, and error notification

set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="$DIR/logs"
LOG_FILE="$LOG_DIR/$(date +%Y-%m-%d).log"

mkdir -p "$LOG_DIR"

# Load Homebrew (needed if Python isn't in default cron PATH)
if [ -f /opt/homebrew/bin/brew ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# Load .env
if [ -f "$DIR/.env" ]; then
    set -a && source "$DIR/.env" && set +a
fi

echo "========================================" >> "$LOG_FILE"
echo "Started: $(date)" >> "$LOG_FILE"
echo "========================================" >> "$LOG_FILE"

cd "$DIR"

python3 scheduler.py "$@" >> "$LOG_FILE" 2>&1
EXIT_CODE=$?

echo "Finished: $(date) (exit $EXIT_CODE)" >> "$LOG_FILE"

# Optional: send a macOS notification when done
if command -v osascript &>/dev/null; then
    if [ $EXIT_CODE -eq 0 ]; then
        osascript -e 'display notification "Daily uploads complete ✓" with title "YouTube Bot"' 2>/dev/null || true
    else
        osascript -e 'display notification "Upload failed — check logs" with title "YouTube Bot ⚠️"' 2>/dev/null || true
    fi
fi

exit $EXIT_CODE
