import urllib.parse , base64, hashlib

print('################################')
print('###### Encoding Texts ##########')
print('################################')
print("Options : ")
print("[ 1 ] URL Encoding")
print("[ 2 ] Base64 Encoding")
print("[ 3 ] Hash sha256")
print("[ 4 ] Hash sha-1")
print("[ 5 ] Hash MD5")
print('################################')

clear_input = input ("Write Your Text ?").strip()
check_url_type = int(input("Select Option "))

if check_url_type == 1 :
	
	print("### Encoding =>	E")
	print("### Decoding =>	D")
	check =	input ("E Or D ? ").lower()
    
	if check ==	'e' :
		
		encode_input = urllib.parse.quote(clear_input)
		print(f"# Here is your encoded text : \n ({encode_input})")
	else:
		
		decode_input =  urllib.parse.unquote(clear_input)
		print(decode_input)	

elif check_url_type == 2 :
	
	print("### Encoding =>	E")
	print("### Decoding =>	D")
	check =	input("E Or D ").lower()
    
	if check == "e" :
		
		encode_input = base64.b64encode(clear_input.encode())
		print(f"# Here is your encoded text : \n ({encode_input})")
	    
	elif check == "d" :
		
		decode_input = base64.b64decode(clear_input).decode()
		check_save =	input("Do you want to save in file? yes Or no ")
		
		if check_save == "yes" :
			
			myFile =	open("/storage/emulated/0/clean_text.txt", "w")
			myFile.write(f"{decode_input}")
			print("Your text has saved in file named 'clean_text'.")
		else:
			
			print(decode_input)

elif check_url_type == 3 :
	
	hash_object = hashlib.sha256(clear_input.encode())
	hex_dig = hash_object.hexdigest()
	print(f"# Here is your hashed text : \n ({hex_dig})")
	
elif check_url_type == 4 :
	
	hash_object = hashlib.sha1(clear_input.encode())
	hex_dig = hash_object.hexdigest()
	print(f"# Here is your hashed text : \n ({hex_dig})")
	
elif check_url_type == 5 :
	
	hash_object = hashlib.md5(clear_input.encode())
	hex_dig = hash_object.hexdigest()
	print(f"# Here is your hashed text : \n ({hex_dig})")