# 006dfafc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `006b5d40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5d40.md) · 移動量 `+0x29dbc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0030.md#compare-d85ccdff9ba1cde053364e622b040c75)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006dfafc",
  "name": "FUN_006dfafc",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "794589466efc653df72ecff127872efd03fccb0b08fc3de3485f0f8373dfc0a6",
  "source_text_sha256": "794589466efc653df72ecff127872efd03fccb0b08fc3de3485f0f8373dfc0a6"
}
~~~

## 呼び出し元

- [006f2494](../006f2/006f2494.md)
- [00716d50](../00716/00716d50.md)
- [008c5c08](../008c5/008c5c08.md)
- [009470d0](../00947/009470d0.md)
- [009d0184](../009d0/009d0184.md)
- [00aeab6c](../00aea/00aeab6c.md)

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [00470800](../00470/00470800.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57c00](../00c57/00c57c00.md)

## 疑似コード / UTF-8 1392 bytes

~~~c

void FUN_006dfafc(undefined8 *param_1,undefined4 *param_2)

{
  ulong uVar1;
  undefined4 *puVar2;
  undefined4 *puVar3;
  void *__dest;
  ulong uVar4;
  ulong uVar5;
  void *__src;
  long lVar6;
  undefined4 *puVar7;
  
  puVar3 = (undefined4 *)param_1[1];
  if (puVar3 < (undefined4 *)param_1[2]) {
    puVar7 = puVar3 + 1;
    *puVar3 = *param_2;
  }
  else {
    __src = (void *)*param_1;
    lVar6 = (long)puVar3 - (long)__src >> 2;
    uVar1 = lVar6 + 1;
    if (uVar1 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00470800(param_1);
    }
    uVar4 = (long)param_1[2] - (long)__src;
    uVar5 = (long)uVar4 >> 1;
    if (uVar5 <= uVar1) {
      uVar5 = uVar1;
    }
    if (0x7ffffffffffffffb < uVar4) {
      uVar5 = 0x3fffffffffffffff;
    }
    if (uVar5 == 0) {
      __dest = (void *)0x0;
    }
    else {
      if (uVar5 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
        FUN_00440e80();
      }
      __dest = (void *)_Znwm(uVar5 << 2);
    }
    puVar2 = (undefined4 *)((long)__dest + lVar6 * 4);
    puVar7 = puVar2 + 1;
    *puVar2 = *param_2;
    memcpy(__dest,__src,(long)puVar3 - (long)__src);
    *param_1 = __dest;
    param_1[1] = puVar7;
    param_1[2] = (void *)((long)__dest + uVar5 * 4);
    if (__src != (void *)0x0) {
      _ZdlPv(__src);
    }
  }
  param_1[1] = puVar7;
  return;
}

~~~
