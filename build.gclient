# TODO(pphaneuf): Make this be good.

INSTALL_DIR?=$(shell pwd)/install
export INSTALL_DIR
PKG_CONFIG_PATH=$(shell pwd)/install/lib/pkgconfig
export PKG_CONFIG_PATH

PHONY: libunwind tcmalloc openssl protobuf libevent libevhtp gflags glog json-c configure-ct

all: configure-ct

_libunwind:
	if [ -d libunwind ]; then \
		$(MAKE) -C libunwind -f ../certificate-transparency/build/Makefile.unwind; \
		(cd libunwind && git checkout --); \
	fi

_tcmalloc:
	$(MAKE) -C tcmalloc -f ../certificate-transparency/build/Makefile.tcmalloc
	cd tcmalloc && git checkout --

_openssl:
	$(MAKE) -C openssl -f `pwd`/certificate-transparency/build/Makefile.openssl

_protobuf:
	$(MAKE) -C protobuf -f `pwd`/certificate-transparency/build/Makefile.protobuf
	cd protobuf && git checkout --
	cd protobuf/gtest && git checkout -- msvc/

_libevent:
	$(MAKE) -C libevent -f ../certificate-transparency/build/Makefile.libevent
	cd libevent && git reset --hard

_libevhtp:
	$(MAKE) -C libevhtp -f `pwd`/certificate-transparency/build/Makefile.libevhtp
	cd libevhtp && git reset --hard

_gflags:
	$(MAKE) -C gflags -f ../certificate-transparency/build/Makefile.gflags
	cd gflags && git checkout --

_glog:
	$(MAKE) -C glog -f ../certificate-transparency/build/Makefile.glog
	# TODO(alcutter): get these removed in Ben's "fix" branch
	cd glog && git checkout -- config.guess config.sub install-sh

_json-c:
	$(MAKE) -C json-c -f ../certificate-transparency/build/Makefile.json-c
	cd json-c && git checkout --

_configure-ct:
  # TODO(alcutter/pphaneuf): consider inlining the contents of this script:
	certificate-transparency/build/configure-ct
