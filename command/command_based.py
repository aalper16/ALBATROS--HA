from core.connection import connect_vehicle


connection = input('Start Connection? (Y/N)')

if connection == 'Y' or connection == 'y':
    connection_addr = input('Address: ')
    connection_baud = int(input('Baud: '))

    vehicle = connect_vehicle(connection_addr, baud=connection_baud, wait_ready=True, timeout=120, heartbeat_timeout=120)