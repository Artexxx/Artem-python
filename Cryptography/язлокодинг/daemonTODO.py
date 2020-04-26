import os
import sys
import atexit
import signal

"""
[1 fork]( перед setsid ) удостоверяется, что процесс не является лидером группы процессов.
        Это необходимо для успешного setsid .

[2 fork]( после setsid ) гарантирует, что новая ассоциация с управляющим terminal
        не будет запущена просто путем открытия устройства terminal.
"""


def daemonize(pidfile, *, stdin='/dev/null',
              stdout='/dev/null',
              stderr='/dev/null', ):
    if os.path.exists(pidfile):
        raise RuntimeError('Already running')

    # [1 fork] -- отделяемся от родителя
    try:
        if os.fork() > 0:
            print("[1 -- ok]")
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError("[-] fork 1 failed")

    os.chdir('/')
    os.umask(0)
    # связь с управляющим terminal прерывается
    os.setsid()

    # [2 fork] -- уступаем лидерство в сессии
    try:
        if os.fork() > 0:
            print("[2 -- ok]")
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError("[-] fork 2 failed")

    print(os.getpid())
    # Сброс буферов
    sys.stdout.flush()
    sys.stderr.flush()

    with open(stdin, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open(stdout, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
    with open(stderr, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stderr.fileno())

    # записываем PID-файл
    # удалить PID-файл после сигнала|выхода
    with open(pidfile) as f:
        print(os.getpid, file=f)
    atexit.register(lambda: os.remove(pidfile))

    def sigterm_handler(signal, frame):
        raise SystemExit(1)

    signal.signal(signal.SIGTERM, sigterm_handler)


def main():
    import time
    sys.stdout.write(f'Daemon started with pid {os.getpid()}\n')
    while True:
        sys.stdout.write(f'Daemon Alive!{time.ctime()}')
        time.sleep(10)


if __name__ == '__main__':
    PIDFILE = "/daemon.txt"
    # PIDFILE = "/tmp/daemon.pid"
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [start|stop]", file=sys.stderr)
        raise SystemExit(1)
    if sys.argv[1] == "start":
        try:
            # stdout='/tmp/daemon.log',
            # stderr='/tmp/daemon.log',
            daemonize(PIDFILE,
                      stdout='daemon.log',
                      stderr='daemon.log',
                      )
        except RuntimeError as e:
            print(e, file=sys.stderr)
            raise SystemExit(1)
        main()

    elif sys.argv[1] == "stop":
        if os.path.exists(PIDFILE):
            with open(PIDFILE) as f:
                os.kill(int(f.read()), signal.SIGTERM)
        else:
            print("Not running", file=sys.stderr)
            raise SystemExit(1)
    else:
        print(f"Unknown command {sys.argv[1]}", file=sys.stderr)
        raise SystemExit(1)
