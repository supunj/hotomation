import schedule
import time
import tinytuya

schedule.clear()


d = tinytuya.OutletDevice('bf58554e8ad68746791nzs', '192.168.50.215', '3bc16bb9028cd949')
d.set_version(3.3)


@schedule.repeat(schedule.every(5).seconds)
def job():
    data = d.status()
    # Show status and state of first controlled switch on device
    print('Dictionary %r' % data)
    print('State (bool, true is ON) %r' % data['dps']['2'])
    switch_state = data['dps']['2']
    data = d.set_status(not switch_state, 2)
    print('set_status() result %r' % data)


while True:
    schedule.run_pending()
    time.sleep(1)
