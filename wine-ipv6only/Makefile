CFLAGS ?= -O2
PREFIX ?= /opt/wine-ipv6only

ipv6only.so: ipv6only.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -fPIC -shared -fvisibility=hidden $(LDFLAGS) -o $@ $<

install: ipv6only.so
	install -Dm755 ipv6only.so $(DESTDIR)$(PREFIX)/lib64/ipv6only.so

clean:
	rm -f ipv6only.so

.PHONY: install clean
