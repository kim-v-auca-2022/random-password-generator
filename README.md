# random-password-generator
Random password generator written in Python. It is possible to customize length, complexity and symbols in the password. Works in Linux operating systems and best used in bash console as an executable.

## Usage
1. Make sure python 3.12.3 is installed and have sudo priviliges
2. Clone the repository:
```
git clone https://github.com/kim-v-auca-2022/random-password-generator.git
```
3. Go to the cloned repository folder and copy source code into /bin folder:
```
cd random-password-generator
sudo cp password_generator.py /usr/local/bin/password_generator
```
4. Make code executable:
```
sudo chmod +x /usr/local/bin/password_generator
```
5. Now you can execute code from any dictionary:
```
password_generator
```
