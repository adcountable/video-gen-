#!/bin/bash
# Run this once to install the daily cron job: bash setup_cron.sh
# Schedules run_daily.sh at 9:00am every day

DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="$DIR/run_daily.sh"

chmod +x "$SCRIPT"

# Remove any existing entry for this script
crontab -l 2>/dev/null | grep -v "$SCRIPT" > /tmp/current_cron || true

# Add new entry: 9am daily
echo "0 9 * * * $SCRIPT" >> /tmp/current_cron

crontab /tmp/current_cron
rm /tmp/current_cron

echo ""
echo "✓ Cron job installed. Runs daily at 9:00am."
echo ""
echo "Current crontab:"
crontab -l
echo ""
echo "To remove:  crontab -e  (delete the line)"
echo "Logs:       $DIR/logs/YYYY-MM-DD.log"
echo ""
