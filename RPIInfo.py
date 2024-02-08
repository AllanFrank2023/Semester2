import csv
import psutil
import platform
import datetime
from datetime import datetime

class SystemInformation:
    def get_system_information(self):
        # Hent systemoplysninger
        cpu_info = psutil.cpu_percent(interval=1, percpu=True)
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')
        net_if_addrs = psutil.net_if_addrs()
        net_io_counters = psutil.net_io_counters(pernic=True)

        # Hent systemtid og dato
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")

        # Hent operativsystemoplysninger
        os_info = platform.uname()

        # Skriv data til CSV-filen
        with open('InfoRPI.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["System Information"])
            writer.writerow(["CPU Usage (%)"] + cpu_info)
            writer.writerow(["Total Memory (bytes)", memory_info.total])
            writer.writerow(["Free Memory (bytes)", memory_info.available])
            writer.writerow(["Total Disk Space (bytes)", disk_info.total])
            writer.writerow(["Free Disk Space (bytes)", disk_info.free])

            writer.writerow([])
            writer.writerow(["Network Information"])
            for interface, addrs in net_if_addrs.items():
                writer.writerow([f"Interface: {interface}"])
                if interface in net_io_counters:
                    io = net_io_counters[interface]
 #                   writer.writerow(["Status", 'UP' if io.isup else 'DOWN'])
                    writer.writerow(["Sent (bytes)", io.bytes_sent])
                    writer.writerow(["Received (bytes)", io.bytes_recv])
                writer.writerow([])

            writer.writerow(["System Time", current_time])
            writer.writerow(["System Date", current_date])

            writer.writerow([])
            writer.writerow(["Operating System Information"])
            writer.writerow(["System", os_info.system])
            writer.writerow(["Node Name", os_info.node])
            writer.writerow(["Release", os_info.release])
            writer.writerow(["Version", os_info.version])
            writer.writerow(["Machine", os_info.machine])
            writer.writerow(["Processor", os_info.processor])

        print("Data er blevet gemt i InfoRPI.csv")

if __name__ == "__main__":
    system_info = SystemInformation()
    system_info.get_system_information()
