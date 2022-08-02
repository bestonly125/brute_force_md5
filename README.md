# Модель по перебору MD5 хешей с помощью библиотеки hashcat
## Требуется установить одну из рекомендуемых ниже библиотек (согласно вашей видеокарты): 
- AMD GPUs on Linux require "RadeonOpenCompute (ROCm)" Software Platform (3.1 or later)
- AMD GPUs on Windows require "AMD Radeon Adrenalin 2020 Edition" (20.2.2 or later)
- Intel CPUs require "OpenCL Runtime for Intel Core and Intel Xeon Processors" (16.1.1 or later)
- NVIDIA GPUs require "NVIDIA Driver" (440.64 or later) and "CUDA Toolkit" (9.0 or later)

### Используется для вычисления обезличенного набора библиотека [hashcat](https://hashcat.net/hashcat/)

## Исползования платформы 
 

Платформу можно запустит main.ipynb указав внутри файла путь к таблице хешей. Следует заполнить таблицу, как указано ниже:

| Номер телефона                   | Скоринговый балл |
|----------------------------------|------------------|
| c210baab81dbbfd3a7f43fb869069fe7 | 0,731            |

### После завершения скрипта вы увидите следующий отчет:

```shell
c210baab81dbbfd3a7f43fb869069fe7:94800097383 

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 0 (MD5)
Hash.Target......: md5_list.txt
Time.Started.....: Sat Jul 30 23:10:54 2022 (45 secs)
Time.Estimated...: Sat Jul 30 23:11:39 2022 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Mask.......: ?d?d?d?d?d?d?d?d?d?d?d [11]
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  2183.2 MH/s (0.21ms) @ Accel:256 Loops:125 Thr:32 Vec:1
Recovered........: 494936/494936 (100.00%) Digests
Remaining........: 0 (0.00%) Digests
Recovered/Time...: CUR:N/A,N/A,N/A AVG:N/A,N/A,N/A (Min,Hour,Day)
Progress.........: 100000000000/100000000000 (100.00%)
Rejected.........: 0/100000000000 (0.00%)
Restore.Point....: 99996664/100000000 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:875-1000 Iteration:0-125
Candidate.Engine.: Device Generator
Candidates.#1....: 46833549496 -> 68874949496
Hardware.Mon.#1..: Temp: 52c Fan: 28% Util: 90% Core:1980MHz Mem:5000MHz Bus:16

Started: Sat Jul 30 23:10:51 2022
Stopped: Sat Jul 30 23:11:40 2022
```