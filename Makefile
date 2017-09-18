.PHONY: FORCE

doc.tmp/log: $(wildcard spec/*) FORCE
	rm -fr doc.tmp
	mkdir doc.tmp
	cp -a spec doc.tmp/
	(docker run -v "$${PWD}/doc.tmp":/tmp/bootprint \
		koluchiy/bootprint-docker -s /tmp/bootprint/spec/vmc.yaml) \
	| tee doc.tmp/log

doc: doc.tmp/log
	/bin/rm -fr doc
	/bin/mv -v doc.tmp doc
