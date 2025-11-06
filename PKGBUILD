pkgname=flatinstall
pkgver=1.0
pkgrel=1
pkgdesc="Simple Python-based Flatpak installer"
arch=('any')
url="https://github.com/lkminv/flatinstall"
license=('GPL')
depends=('python' 'flatpak')
source=()
sha256sums=()

package() {
    install -Dm755 "${startdir}/main.py" "$pkgdir/usr/lib/flatinstall/main.py"
    
    install -Dm755 "${startdir}/flatinstall" "$pkgdir/usr/bin/flatinstall"y
    
    if [ -d "${startdir}/src" ] && [ "$(ls -A ${startdir}/src)" ]; then
        cp -r "${startdir}/src" "$pkgdir/usr/lib/flatinstall/"
    fi
}