# tobin
> Convert text to binary and vice versa

## Installation 

1. Install [addtopath](https://github.com/Simatwa/addtopath).
2. Clone repo and install

```sh
git clone https://github.com/Simatwa/tobin.git
cd tobin
addtopath main.py tobin
```

## Usage

1. Convert ascii to binary 
- `$ tobin -b "<ascii-text>`
> Instance:

```sh
tobin -b "Hello world"

# Output : 01001000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100
```

2. Convert binary to ascii

- `$ tobin <binary>`
> Instance:

```sh
tobin "01001000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100"
# Output : Hello world
```

- For more info run: 

 <details>

 <summary>

 - `$ tobin -h`

 </summary>

```
usage: tobin [-h] [-f FILE] [-b] [message]

Convert text to binary and vice versa

positional arguments:
  message               Message to be
                        converted

options:
  -h, --help            show this help message
                        and exit
  -f FILE, --file FILE  Path to file
                        containing message
  -b, --bin             Convert message to
                        binary

01001000 01100101 01101100 01101100 01101111
00100000 01110101 00110000 01011111 01100001
00110010 00110000 00110011 Hello u0_a203
```
</details>
  

