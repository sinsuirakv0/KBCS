# 00c2aebc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2aa94`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2aa94.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/detail_skipped-0008.md#compare-f93dd374b65f744ec78b21fd7b5a433a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/detail_skipped-0010.md#compare-81afe40dfa81dc6660836cb53d2e6e05)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2aebc",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6bfbecd6a714d8d78fe954ecc17786f7620c273afe369330f8a1c6d32bcd7297",
  "source_text_sha256": "6bfbecd6a714d8d78fe954ecc17786f7620c273afe369330f8a1c6d32bcd7297"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1370 bytes

~~~c

undefined8
_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_
          (long param_1,undefined8 param_2,ushort *param_3,ushort *param_4,ulong *param_5,
          undefined2 *param_6,long param_7,undefined8 *param_8)

{
  undefined2 *puVar1;
  ushort uVar2;
  undefined8 uVar3;
  ulong uVar4;
  long lVar5;
  
  uVar4 = *(ulong *)(param_1 + 0x10);
  if ((*(byte *)(param_1 + 0x18) >> 1 & 1) != 0) {
    if (param_7 - (long)param_6 < 2) {
LAB_00c2aed8:
      uVar3 = 1;
      goto LAB_00c2af4c;
    }
    *param_6 = 0xfeff;
    param_6 = param_6 + 1;
  }
  if (param_3 < param_4) {
    lVar5 = param_7 - (long)param_6;
    do {
      uVar2 = *param_3;
      if ((uVar2 & 0xf800) == 0xd800 || uVar4 < uVar2) {
                    /* catch() { ... } // from try @ 00c2b038 with catch @ 00c2af48 */
        uVar3 = 2;
        goto LAB_00c2af4c;
      }
      if (lVar5 < 2) goto LAB_00c2aed8;
      param_3 = param_3 + 1;
      *(char *)param_6 = (char)uVar2;
                    /* catch() { ... } // from try @ 00c2ae8c with catch @ 00c2af20 */
      puVar1 = param_6 + 1;
      *(char *)((long)param_6 + 1) = (char)(uVar2 >> 8);
      param_6 = puVar1;
      lVar5 = lVar5 + -2;
    } while (param_3 < param_4);
    uVar3 = 0;
  }
  else {
    uVar3 = 0;
  }
LAB_00c2af4c:
  *param_5 = (ulong)param_3;
  *param_8 = param_6;
  return uVar3;
}

~~~
