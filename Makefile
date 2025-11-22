PY?=uv run python
PELICAN?=uv run pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_HOST=bestbo.se
SSH_PORT=22
SSH_USER=tmy
SSH_TARGET_DIR=/home/tmy/tmy.se


DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif


help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make devserver-global               regenerate and serve on 0.0.0.0    '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make drafts                         list all draft posts               '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	$(PELICAN) "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	$(PELICAN) -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve:
	$(PELICAN) -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve-global:
	$(PELICAN) -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b $(SERVER)

devserver:
	$(PELICAN) -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

devserver-global:
	$(PELICAN) -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b 0.0.0.0

publish:
	$(PELICAN) "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)

rsync_upload: publish
	chmod -R a+rX "$(OUTPUTDIR)"
	rsync -e "ssh -p $(SSH_PORT)" -a --no-checksum --delete "$(OUTPUTDIR)/" $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude --exclude=t --exclude=tmp

drafts:
	@echo "Draft posts:"
	@grep -l "^Status: draft" "$(INPUTDIR)"/*.md 2>/dev/null | xargs -I{} sh -c 'printf "  %-30s %s\n" "$$(basename {})" "$$(grep "^Title:" {} | cut -d: -f2-)"' || echo "  No drafts found"


.PHONY: html help clean regenerate serve serve-global devserver devserver-global publish rsync_upload drafts 
