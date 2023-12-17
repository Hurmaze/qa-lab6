import subprocess as sb

server_ip = '172.25.112.1'

def client(server_ip):
    iperf_command = f"iperf3 -c {server_ip} -t {10}"

    result = sb.run(iperf_command, shell=True, capture_output=True, text=True)

    return result


def parser(result):
    if result.returncode == 0:
        result_arr = result.stdout.split('\n')
        result = []
        for line in result_arr:
            if "sec" in line:
                result.append(line)
        return result
    else:
        print('Error happened: ', result.stdout)
        return []


if __name__ == '__main__':
    try:
        result = client(server_ip)

        parsed_result = parser(result)
        for line in parsed_result:
            print(line)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
