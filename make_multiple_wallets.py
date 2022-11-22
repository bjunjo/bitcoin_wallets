import bitcoin
import qrcode
import image

# QR 코드 이미지를 저장할 파일경로를 설정해주세요
file_path = f"본인_파일경로_설정"

# 지갑 만들고 싶은 수를 지정하세요
num_wallets = 4

# 지정하신 지갑수만큼 개인키를 생성합니다
for i in range(num_wallets):
    private_key_num_wallets = bitcoin.random_key()
    decoded_private_key_num_wallets = bitcoin.decode_privkey(private_key_num_wallets, 'hex')
    wif_encoded_private_key_num_wallets = bitcoin.encode_privkey(decoded_private_key_num_wallets, 'wif')
    compressed_private_key_num_wallets = private_key_num_wallets + '01'
    wif_compressed_private_key_num_wallets = bitcoin.encode_privkey(bitcoin.decode_privkey(compressed_private_key_num_wallets, 'hex_compressed'), 'wif_compressed')
    
    # 생성된 비밀키들의 QR 코드 이미지 만들어집니다
    private_img = qrcode.make(wif_compressed_private_key_num_wallets)

    # QR 코드 이미지를 저장할 본인만의 파일 경로를 입력하세요
    private_img.save(f"{file_path}암호키_{i + 1}.png")

    # 공개키 만들기
    public_key_num_wallets = bitcoin.fast_multiply(bitcoin.G, decoded_private_key_num_wallets)
    hex_encoded_public_key_num_wallets = bitcoin.encode_pubkey(public_key_num_wallets, 'hex')
    (public_key_x, public_key_y) = public_key_num_wallets
    compressed_prefix = '02' if(public_key_y % 2) == 0 else '03'
    hex_compressed_public_key_num_wallets = compressed_prefix + (bitcoin.encode(public_key_x, 16).zfill(64))

    # 공개키 QR 코드 이미지를 생성합니다
    public_img = qrcode.make(hex_compressed_public_key_num_wallets)

    # QR 코드 이미지를 저장할 본인만의 파일 경로를 입력하세요
    public_img.save(f"{file_path}공개키_{i + 1}.png")
