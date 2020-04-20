# fail2ufw
Blocking regular offenenders captured by fail2ban in ufw.

## Why the script
I've been recently facing a bruteforce attack on ssh, coming every few minutes, each time from a different IP.
Fail2Ban was managing it nicely, but I grew bored and impatient because of all these attempts. 
Since at least 50% of the "attacks" were coming from similar IP ranges, I decided to ban them ahead of Fail2Ban - in UFW. 
While the attempts didn't stop, it made Fail2Ban less busy and reduced the number of alerts.

## The use
`python3 fail2ufw.py <your jail name> <number of minimum attempts>`

For example:
`python3 fail2ufw.py sshd 5`

That would firtst query IPs captured by sshd Fail2Ban jail, group them and then ban a subnet where at least 5 IPs were spotted.

## Disclaimer
This is probably a restrictive setup that will block any traffic from `x.x.0.0/16` subnet. I don't mind, but you may want to revise it.
