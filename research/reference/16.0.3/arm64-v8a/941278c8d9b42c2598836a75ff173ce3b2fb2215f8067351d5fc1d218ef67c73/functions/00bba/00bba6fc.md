# 00bba6fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bba6fc",
  "name": "_ZN8firebase9messaging10FileLocker11AcquireLockEPKc",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "79a43928de3cc6f8190f49faebf61e694b1d9f21c7cec90c40fb2935cfeed4d3",
  "source_text_sha256": "79a43928de3cc6f8190f49faebf61e694b1d9f21c7cec90c40fb2935cfeed4d3"
}
~~~

## 呼び出し元

- [00c5e620](../00c5e/00c5e620.md)

## 呼び出し先

- [00c5a870](../00c5a/00c5a870.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bc10](../00c5b/00c5bc10.md)
- [00c5e680](../00c5e/00c5e680.md)
- [00c5e6b0](../00c5e/00c5e6b0.md)

## 疑似コード / UTF-8 397 bytes

~~~c

int _ZN8firebase9messaging10FileLocker11AcquireLockEPKc(char *param_1)

{
  undefined4 uVar1;
  int __fd;
  int iVar2;
  
  if (DAT_01127418 != 0) {
    _ZN8firebase5Mutex7AcquireEv(DAT_01127418);
  }
  uVar1 = __umask_chk(0);
  __fd = open(param_1,0x42,0x1b6);
  __umask_chk(uVar1);
  if ((__fd < 0) || (iVar2 = flock(__fd,2), iVar2 < 0)) {
    close(__fd);
    __fd = -1;
  }
  return __fd;
}

~~~
