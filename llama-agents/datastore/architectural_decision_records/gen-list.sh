#!/bin/bash

echo -e '# Architectural Descision Records\n\n' > ADR.md
grep -rE --exclude=ADR-template.md '^title: .*$' \
	| sort | sed -E 's/^\.?\/?((ADR-[0-9]+).+):title: (.+)$/1. [\2 : \3](\1)/g'  >> ADR.md
