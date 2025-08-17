Name:           docsis
Version:        0.9.8
Release:        1%{?dist}
Summary:        encode a DOCSIS binary configuration file

License:        GPL
URL:            https://github.com/rlaager/docsis.git
Source:         docsis-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: glib2-devel
BuildRequires: bison
BuildRequires: flex
BuildRequires: net-snmp-devel
BuildRequires: libtool
BuildRequires: which
BuildRequires: diffutils

%description
This program encodes a DOCSIS binary configuration file from a human-readable text configuration file.

%prep
%autosetup


%build
cp /usr/share/automake-1.*/config.guess .
cp /usr/share/automake-1.*/config.sub .
./autogen.sh
%configure CFLAGS=-fPIE
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
/usr/bin/docsis
/usr/lib/debug/usr/bin/docsis-0.9.8-1.el9.x86_64.debug
/usr/share/docsis
/usr/share/snmp/mibs/CLAB-DEF-MIB
/usr/share/snmp/mibs/CLAB-DNS-MIB
/usr/share/snmp/mibs/CLAB-GW-MIB
/usr/share/snmp/mibs/DIFFSERV-DSCP-TC
/usr/share/snmp/mibs/DIFFSERV-MIB
/usr/share/snmp/mibs/DOCS-BPI-MIB
/usr/share/snmp/mibs/DOCS-BPI2-MIB
/usr/share/snmp/mibs/DOCS-BPI2EXT-MIB
/usr/share/snmp/mibs/DOCS-CABLE-DEVICE-MIB
/usr/share/snmp/mibs/DOCS-CABLE-DEVICE-TRAP-MIB
/usr/share/snmp/mibs/DOCS-IETF-BPI2-MIB
/usr/share/snmp/mibs/DOCS-IF-EXT-MIB
/usr/share/snmp/mibs/DOCS-IF-MIB
/usr/share/snmp/mibs/DOCS-IF3-MIB
/usr/share/snmp/mibs/DOCS-IF31-MIB
/usr/share/snmp/mibs/DOCS-MCAST-MIB
/usr/share/snmp/mibs/DOCS-PNM-MIB
/usr/share/snmp/mibs/DOCS-QOS-MIB
/usr/share/snmp/mibs/DOCS-SEC-MIB
/usr/share/snmp/mibs/DOCS-SUBMGT-MIB
/usr/share/snmp/mibs/IGMP-STD-MIB
/usr/share/snmp/mibs/INTEGRATED-SERVICES-MIB
/usr/share/snmp/mibs/PKTC-EVENT-MIB
/usr/share/snmp/mibs/PKTC-IETF-SIG-MIB
/usr/share/snmp/mibs/PKTC-MTA-MIB
/usr/share/snmp/mibs/PKTC-SIG-MIB
/usr/share/snmp/mibs/RMON2-MIB
/usr/share/snmp/mibs/TOKEN-RING-RMON-MIB

# %license add-license-file-here
# %doc add-docs-here



%changelog
* Sun Aug 17 2025 1000
- 
