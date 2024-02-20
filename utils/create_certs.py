from OpenSSL import crypto

def cert_gen(
    emailAddress:str="emailAddress",
    commonName:str="commonName",
    countryName:str="NT",
    localityName:str="localityName",
    stateOrProvinceName:str="stateOrProvinceName",
    organizationName:str="organizationName",
    organizationUnitName:str="organizationUnitName",
    serialNumber:int=0,
    validityStartInSeconds:int=0,
    validityEndInSeconds:int=10*365*24*60*60,
    KEY_FILE:str = "private.key",
    CERT_FILE:str="selfsigned.crt",
    ENV_FILE:str='.env'):
    #can look at generated file using openssl:
    #openssl x509 -inform pem -in selfsigned.crt -noout -text
    # create a key pair
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4096)
    # create a self-signed cert
    cert = crypto.X509()
    cert.get_subject().C = countryName
    cert.get_subject().ST = stateOrProvinceName
    cert.get_subject().L = localityName
    cert.get_subject().O = organizationName
    cert.get_subject().OU = organizationUnitName
    cert.get_subject().CN = commonName
    cert.get_subject().emailAddress = emailAddress
    cert.set_serial_number(serialNumber)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(validityEndInSeconds)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha512')
    with open(CERT_FILE, "wt") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
    with open(KEY_FILE, "wt") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))
    f = open(ENV_FILE, 'a')
    f.write(f'SSL_KEYFILE={KEY_FILE}\nSSL_CERTFILE={CERT_FILE}\n\n')
    f.close()

if __name__ == '__main__':
    print('This script should not be run in standalone mode! run one of the generator files instead.')