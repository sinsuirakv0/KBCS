# 007cbdec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `007cbdec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbdec.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "007cbdec",
  "name": "FUN_007cbdec",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "338ebc003d2404e765db11fa30148db2ec61ec5e3869f52ddb48aab775f5519f",
  "source_text_sha256": "338ebc003d2404e765db11fa30148db2ec61ec5e3869f52ddb48aab775f5519f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0044d968](../0044d/0044d968.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)

## 疑似コード / UTF-8 856 bytes

~~~c

undefined8 * FUN_007cbdec(long param_1)

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
  *puVar2 = &PTR_FUN_00bffff8;
  puVar2[1] = uVar1;
  lVar3 = *(long *)(param_1 + 0x18);
  puVar2[2] = 0;
                    /* try { // try from 007cbe2c to 008cbe4f has its CatchHandler @ 007cdafc */
  __n = lVar3 - (long)__src;
  if (__n != 0) {
    if ((long)__n < 0) {
                    /* WARNING: Subroutine does not return */
      FUN_0044d968(puVar2 + 2);
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
