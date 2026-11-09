# 007afcdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007afcdc",
  "name": "FUN_007afcdc",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f47577fac5f00ce324f62d22771ffe5cba2b7d0af4213df029d1700e3f4a6bf5",
  "source_text_sha256": "f47577fac5f00ce324f62d22771ffe5cba2b7d0af4213df029d1700e3f4a6bf5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)

## 疑似コード / UTF-8 524 bytes

~~~c

undefined8 * FUN_007afcdc(long param_1)

{
  undefined8 *puVar1;
  long *plVar2;
  undefined8 uVar3;
  long lVar4;
  
  puVar1 = (undefined8 *)_Znwm(0x40);
  plVar2 = *(long **)(param_1 + 0x30);
  *puVar1 = &PTR_FUN_00c7a618;
  uVar3 = 0;
  if (plVar2 != (long *)0x0) {
    if (plVar2 == (long *)(param_1 + 0x10)) {
      lVar4 = *plVar2;
      puVar1[6] = puVar1 + 2;
      (**(code **)(lVar4 + 0x18))();
      return puVar1;
    }
    uVar3 = (**(code **)(*plVar2 + 0x10))();
  }
  puVar1[6] = uVar3;
  return puVar1;
}

~~~
