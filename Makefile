.PHONY: mds clean

.DEFAULT_GOAL := mds

mds: clean
	./scripts/gen-md.py

clean:
	rm -rf docs/ReadingList.md
	rm -rf docs/labels
	rm -rf docs/conferences
