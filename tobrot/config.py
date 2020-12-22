from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1334653293:AAGwSNwkUCgvgxKZTzKLoZVHItpyZTCjUYo"
	APP_ID = 1917410
	API_HASH = "5291638b6743bbe8347a72999d72a938"
	OWNER_ID = 1204927413 #ID of bot owner
	AUTH_CHANNEL = [-1001339069584]
	DESTINATION_FOLDER = "./downloads" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive\nclient_id = 51420638258-774rni6iqdb7get790d8i2035mt97bb2.apps.googleusercontent.com\nclient_secret = tug7bTyMtAMswkyHPKqbyyG5\nscope = drive\nroot_folder_id = 12DMPFBu6irOrYzlLB4ucLvl1k2y0wouB\ntoken = {"access_token":"ya29.a0AfH6SMDslRazcC9UPl-5nzxO5gsIczx467JKJjVQ4AXFZ4gtJgQu62NNkKU4GdcvIVkyCqIbvEmLpdRZB8GyPt2nA6OX_Ub2lO0kBchEZfcFE9FdC_mIvy3Ci2PibYRC3wj8Z3Wi2xZECvNeF-gc9kycC12Z3yhC6gzdfu12q70","token_type":"Bearer","refresh_token":"1//0gM_IJtsD7KL0CgYIARAAGBASNwF-L9IrTO6aTAT7MbP3oKYYgSDJuut_w20GO7Czi_3UxklY3z4Y6cGadl00uX1bF8QA2eCrFXI","expiry":"2020-12-14T13:24:20.057755356+05:30"}"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
