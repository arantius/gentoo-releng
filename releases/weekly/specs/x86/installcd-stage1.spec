subarch: x86
version_stamp: latest
target: livecd-stage1
rel_type: default
profile: default/linux/x86/17.0
snapshot: latest
source_subpath: default/stage3-i486-latest
compression_mode: pixz_x
portage_confdir: @REPO_DIR@/releases/weekly/portage/isos

livecd/use:
	deprecated
	fbcon
	ipv6
	livecd
	loop-aes
	lvm1
	modules
	ncurses
	nls
	pam
	readline
	socks5
	ssl
	static-libs
	unicode
	xml

livecd/packages:
	app-accessibility/brltty
	app-admin/hddtemp
	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
	app-editors/nano
	app-misc/screen
	app-portage/mirrorselect
	app-text/wgetpaste
	media-gfx/fbgrab
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ndisc6
	net-misc/ntp
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-misc/vconfig
	net-proxy/dante
#	net-proxy/ntlmaps
	net-proxy/tsocks
	net-wireless/b43-fwcutter
### Masked (~keywords)
#	net-wireless/bcm43xx-fwcutter
	net-wireless/iw
	net-wireless/rfkill
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/busybox
	sys-apps/dmidecode
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/netplug
	sys-apps/sdparm
	sys-block/parted
	sys-block/partimage
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/f2fs-tools
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	sys-power/acpid
	www-client/links
