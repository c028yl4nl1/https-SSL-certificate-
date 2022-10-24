import ssl 
import socket 

def https_socket(hostname):
    ### configurando o certificado ssl ###
    conn = ssl.create_connection((hostname, 443))
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    sock = context.wrap_socket(conn, server_hostname=hostname)
    cert = sock.getpeercert(True)
    cert = ssl.DER_cert_to_PEM_cert(cert)
    sock.close()
    ### configurando o socket ###
    socket.timeout(4)
    ssl_requicisao = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    try:
        ssl_requicisao.connect((str(hostname),int(443)))
        ssl_requicisao.send(f'HEAD / HTTP/1.1\r\nHost: {hostname}\r\n'.encode())
        html_open = ssl_requicisao.recv(15560).decode()
        ssl_requicisao.close()
    except:
        print(f' não tive resposta do servidor na porta 443\nCertificado\n{cert}')

    print(f'##certificado ##\n\r{cert}',f'\r\n### Https SSL recv###\n{html_open}')           
         
#https_socket(hostname='google.com')        
host = input('\033[32mDigite o host : ')
https_socket(str(host))
'''
ssl_requicisao = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ssl_requicisao.connect(('www.oprimorico.com.br',443))
ssl_requicisao.send('HEAD / HTTP/1.1\r\nHost www.oprimorico.com.br\r\n'.encode())
html_open = ssl_requicisao.recvmsg(2000)

print(html_open)'''