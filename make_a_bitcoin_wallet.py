# 이 파일을 실행하기 위해서는 python 3.0+과 pip를 먼저 다운로드 받으셔야 합니다
# 파이썬과 pip는 여기서 다운 받으세요: https://www.python.org/downloads/
# 이해가 안되시면 지혜의 족보 영상을 보세요: https://youtu.be/Zb-ClnsxeVM
# 이것은 비트코인을 오래 두는 용도입니다. 거래 편의성으로는 꽝입니다 
# 처음에는 GNC 코인으로 연습하세요
# 나중에는 비트코인 저장하실때 꼭 인터넷이 연결하지 않을 퇴역할 컴퓨터로만 하세요
import bitcoin
import qrcode
import image

# QR 코드 이미지를 저장할 파일경로를 설정해주세요
file_path = f"/Users/byoungjunjo/Downloads/"

# 비밀키 만들기
private_key = bitcoin.random_key()

# 더 높은 보안성을 위해 프린트된 'private_key'를 임의로 바꿔줍니다. 0-9 그리고 a-z 사이에서 자릿수에 맞게끔 바꾸세요
# 잘 이해가 안 되시면 이 영상 6분대 부터 보세요: https://youtu.be/Zb-ClnsxeVM
print(private_key)

decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
compressed_private_key = private_key + '01'
wif_compressed_private_key = bitcoin.encode_privkey(bitcoin.decode_privkey(compressed_private_key, 'hex_compressed'), 'wif_compressed')

# 비밀키 QR 코드 이미지를 생성합니다
private_img = qrcode.make(wif_compressed_private_key)

# QR 코드 이미지를 저장할 본인만의 파일 경로를 입력하세요
# 잘 이해가 안 되시면 이 영상 16분대 부터 보세요: https://youtu.be/Zb-ClnsxeVM
private_img.save(f"{file_path}암호키.png")

# 공개키 만들기
public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')
(public_key_x, public_key_y) = public_key
compressed_prefix = '02' if(public_key_y % 2) == 0 else '03'
hex_compressed_public_key = compressed_prefix + (bitcoin.encode(public_key_x, 16).zfill(64))
print(bitcoin.pubkey_to_address(hex_compressed_public_key))

# 공개키 QR 코드 이미지를 생성합니다
public_img = qrcode.make(hex_compressed_public_key)

# QR 코드 이미지를 저장할 본인만의 파일 경로를 입력하세요
public_img.save(f"{file_path}공개키.png")