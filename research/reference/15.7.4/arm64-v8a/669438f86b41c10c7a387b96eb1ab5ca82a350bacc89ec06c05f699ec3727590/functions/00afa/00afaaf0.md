# 00afaaf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afaaac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaaac.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0008.md#compare-9702e620d9be57dd54ab8d4e0b8dae30)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaaf0",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b243bdf224aa79684abe88f9e57d5aed80b16893bac81fafe27940aa55849ccd",
  "source_text_sha256": "b243bdf224aa79684abe88f9e57d5aed80b16893bac81fafe27940aa55849ccd"
}
~~~

## 呼び出し元

- [00bde970](../00bde/00bde970.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 疑似コード / UTF-8 1385 bytes

~~~c

void _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
               (ulong *param_1,byte *param_2,ulong param_3,ulong param_4)

{
  ulong __n;
  byte bVar1;
  byte *pbVar2;
  void *__dest;
  ulong uVar3;
  
                    /* try { // try from 00afaaf4 to 00bfab13 has its CatchHandler @ 00afff84 */
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  bVar1 = *param_2;
  uVar3 = (ulong)(bVar1 >> 1);
  if ((bVar1 & 1) != 0) {
    uVar3 = *(ulong *)(param_2 + 8);
  }
  if (uVar3 < param_3) {
LAB_00afabac:
                    /* WARNING: Subroutine does not return */
    abort();
  }
  pbVar2 = *(byte **)(param_2 + 0x10);
  if ((bVar1 & 1) == 0) {
    pbVar2 = param_2 + 1;
  }
  __n = uVar3 - param_3;
  if (param_4 <= uVar3 - param_3) {
    __n = param_4;
  }
  if (0xffffffffffffffef < __n) goto LAB_00afabac;
  if (__n < 0x17) {
    __dest = (void *)((long)param_1 + 1);
    *(char *)param_1 = (char)((int)__n << 1);
    if (__n == 0) goto LAB_00afab94;
  }
  else {
    uVar3 = __n + 0x10 & 0xfffffffffffffff0;
    __dest = (void *)_Znwm(uVar3);
    param_1[1] = __n;
    param_1[2] = (ulong)__dest;
    *param_1 = uVar3 | 1;
  }
                    /* try { // try from 00afab8c to 00bfab93 has its CatchHandler @ 00aff560 */
  memcpy(__dest,pbVar2 + param_3,__n);
LAB_00afab94:
  *(undefined1 *)((long)__dest + __n) = 0;
  return;
}

~~~
