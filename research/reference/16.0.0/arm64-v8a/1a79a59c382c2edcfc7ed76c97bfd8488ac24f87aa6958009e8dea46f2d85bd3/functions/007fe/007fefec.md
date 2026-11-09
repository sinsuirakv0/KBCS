# 007fefec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007fefec",
  "name": "FUN_007fefec",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d7902b653466e6312cd5ef0a5e36f9089a46ac2e1b9a171c54109d46c85c4bf",
  "source_text_sha256": "7d7902b653466e6312cd5ef0a5e36f9089a46ac2e1b9a171c54109d46c85c4bf"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00470800](../00470/00470800.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57c00](../00c57/00c57c00.md)

## 疑似コード / UTF-8 759 bytes

~~~c

undefined8 * FUN_007fefec(long param_1)

{
  undefined8 uVar1;
  void *__src;
  size_t __n;
  undefined8 *puVar2;
  void *__dest;
  long lVar3;
  
  puVar2 = (undefined8 *)_Znwm(0x28);
  uVar1 = *(undefined8 *)(param_1 + 8);
  __src = *(void **)(param_1 + 0x10);
  puVar2[3] = 0;
  puVar2[4] = 0;
  *puVar2 = &PTR_FUN_00c7dc30;
  puVar2[1] = uVar1;
  lVar3 = *(long *)(param_1 + 0x18);
  puVar2[2] = 0;
  __n = lVar3 - (long)__src;
  if (__n != 0) {
    if ((long)__n < 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00470800(puVar2 + 2);
    }
    __dest = (void *)_Znwm(__n);
    puVar2[2] = __dest;
    puVar2[4] = (long)__dest + __n;
    memcpy(__dest,__src,__n);
    puVar2[3] = (long)__dest + __n;
  }
  return puVar2;
}

~~~
