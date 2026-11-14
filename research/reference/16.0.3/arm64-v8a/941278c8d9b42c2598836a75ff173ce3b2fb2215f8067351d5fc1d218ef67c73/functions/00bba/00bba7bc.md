# 00bba7bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bba7bc",
  "name": "_ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b1268573302aa97b31519529f640bfd602ae5786282f20d538ac27912d28e028",
  "source_text_sha256": "b1268573302aa97b31519529f640bfd602ae5786282f20d538ac27912d28e028"
}
~~~

## 呼び出し元

- [00c5e390](../00c5e/00c5e390.md)

## 呼び出し先

- [00c5a870](../00c5a/00c5a870.md)
- [00c5b0a0](../00c5b/00c5b0a0.md)
- [00c5b130](../00c5b/00c5b130.md)
- [00c5b300](../00c5b/00c5b300.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5e620](../00c5e/00c5e620.md)

## 疑似コード / UTF-8 1248 bytes

~~~c

ulong _ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE(ulong param_1)

{
  int __fd;
  uint uVar1;
  byte *__filename;
  FILE *__stream;
  byte *__filename_00;
  
  if ((param_1 != 0) && (DAT_01127420 != 0)) {
    if ((*DAT_01127450 & 1) == 0) {
      __filename_00 = DAT_01127450 + 1;
    }
    else {
      __filename_00 = *(byte **)(DAT_01127450 + 0x10);
    }
    __fd = _ZN8firebase9messaging10FileLocker11AcquireLockEPKc(__filename_00);
    if ((*DAT_01127428 & 1) == 0) {
      __filename = DAT_01127428 + 1;
                    /* try { // try from 00bba814 to 00cba9ff has its CatchHandler @ 00bba814
                       catch() { ... } // from try @ 00bba814 with catch @ 00bba814
                       catch() { ... } // from try @ 00bbaa30 with catch @ 00bba814 */
    }
    else {
      __filename = *(byte **)(DAT_01127428 + 0x10);
    }
    __stream = fopen((char *)__filename,"a");
    param_1 = 0;
    if (__stream != (FILE *)0x0) {
      uVar1 = fclose(__stream);
      param_1 = (ulong)uVar1;
    }
    if (-1 < __fd) {
      remove((char *)__filename_00);
      close(__fd);
      param_1 = 0;
      if (DAT_01127418 != 0) {
        param_1 = _ZN8firebase5Mutex7ReleaseEv();
      }
    }
  }
  return param_1;
}

~~~
