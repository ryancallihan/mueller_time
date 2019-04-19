def clean_text(path):
    text = ''
    with open(path, 'r', encoding='utf-8') as file:
        while True:
            try:
                line = next(file)

                # Check for header
                if line.startswith('\f'):
                    _ = [next(file) for _ in range(3)]
                    continue

                line = line.strip()

                # Check if blank
                if (len(line) == 0):
                    continue

                # Check if page number
                try:
                    float(line)
                    continue
                except ValueError:
                    pass

                # Check Redactions
                if 'Harm to Ongoing Matter' in line:
                    continue

                text += '{} '.format(line)
            except StopIteration:
                print('Read: {}'.format(path))
                break
        file.close()
    return text


def write_text(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)
        file.close()
    print('Wrote text to {}'.format(path))


if __name__ == '__main__':

    vol1_path = './data/mueller_report_vol1.txt'
    vol1 = clean_text(vol1_path)
    write_vol1_path = './data/mueller_report_clean_vol1.txt'
    write_text(write_vol1_path, vol1)

    vol2_path = './data/mueller_report_vol2.txt'
    vol2 = clean_text(vol2_path)
    write_vol2_path = './data/mueller_report_clean_vol2.txt'
    write_text(write_vol2_path, vol2)
