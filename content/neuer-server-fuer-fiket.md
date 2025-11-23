Title: Neuer Server für Fiket
Date: 2008-07-03 15:53
Tags: Fiket, KurzNotiert, Technik, Schweden
Slug: neuer-server-fuer-fiket
Status: published

Wenn man das hier liest, haben die Nameserver des Internet die frohe
Botschaft propagiert: *Fiket* und alle meine anderen Seiten werden jetzt
von einem neuen Rechner serviert, den ich in den letzten Tagen
aufgesetzt habe. Abgesehen davon, dass die Seite schneller lädt, sollte
alles identisch aussehen und funktionieren. Wenn nicht, bitte ich um
einen
[Kommentar](http://www.fiket.de/2008/07/03/neuer-server-fuer-fiket/#comment).

Für Technikinteressierte: <!--more Weiterlesen &raquo; -->

Der Server, der mir und ein paar Freunden in den letzten Jahren treue
Dienste geleistet hat, wurde durch einen kräftigeren ersetzt, wieder von
[Hetzner](http://www.hetzner.de). Die beiden 500GB-Platten habe ich in
zu einem Raid-1 gemacht, um einem Versagen vorzubeugen. Dann habe ich
den Server mit [Xen](http://www.xen.org/) virtualisiert, wobei die eine
virtuelle Maschine sich nur um meinen Kram kümmert. Die übergeordnete
“Dom0” kümmert sich um die Ressourcenverteilung, das Routing zu den
anderen IP-Adressen und ums Backup. Selbstverständlich läuft überall
[Debian GNU/Linux](http://www.debian.org/index.de.html).

Das Einrichten hat Spaß gemacht, v.a. weil ich Xen bisher nur aus
Beschreibungen kannte. Auf dem Server ist noch eine Menge Platz – falls
jemand Interesse hat, kann man mich gerne
[fragen](http://www.fiket.de/impressum/).

