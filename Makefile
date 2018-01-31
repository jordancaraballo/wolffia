
VERSION=0.22


all: 
	cd interface ; make
	
doc:
	cd doc ; make

builds: all
	cd builds ; make

debian:
	cd builds ; make debian

fedora:
	cd builds ; make fedora

windows:
	cd builds ; make windows

zip:
	cd builds ; make zip

source:
	cd builds ; make source

install: 
	cd builds/debian ; make
	sudo apt-get install builds/debian/wolffia_$(VERSION)-1_all.deb

uninstall:
	sudo apt-get uninstall wolffia

clean:
	cd interface/nanotubeEditor ; make clean
	cd interface/grapheneEditor ; make clean
	cd interface/homopolyEditor ; make clean
	cd interface/classifier ; make clean
	cd interface/main ; make clean
	cd doc; make clean
	cd builds ; make clean
