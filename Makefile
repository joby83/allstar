CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -O2

all: bfs

bfs: bfs.c
	$(CC) $(CFLAGS) -o bfs bfs.c

clean:
	rm -f bfs

run: bfs
	./bfs

.PHONY: all clean run
