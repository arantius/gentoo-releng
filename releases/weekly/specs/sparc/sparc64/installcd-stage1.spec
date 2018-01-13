subarch: sparc64
version_stamp: 2008.0
target: livecd-stage1
rel_type: default
profile: default/linux/sparc/13.0
snapshot: 2008.0
source_subpath: default/stage3-sparc64-2008.0

livecd/use:
	deprecated
	fbcon
	gpm
	ipv6
	livecd
	loop-aes
	lvm1
	ncurses
	nls
	nptl
	nptlonly
	pam
	readline
	socks5
	ssl
	static-libs
	unicode
	xml

livecd/packages:
# Masked (not keyworded, use.masked as well)
#	app-accessibility/brltty
	app-admin/hddtemp
#	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
	app-misc/screen
	app-portage/mirrorselect
	app-text/wgetpaste
#	media-gfx/fbgrab
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-dialup/mingetty
#	net-dialup/penggy
#	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/rdate
	net-misc/vconfig
	net-proxy/dante
# Not keyworded
##	net-proxy/ntlmaps
	net-proxy/tsocks
#	net-wireless/ipw2100-firmware
#	net-wireless/ipw2200-firmware
#	net-wireless/prism54-firmware
#	net-wireless/wireless-tools
#	net-wireless/wpa_supplicant
#	net-wireless/zd1201-firmware
#	net-wireless/zd1211-firmware
	sys-apps/busybox
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/lssbus
	sys-apps/memtester
#	sys-apps/netplug
#	sys-apps/powerpc-utils
#	sys-apps/ibm-powerpc-utils
#	sys-apps/ibm-powerpc-utils-papr
	sys-apps/sdparm
	sys-block/parted
#	sys-block/partimage
	sys-block/qla-fc-firmware
#	sys-boot/yaboot
#	sys-devel/binutils-hppa64
#	sys-devel/gcc-hppa64
#	sys-fs/dmraid
#	sys-fs/dosfstools
	sys-fs/e2fsprogs
#	sys-fs/hfsplusutils
#	sys-fs/hfsutils
#	sys-fs/iprutils
#	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
#	sys-fs/lvm-user
#	sys-fs/mac-fdisk
	sys-fs/mdadm
#	sys-fs/multipath-tools
#	sys-fs/ntfsprogs
#	sys-fs/reiserfsprogs
#	sys-fs/xfsprogs
	sys-libs/gpm
#	sys-power/acpid
	www-client/links
