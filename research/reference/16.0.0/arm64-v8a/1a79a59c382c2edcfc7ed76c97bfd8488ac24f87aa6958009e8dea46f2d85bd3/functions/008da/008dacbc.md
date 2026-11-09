# 008dacbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "008dacbc",
  "name": "FUN_008dacbc",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a692b6da895fb53ecf53e015d0d6f7e8fb1606f92612c8ee9db4676a74fb3f73",
  "source_text_sha256": "a692b6da895fb53ecf53e015d0d6f7e8fb1606f92612c8ee9db4676a74fb3f73"
}
~~~

## 呼び出し元

- [008d6b44](../008d6/008d6b44.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 406 bytes

~~~c

void FUN_008dacbc(void *param_1)

{
  long *plVar1;
  long *plVar2;
  long lVar3;
  
  plVar1 = *(long **)((long)param_1 + 0x40);
  plVar2 = (long *)((long)param_1 + 0x20);
  if (plVar1 == plVar2) {
    lVar3 = 0x20;
  }
  else {
    if (plVar1 == (long *)0x0) goto LAB_008dacfc;
    lVar3 = 0x28;
    plVar2 = plVar1;
  }
  (**(code **)(*plVar2 + lVar3))();
LAB_008dacfc:
  _ZdlPv(param_1);
  return;
}

~~~
