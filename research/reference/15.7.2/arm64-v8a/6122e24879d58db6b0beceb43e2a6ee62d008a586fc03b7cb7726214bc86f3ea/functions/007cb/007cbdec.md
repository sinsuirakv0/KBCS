# 007cbdec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007cbdec.md)

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
  "source_sha256": "2ddd754c6ac3339e2af45f5f6ac963d2d7151b11815bb8606e72fe1a1b93d032",
  "source_text_sha256": "2ddd754c6ac3339e2af45f5f6ac963d2d7151b11815bb8606e72fe1a1b93d032"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0044d968](../0044d/0044d968.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)

## 疑似コード 1/1 / UTF-8 883 bytes

~~~c

undefined8 * FUN_007cbdec(long param_1)

{
  undefined8 uVar1;
  void *__src;
  ulong __n;
  undefined8 *puVar2;
  void *__dest;
  long lVar3;
  
  puVar2 = operator_new(0x28);
  uVar1 = *(undefined8 *)(param_1 + 8);
  __src = *(void **)(param_1 + 0x10);
  puVar2[3] = 0;
  puVar2[4] = 0;
  *puVar2 = &PTR_FUN_00bffef8;
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
    __dest = operator_new(__n);
    puVar2[2] = __dest;
    puVar2[4] = (long)__dest + __n;
    memcpy(__dest,__src,__n);
    puVar2[3] = (long)__dest + __n;
  }
  return puVar2;
}

~~~
