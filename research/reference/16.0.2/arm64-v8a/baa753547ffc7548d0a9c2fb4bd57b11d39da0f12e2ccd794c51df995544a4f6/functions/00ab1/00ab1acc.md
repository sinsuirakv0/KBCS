# 00ab1acc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00ab1acc",
  "name": "FUN_00ab1acc",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c281f86d7d49f813689b6156dc4958a8c00536d4de98d6bb4a50ceac3fedb4f1",
  "source_text_sha256": "c281f86d7d49f813689b6156dc4958a8c00536d4de98d6bb4a50ceac3fedb4f1"
}
~~~

## 呼び出し元

- [00ab1808](../00ab1/00ab1808.md)

## 呼び出し先

- [00ab17a8](../00ab1/00ab17a8.md)
- [00ab17f4](../00ab1/00ab17f4.md)
- [00c53ffc](../00c53/00c53ffc.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c580d0](../00c58/00c580d0.md)

## 疑似コード / UTF-8 1251 bytes

~~~c

void FUN_00ab1acc(long *param_1,long param_2,undefined4 *param_3)

{
  long lVar1;
  undefined4 uVar2;
  size_t __n;
  long lVar3;
  void *__dest;
  undefined8 uVar4;
  void *pvVar5;
  undefined8 *puVar6;
  
  lVar3 = _Znwm(0x40);
  uVar2 = *param_3;
  *param_1 = lVar3;
  param_1[1] = param_2 + 8;
  *(undefined1 *)(param_1 + 2) = 0;
  *(undefined4 *)(lVar3 + 0x20) = uVar2;
  pvVar5 = *(void **)(param_3 + 2);
  lVar1 = *(long *)(param_3 + 4);
  puVar6 = (undefined8 *)(lVar3 + 0x28);
  *puVar6 = 0;
  *(undefined8 *)(lVar3 + 0x30) = 0;
  *(undefined8 *)(lVar3 + 0x38) = 0;
  __n = lVar1 - (long)pvVar5;
  if (__n != 0) {
    if ((long)__n < 0) {
      uVar4 = FUN_00ab17f4(puVar6);
      pvVar5 = (void *)*puVar6;
      if (pvVar5 != (void *)0x0) {
        *(void **)(lVar3 + 0x30) = pvVar5;
        _ZdlPv(pvVar5);
      }
      FUN_00ab17a8(param_1);
                    /* WARNING: Subroutine does not return */
      FUN_00c53ffc(uVar4);
    }
    __dest = (void *)_Znwm(__n);
    *(void **)(lVar3 + 0x28) = __dest;
    *(void **)(lVar3 + 0x30) = __dest;
    *(size_t *)(lVar3 + 0x38) = (long)__dest + __n;
    memcpy(__dest,pvVar5,__n);
    *(size_t *)(lVar3 + 0x30) = (long)__dest + __n;
  }
  *(undefined1 *)(param_1 + 2) = 1;
  return;
}

~~~
