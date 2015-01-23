import sys
import os
import getopt
import pwd
import grp
import signal
from daemon import DaemonContext
from daemon.pidlockfile import PIDLockFile

from SIPClientBase import SIPClientBase
from SIPConfigBase import SIPConfigBase


def usage():
    return '-c --config= -d --daemon'

if __name__ == '__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:d", ["config=", "daemon"])
    except getopt.GetoptError as err:
        print(err)
        print(usage())
        sys.exit(2)

    if len(opts) == 0 and len(args) == 0:
        print(usage())
        sys.exit(1)

    config_path = '/etc/sip_emu/sip_emu.config'
    is_daemon = False

    for o, a in opts:
        if o in ("-c", "--config"):
            config_path = a
        elif o in ("-d", "--daemon"):
            is_daemon = True
        else:
            print("unknown option %s" % o)
            print(usage())
            sys.exit(2)

    if not os.path.exists(config_path):
        print("Can't find config: '%s'" % config_path)
        sys.exit(2)

    config = SIPConfigBase(config_path)
    client = SIPClientBase(
        host=config.get('client', 'host'),
        port=config.get('client', 'port'),
        use_ssl=config.get('client', 'use_ssl'),
        auth_key=config.get('client', 'auth_key'),
        logfile=open(config.get('client', 'logfile'), 'a+', 0),
        pidfile=config.get('client', 'pidfile')
    )

    if client.use_ssl():
        client.set_ssl_attrs(
            certfile=config.get('ssl', 'cert'),
            keyfile=config.get('ssl', 'key')
        )

    if is_daemon:
        daemon_context = DaemonContext(
            chroot_directory=config.get('daemon', 'chroot_directory'),
            working_directory=config.get('daemon', 'working_directory'),
            umask=config.get('daemon', 'umask'),
            uid=pwd.getpwnam(config.get('daemon', 'uid')).pw_uid,
            gid=grp.getgrnam(config.get('daemon', 'gid')).gr_gid,
            prevent_core=config.get('daemon', 'prevent_core'),
            detach_process=config.get('daemon', 'detach_process'),
            files_preserve=config.get('daemon', 'files_preserve'),
            pidfile=PIDLockFile(config.get('daemon', 'lockfile'))
        )
        daemon_context.stdout = open(config.get('daemon', 'logfile'), 'a+', 0)
        daemon_context.stderr = daemon_context.stdout
        daemon_context.files_preserve(client.logfile().fileno())
        daemon_context.signal_map = {
            signal.SIGTERM: client.sigterm_handler()
        }
        with daemon_context:
            client.run()

    else:
        client.run()