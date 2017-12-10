all:; docker build -t lessrest/dance .
run: all; docker run --rm -v `pwd`:/app lessrest/dance ./start