#!/bin/bash
mkdir -p backups
cp -r . backups/backup_$(date +%s)