
VERSION=$(shell grep Version ../debian/debiansrc/control | cut -d' ' -f2)



source: ../dist
	cd .. ; make dist_src
	rm -Rf wolffia$(VERSION)
	mkdir wolffia$(VERSION)
	cp -R ../dist/* wolffia$(VERSION)
	zip -r wolffia$(VERSION)_source.zip wolffia$(VERSION)

clean:
	rm -fR wolffia$(VERSION)_source.zip
	rm -fR wolffia$(VERSION)
