import hashlib
import zlib
from simhash import Simhash


def secure_shorten(url,char_length=8):

    if char_length > 128:
        raise ValueError("char_length {} exceeds 128".format(char_length))
    hash_object = hashlib.sha512(url.encode())
    hash_hex = hash_object.hexdigest()
    return hash_hex[0:char_length]



def shorten_using_builtin(url):
    return hash(url)


def shorten_using_crc(url):
    return zlib.adler32(url)


def shorten_using_Simhash(article):
    return Simhash(article).value



shortened_hash = secure_shorten("https://9to5mac.com/2020/05/18/fbi-links-pensacola-shooter-to-al-qaeda-with-cracked-iphones-with-no-thanks-to-apple/")

shortened2 = shorten_using_builtin("https://9to5mac.com/2020/05/18/fbi-links-pensacola-shooter-to-al-qaeda-with-cracked-iphones-with-no-thanks-to-apple/")

shortened3 = shorten_using_crc(b"https://9to5mac.com/2020/05/18/fbi-links-pensacola-shooter-to-al-qaeda-with-cracked-iphones-with-no-thanks-to-apple/")

shortened22 = shorten_using_builtin("https://9to5mac.com/2020/05/18/fbi-links-pensacola-shooter-to-al-qaeda-with-cracked-iphones-with-no-thanks-to-apple/")

shortenedsim = shorten_using_Simhash("https://9to5mac.com/2020/05/18/fbi-links-pensacola-shooter-to-al-qaeda-with-cracked-iphones-with-no-thanks-to-apple/")