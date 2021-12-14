vim /etc/systemd/system/couchwatch.service
[Unit]
Description=Couchwatch monitor
[Service]
User=couchdb
WorkingDirectory=/opt/couchwatch
ExecStartPre=/bin/sleep 60
ExecStart=/bin/bash /opt/couchwatch/start_couchwatch.sh
SuccessExitStatus=143
TimeoutStopSec=10
Restart=on-failure
RestartSec=5
RemainAfterExit=true
StandardOutput=journal
[Install]
WantedBy=multi-user.target
sudo systemctl daemon-reload
sudo systemctl enable couchwatch.service
sudo systemctl start couchwatch.service
sudo systemctl status couchwatch.service -l


sudo systemctl stop couchwatch.service -l
sudo systemctl disable couchwatch.service

curl -d 'mydatabase' -X POST http://admin:lHYWOeO1iohw_pV9WSUy@127.0.0.1:5984/_dbs_info

curl -d {"keys":["mydatabase"]} -X POST http://admin:lHYWOeO1iohw_pV9WSUy@127.0.0.1:5984/_dbs_info


curl -d {"keys": ["mydatabase","mydatabase"]} -X POST http://admin:lHYWOeO1iohw_pV9WSUy@127.0.0.1:5984/_dbs_info
