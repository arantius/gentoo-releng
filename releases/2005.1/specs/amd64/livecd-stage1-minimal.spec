subarch: amd64
version_stamp: 2005.1
target: livecd-stage1
rel_type: default
profile: default-linux/amd64/2005.1
snapshot: official
source_subpath: default/stage3-amd64-2005.1
livecd/use:
	-*
	ipv6
	socks5
	livecd
	fbcon
	ncurses
	readline
	ssl
	atm

livecd/packages:
	livecd-tools
	gentoo-sources
	dhcpcd
	acpid
	apmd
	fxload
	irssi
	gpm
	syslog-ng
	parted
	links
	raidtools
	dosfstools
	nfs-utils
	jfsutils
	xfsprogs
	e2fsprogs
	reiserfsprogs
	ntfsprogs
	pwgen
	popt
	dialog
	rp-pppoe
	screen
	mirrorselect
	iputils
	hwsetup
	lvm2
	evms
	vim
	pptpclient
	mdadm
	ethtool
	wireless-tools
	prism54-firmware
	coldplug
