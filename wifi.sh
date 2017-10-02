
#Find out the active wireless interface
iwconfig | grep "(\w).*IEEE" -oP > interface.config
ACTIVE_INTERFACE=$(tail -n1 interface.config | cut -f1 -d" ")
echo $ACTIVE_INTERFACE > interface.config

#Disconnect, get new mac address, reconnect
killall NetworkManager
ifconfig $ACTIVE_INTERFACE down
macchanger -r $ACTIVE_INTERFACE
MAC_ADDRESS=$(ifconfig $ACTIVE_INTERFACE | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}')

echo "
auto lo
iface lo inet loopback

auto $ACTIVE_INTERFACE
iface $ACTIVE_INTERFACE inet dhcp
wireless-mode Managed
wpa-ssid ELTE
wpa-ap-scan 1
wpa-proto RSN WPA
wpa-pairwise CCMP TKIP
wpa-group CCMP TKIP
wpa-key-mgmt WPA-EAP
wpa-eap PEAP
wpa-identity $1
wpa-password $2
wpa-phase1 fast_provisioning=1
wpa-pac-file " `pwd` "/cert.crt
" > /etc/network/interfaces


ifconfig $ACTIVE_INTERFACE up

dhclient $ACTIVE_INTERFACE -v

service NetworkManager start


