# 009fcddc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "009fcddc",
  "name": "FUN_009fcddc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1abc089b7310ec21c02925dd36ac809594745dec513a8177a4fa3fee3ec23063",
  "source_text_sha256": "1abc089b7310ec21c02925dd36ac809594745dec513a8177a4fa3fee3ec23063"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 527 bytes

~~~c

void FUN_009fcddc(undefined8 *param_1)

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
  *__ptr = &PTR_FUN_00c8a550;
  if (plVar1 == plVar2) {
    lVar3 = 0x20;
  }
  else {
    if (plVar1 == (long *)0x0) goto LAB_009fce3c;
    lVar3 = 0x28;
    plVar2 = plVar1;
  }
  (**(code **)(*plVar2 + lVar3))();
LAB_009fce3c:
  _ZdlPv(__ptr);
  return;
}

~~~
