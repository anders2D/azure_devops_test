@echo off
echo Installing pytm...
pip install pytm

echo Running threat analysis...
python threat_model.py > threat-report.md 2>&1

echo Report generated: threat-report.md
type threat-report.md
pause