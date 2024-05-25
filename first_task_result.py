import sys
import logging
import os
from datetime import datetime

# Создаем директорию для логов, если она не существует
log_dir = "log"
log_subdir = f"{sys.argv[0][:-3]}_log"
log_path = os.path.join(log_dir, log_subdir)
os.makedirs(log_path, exist_ok=True)

# Настройка логирования
log_file = os.path.join(log_path, f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_log.txt")
logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Читаем входные данные
b, c = sys.stdin.readline().split()
r, d = sys.stdin.readline().split()

b, c = int(b), int(c)
r, d = int(r), int(d)

# Логируем входные данные
logging.debug(f'Input: b={b}, c={c}, r={r}, d={d}')


count = 0

"""
10000000 100000000
1100000 0"""

z = b * (10 ** 6) + c

while z >= r:
    logging.debug(f'Starting buy_bottle with b={b}, c={c}, r={r}, d={d}, count={count}')

    if c >= r:
        count_add = c // r
        d += count_add * r
        c -= count_add * r

        count += count_add
        logging.debug(f'After buying with c >= r: count_add={count_add}, b={b}, c={c}, d={d}, count={count}')

    b_needs = r // 10 ** 6

    if r % 10**6 == 0:
        count_add = (b*10**6)//r
        b -= count_add * (r//10**6)
        count += count_add


        if b*10**6 + c >= r:
            count += 1

        break

    if b_needs * 10 ** 6 + 10**6 - 1 >= r and b_needs * 10 ** 6 + c >= r:

        c_rep = c // (r % 10**6)
        b_needs_rep = c_rep * b_needs
        logging.debug(
            f'Before while c_rep= {c_rep}, b_needs= {b_needs}')

        if b_needs_rep > b:
            b_needs_rep = b//b_needs

        logging.debug(
            f'Before while c_rep= {c_rep}, b_needs= {b_needs}')

        count_add = (b_needs_rep * 10 ** 6 + c) // r
        b -= b_needs_rep
        c_drop = c - (b_needs_rep * 10 ** 6 + c - r * count_add)
        count += count_add
        c -= c_drop
        d += c_drop

        logging.debug(
            f'After buying with b_needs <= b and b_needs*10**6 + c >= r: count_add={count_add}, b={b}, c={c}, d={d}, count={count}, c_drop={c_drop}, b_needs={b_needs}')
    elif b_needs + 1 <= b:

        b_needs += 1
        c_drop_rep = d//(b_needs*1000000- r)

        if c_drop_rep == 0:
            break

        b_needs_rep = b_needs * c_drop_rep

        if b_needs_rep > b:
            c_drop_rep = b//b_needs
            b_needs_rep = b

        c += c_drop_rep * (b_needs*1000000 - r)
        d -= c_drop_rep * (b_needs*1000000 - r)

        b -= b_needs_rep

        count += c_drop_rep

        logging.debug(
            f'After increasing b_needs and checking d: count_add={count_add}, b={b}, c={c}, d={d}, count={count}, c_drop={c_drop_rep}')
    else:
        logging.debug(f'Cannot proceed: b_needs > b')
        break

    z = b * (10 ** 6) + c

# Логируем выходные данные
logging.debug(f'Output: count= {count}')

print(count)