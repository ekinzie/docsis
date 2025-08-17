Building an RPM
---------------

The RPM spec file is located in the `lib` directory.
To build an RPM, create an archive of the source:

    git archive --prefix=docsis-0.9.8/ -o ../docsis-0.9.8.tar HEAD
    gzip ../docsis-0.9.8.tar

and then run rpmbuild:

    dnf -y install rpm-build rpmdevtools 'dnf-command(builddep)'
    dnf builddep lib/docsis.spec
    rpmbuild -ta ../docsis-0.9.8.tar.gz
