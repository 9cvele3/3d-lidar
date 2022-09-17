from rplidar import RPLidar
import time

def run():
    lidar = RPLidar('/dev/ttyUSB0')

    info = lidar.get_info()
    print(info)

    health = lidar.get_health()
    print(health)

    try:
        for i, scan in enumerate(lidar.iter_scans()):
            print('%d: Got %d measurments' % (i, len(scan)))
            
            for new_scan, quality, angle in scan:
                print("%d %d %d %d", new_scan, quality, angle)

    except KeyboardInterrupt:
        lidar.stop()
        lidar.stop_motor()


    # after you disconnect, the motor will start again
    time.sleep(10)
    lidar.disconnect()

def main():
    run()

if __name__ == "__main__":
    main()
