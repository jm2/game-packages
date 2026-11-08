/*
 * ipv6only.so - make Linux accept the socket layout Windows games expect.
 *
 * Some games (e.g. Wreckfest's THQ Nordic wrapper) bind a dual-stack IPv6
 * socket ([::]:port with IPV6_V6ONLY=0) and then an IPv4 socket on the same
 * port. Windows lets the IPv4 bind through; Linux refuses it (EADDRINUSE), so
 * under Wine the game loses its IPv4 listener and LAN clients can't join.
 * This preload forces IPV6_V6ONLY=1, so the IPv6 socket leaves the IPv4 port
 * free. IPv4 traffic then goes to the game's own IPv4 socket.
 *
 * Don't preload it into a program that relies on a single dual-stack socket
 * for IPv4 (e.g. Wreckfest's dedicated server): that socket becomes IPv6-only.
 *
 * It calls the syscall directly instead of dlsym(RTLD_NEXT), so the library
 * only needs syscall() from glibc and loads inside umu's Steam Runtime too.
 */
#define _GNU_SOURCE
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/syscall.h>
#include <unistd.h>

__attribute__((visibility("default")))
int setsockopt(int fd, int level, int name, const void *val, socklen_t len)
{
    static const int one = 1;
    if (level == IPPROTO_IPV6 && name == IPV6_V6ONLY && len == sizeof(int))
        val = &one;
    return syscall(SYS_setsockopt, fd, level, name, val, len);
}
