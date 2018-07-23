import sys
import Analisis

if "-pM" in sys.argv:
    Analisis.PingScan(sys.argv[sys.argv.index("-pS") + 1])
    sys.exit(1)

if "-aM" in sys.argv:
    Analisis.ArpScan(sys.argv[sys.argv.index("-aM") + 1])
    sys.exit(1)

if "-sTS" in sys.argv:
    Analisis.SockScan(sys.argv[sys.argv.index("-sTS") + 1])
    sys.exit(1)

if "-sUS" in sys.argv:
    Analisis.SockUDPScan(sys.argv[sys.argv.index("-sUS") + 1])
    sys.exit(1)

if "-fS" in sys.argv:
    if len(sys.argv) == 3:
        Analisis.finScan(sys.argv[sys.argv.index("-fS") + 1], 10)
        sys.exit(1)
    else:
        Analisis.finScan(sys.argv[sys.argv.index("-fS") + 1], int(sys.argv[sys.argv.index("-fS") + 2]))

if "-hsS" in sys.argv:
    Analisis.halfSynScan(sys.argv[sys.argv.index("-hsS") + 1])

if "-aM" in sys.argv:
    Attacks.ARPSpoof(sys.argv[sys.argv.index("-sP") + 1],sys.argv[sys.argv.index("-sP") + 2])
    sys.exit(1)

if "-aD" in sys.argv:
    Attacks.ARPDos(sys.argv[sys.argv.index("-sP") + 1],sys.argv[sys.argv.index("-sP") + 2])
    sys.exit(1)

if "-h" in sys.argv:
    print """
    ==COMPUTER SEARCHING==
    -pS: Make a ping scan. It need an example ip like "192.168.1.0"
    -pA: Make an ARP scan. It need an example ip like "192.168.1.0"

    ==PORT SCAN==
    -sTS Make a socket port scan. It need an IP like "192.168.1.126"
    -sUS Make a socket port scan for UDP. It need an IP like "192.168.1.126"
    -fS Make a FIN port scan. It need an IP like "192.168.1.126". You can set a
    timeout (In secs), 10 is the default time.
    -hsS Make a halfSynScan. It need an IP like "192.168.1.126".
    ==ATTACKS==
    -aD Make an ARP man in the middle attack with the ip forwarding in 1
    -aM Make an ARP man in the middle attack with the ip forwarding in 0
    """
    sys.exit(1)
else:
    print """
What the hell is that argument? Use "-h" option for get help
    """
