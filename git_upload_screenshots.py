# defaults write com.apple.screencapture "include-date" 0
import sys

date = '10-02'
time = '17.30.05'
symbols = ['!', '[', ']', ':', '/', ' ', '"', '-', '%', '(', ')']

def mov(time, date):
    # print('mv ~/Desktop/Screen\ Shot\ 2022-10-02\ at\ 17.30.05.png ./screenshots/\n')
    print(f'mv ~/Desktop/Screen\ Shot\ 2022-{date}\ at\ {time}.png ./screenshots/\n')

def readme(time, date):
    # link = '![2nd-edition-2](https://github.com/stella-vir/vehicleAutomation/blob/main/screenshots/Screen%20Shot%202022-10-02%20at%2017.30.05.png)'
    link = f'![2nd-edition-2](https://github.com/stella-vir/vehicleAutomation/blob/main/screenshots/Screen%20Shot%202022-{date}%20at%20{time}.png)'
    # escape '\' the escape sign: double '\\'
    esc = '\\'
    res = []

    for s in link:
        if s in symbols:
            res.append(esc)
        res.append(s)
    res = 'echo ' + ''.join(res) + ' >> README.md'
    print(res)
    return res

if __name__ == '__main__':
    print("Argument List:", str(sys.argv))
    mov(sys.argv[1], sys.argv[2])
    readme(sys.argv[1], sys.argv[2])
