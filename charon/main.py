import subprocess
import os


def status():
	batcmd="iw dev"
	result = subprocess.check_output(batcmd, shell=True)
	print(result.decode(), sep='\n')


def run_commands(commands):
	for command in commands:
		os.system(command)


DOWN_INTERFACE = 'sudo ip link set wlan0 down'
UP_INTERFACE = 'sudo ip link set wlan0 up'


def network_manager(action):
	return 'sudo systemctl {} NetworkManager'.format(action)


def set_interface_type(itype):
	return 'sudo iw wlan0 set {}'.format(itype)


commands = {
	'prepare': [
		network_manager('stop'),
		DOWN_INTERFACE,
		'sudo iw reg set BZ',
		'sudo iw dev wlan0 set txpower fixed 30mBm',
		set_interface_type('monitor control'),
		UP_INTERFACE
	],
	'normal': [
		network_manager('start'),
		DOWN_INTERFACE,
		set_interface_type('type managed'),
		UP_INTERFACE
	]
}


#prepare()
run_commands(commands['normal'])
status()