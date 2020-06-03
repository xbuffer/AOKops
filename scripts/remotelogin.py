import pexpect
import logging


def login_ssh_passwd(port="", user="", host="", passwd=""):
    """
    用于实现pexpect自动登录主机
    :param port:
    :param user:
    :param host:
    :param passwd:
    :return:
    """
    if port and user and host and passwd:
        ssh = pexpect.spawn("ssh -p{port} {user}@{host}".format(port=port, user=user, host=host))
        catch_flag = ssh.expect(['password:', 'Password:', '(yes/no)?'], timeout=3)
        if catch_flag == 0 or catch_flag == 1:
            ssh.sendline(passwd)
        elif catch_flag == 2:
            ssh.sendline('yes\n')
            ssh.expect('password: ')
            ssh.sendline(passwd)
        else:
            logging.error("ssh login error !")
        index = ssh.expect(["#", pexpect.EOF, pexpect.TIMEOUT])
        if index == 0:
            print("Logging in as root !")
        elif index == 1:
            print("Loggin in as non-root !")
        elif index == 2:
            print("Time out !")
    else:
        print("Parameter error !")


if __name__ == '__main__':
    login_ssh_passwd(port='22', user='root', host='10.0.0.61', passwd='1qaz@WSX')
