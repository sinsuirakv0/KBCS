# 009fcbec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "009fcbec",
  "name": "FUN_009fcbec",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a4cb2efe8a7bef2312aeba372a99be47dbcc76bb5d350830baf3d083bed68668",
  "source_text_sha256": "a4cb2efe8a7bef2312aeba372a99be47dbcc76bb5d350830baf3d083bed68668"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 527 bytes

~~~c

void FUN_009fcbec(undefined8 *param_1)

{
  long *plVar1;
  long *plVar2;
  long lVar3;
  undefined8 *__ptr;
  
  __ptr = (undefined8 *)*param_1;
  *param_1 = 0;
  if (__ptr == (undefined8 *)0x0) {
    return;
  }
  plVar1 = (long *)__ptr[10];
  plVar2 = __ptr + 6;
  *__ptr = &PTR_FUN_00c8a080;
  if (plVar1 == plVar2) {
    lVar3 = 0x20;
  }
  else {
    if (plVar1 == (long *)0x0) goto LAB_009fcc4c;
    lVar3 = 0x28;
    plVar2 = plVar1;
  }
  (**(code **)(*plVar2 + lVar3))();
LAB_009fcc4c:
  _ZdlPv(__ptr);
  return;
}

~~~
