.PHONY: build
build:
	# pyinstaller -Fw qtext/__main__.py -n qtext
	pyinstaller qtext.spec

.PHONY: clean
clean:
	rm -rf '$(CURDIR)/build/'
	rm -rf '$(CURDIR)/dist/'
