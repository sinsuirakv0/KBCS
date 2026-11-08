# 007cbdec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

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
  "source_sha256": "57e5ea6438b61251689a00fac8808fb3ffc55f4c7fc9fd7d7dee4278785ceb55",
  "source_text_sha256": "57e5ea6438b61251689a00fac8808fb3ffc55f4c7fc9fd7d7dee4278785ceb55"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0044d968](../0044d/0044d968.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb160](../00bdb/00bdb160.md)

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
  *puVar2 = &PTR_FUN_00bfffa8;
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
