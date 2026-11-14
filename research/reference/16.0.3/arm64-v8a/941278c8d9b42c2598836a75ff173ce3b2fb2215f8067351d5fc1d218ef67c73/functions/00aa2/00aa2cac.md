# 00aa2cac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aa2cac",
  "name": "FUN_00aa2cac",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b7b057f1e0c10301a350a6fcfc70315f8ecda252ce1ebbc4e6d4d6761282a048",
  "source_text_sha256": "b7b057f1e0c10301a350a6fcfc70315f8ecda252ce1ebbc4e6d4d6761282a048"
}
~~~

## 呼び出し元

- [00aa2450](../00aa2/00aa2450.md)
- [00aa2e10](../00aa2/00aa2e10.md)

## 呼び出し先

- [00470ba0](../00470/00470ba0.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c590a0](../00c59/00c590a0.md)

## 疑似コード / UTF-8 1196 bytes

~~~c

void FUN_00aa2cac(long *param_1,long param_2,undefined4 *param_3)

{
  void *__src;
  long lVar1;
  undefined4 uVar2;
  size_t __n;
  long lVar3;
  void *__dest;
  
  lVar3 = _Znwm(0x40);
  uVar2 = *param_3;
  *param_1 = lVar3;
  param_1[1] = param_2 + 8;
  *(undefined1 *)(param_1 + 2) = 0;
  *(undefined4 *)(lVar3 + 0x20) = uVar2;
  __src = *(void **)(param_3 + 2);
  lVar1 = *(long *)(param_3 + 4);
  *(undefined8 *)(lVar3 + 0x28) = 0;
  *(undefined8 *)(lVar3 + 0x30) = 0;
  *(undefined8 *)(lVar3 + 0x38) = 0;
  __n = lVar1 - (long)__src;
  if (__n != 0) {
    if ((long)__n < 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00470ba0((undefined8 *)(lVar3 + 0x28));
    }
    __dest = (void *)_Znwm(__n);
                    /* try { // try from 00aa2d10 to 00ba2d13 has its CatchHandler @ 00aa3a98 */
                    /* try { // try from 00aa2d14 to 00ba2e37 has its CatchHandler @ 00aa2600 */
    *(void **)(lVar3 + 0x28) = __dest;
    *(void **)(lVar3 + 0x30) = __dest;
    *(size_t *)(lVar3 + 0x38) = (long)__dest + __n;
    memcpy(__dest,__src,__n);
    *(size_t *)(lVar3 + 0x30) = (long)__dest + __n;
  }
  *(undefined1 *)(param_1 + 2) = 1;
  return;
}

~~~
