"""Copyright (c) 2017 * Keith Cestaro
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


import ctypes


def get_free_space_mb(dirname):
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(
            ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return (free_bytes.value / 1024 / 1024)


def main():
    print("Please in put the name of the drive you want to check the memory \
of (ex: C)")
    driveName = str(input())
    storageSpace1 = get_free_space_mb(driveName + ":\\")
    print("You have " + str(storageSpace1) + " MB of memory left on this drive")
    print("Be careful not to over bloat your target drive")
    print("Please input the number of characters you would like in each file \
as an integer value")
    numChar = int(input())
    print("Please input the number of text files you want to create as \
an integer value")
    numFiles = int(input())
    i = 1
    while i < numFiles + 1:
        q = 1
        lst = []
        while q < numChar + 1:
            lst.append(str(q))
            q += 1
        f = open("file" + str(i) + ".txt", "w+")
        f.write(" ".join(lst))
        i += 1
    storageSpace2 = get_free_space_mb(driveName + ":\\")
    print("You bloated " + str(storageSpace1 - storageSpace2) + " MB of memory")
    print("You now have " + str(storageSpace2) + " MB of memory left on this \
drive")
    print("Thank you for using this bloater!")


main()
