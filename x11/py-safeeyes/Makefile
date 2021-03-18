# $FreeBSD$

PORTNAME=	safeeyes
DISTVERSION=	2.0.9
CATEGORIES=	x11 python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	samir@noir.im
COMMENT=	GTK application to protect your eyes from eye strain

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}Babel>0:devel/py-babel@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}psutil>0:sysutils/py-psutil@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}xlib>0:x11-toolkits/py-xlib@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}dbus>0:devel/py-dbus@${PY_FLAVOR} \
		libappindicator>0:devel/libappindicator

USES=		python:3.4+ gnome
USE_PYTHON=	autoplist distutils
USE_GNOME=	gtk30 pygobject3

INSTALLS_ICONS= yes

NO_ARCH=	yes

.include <bsd.port.mk>
