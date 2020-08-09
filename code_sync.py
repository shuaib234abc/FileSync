import os
import time

def main():
#{
	print("Code sync program started")

	try:
	#{
		while(1==1):
		#{
			# step 1: execute the commands needed
			os.system('rsync -a /home/shoeb/Documents/pos_netcoreangular/frontend/src/ root@10.13.10.107:/home/development/tutorial/tmp/pos_netcoreangular/frontend/src')
			os.system('rm -r /home/shoeb/Documents/pos_netcoreangular/backend/bin >/dev/null 2>&1')	# do not need to sync this folder
			os.system('rm -r /home/shoeb/Documents/pos_netcoreangular/backend/obj >/dev/null 2>&1')	# do not need to sync this folder
			os.system('rsync -a /home/shoeb/Documents/pos_netcoreangular/backend/ root@10.13.10.107:/home/development/tutorial/tmp/pos_netcoreangular/backend')

			# >/dev/null 2>&1 suppresses output of command

			# step 2: sleep for 10 seconds
			time.sleep(10)
		#}

	#}
	except Exception as ex:
	#{
		print(type(ex))
		print(ex)
	#}
#}

if __name__ == "__main__": main()


## credits
# credits: https://janakiev.com/blog/python-shell-commands/
# credits: https://www.programiz.com/python-programming/time/sleep
# https://stackoverflow.com/questions/33985863/hiding-console-output-produced-by-os-system
