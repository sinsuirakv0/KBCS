# 00c2adec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c2ad50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2ad50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/detail_skipped-0009.md#compare-256c4b1c093a41565af1b2d171e3c649)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/detail_skipped-0010.md#compare-44ed9c047765351be409c267684b39b7)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2adec",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb0EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d77bfa624d821a71994479c7025ea29c0469df005771d99bc12a7936de86213",
  "source_text_sha256": "5d77bfa624d821a71994479c7025ea29c0469df005771d99bc12a7936de86213"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1397 bytes

~~~c

undefined1
_ZNKSt6__ndk115__codecvt_utf16IDsLb0EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_
          (long param_1,undefined8 param_2,byte *param_3,byte *param_4,ulong *param_5,
          ushort *param_6,ushort *param_7,undefined8 *param_8)

{
  ushort uVar1;
  undefined1 uVar2;
  ushort *puVar3;
  ulong uVar4;
  
  if (((1 < (long)param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x18) >> 2 & 1) != 0)) &&
     (*param_3 == 0xfe)) {
    param_3 = param_3 + (ulong)(param_3[1] == 0xff) * 2;
  }
  if (param_3 < param_4 + -1) {
    uVar4 = *(ulong *)(param_1 + 0x10);
    uVar2 = 2;
    puVar3 = param_6;
    while (param_6 = puVar3, puVar3 < param_7) {
                    /* catch() { ... } // from try @ 00c2ad50 with catch @ 00c2ae50 */
      if (((*param_3 & 0xf8) == 0xd8) || (uVar1 = CONCAT11(*param_3,param_3[1]), uVar4 < uVar1))
      goto LAB_00c2ae74;
      param_3 = param_3 + 2;
      param_6 = puVar3 + 1;
      *puVar3 = uVar1;
      puVar3 = param_6;
      if (param_4 + -1 <= param_3) break;
    }
  }
  uVar2 = param_3 < param_4;
LAB_00c2ae74:
  *param_5 = (ulong)param_3;
                    /* try { // try from 00c2ae78 to 00d2af27 has its CatchHandler @ 00c2ae78
                       catch() { ... } // from try @ 00c2ae78 with catch @ 00c2ae78
                       catch() { ... } // from try @ 00c2af3c with catch @ 00c2ae78 */
  *param_8 = param_6;
  return uVar2;
}

~~~
