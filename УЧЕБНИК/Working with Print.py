
# ----------------------------------------------------------------------------------------------------------------------
class sys():
    """ Секундомер в терминале [динамически обновляется]"""
    for i in range(1, 4):
        a = f"\r{'.' * i}{i}"
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rtime out")
