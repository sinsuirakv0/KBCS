# 00bb3dbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb3994`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3994.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/alignment_unresolved-0010.md#compare-58a6c7994b37b0e35852426a1b6b7339)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/high-0010.md#compare-dbf76781ca5da6f4524600fca4090df6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb3dbc",
  "name": "_ZN11flatbuffers18RemoveStringQuotesERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f170a9898a297888ed880b2d84be1525b3f70c0731d73d099936f188c8ac096",
  "source_text_sha256": "0f170a9898a297888ed880b2d84be1525b3f70c0731d73d099936f188c8ac096"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b5b0](../00c5b/00c5b5b0.md)
- [00c5b7f0](../00c5b/00c5b7f0.md)

## 疑似コード / UTF-8 1220 bytes

~~~c

void _ZN11flatbuffers18RemoveStringQuotesERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
               (undefined8 param_1,byte *param_2,undefined8 param_3,undefined8 param_4)

{
  ulong uVar1;
  byte *pbVar2;
  byte bVar3;
  
  uVar1 = *(ulong *)(param_2 + 8);
  pbVar2 = *(byte **)(param_2 + 0x10);
                    /* try { // try from 00bb3dc4 to 00cb3dcb has its CatchHandler @ 00bb4ca0 */
  if ((*param_2 & 1) == 0) {
    pbVar2 = param_2 + 1;
    uVar1 = (ulong)(*param_2 >> 1);
  }
                    /* try { // try from 00bb3de4 to 00cb3df3 has its CatchHandler @ 00bb4a28 */
                    /* try { // try from 00bb3df4 to 00cb3dff has its CatchHandler @ 00bb4a1c */
                    /* try { // try from 00bb3e00 to 00cb3e2f has its CatchHandler @ 00bb31a4 */
  if ((1 < uVar1) &&
     (((bVar3 = *pbVar2, bVar3 == 0x27 || (bVar3 == 0x22)) && (bVar3 == pbVar2[uVar1 - 1])))) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
              (param_1,param_2,1,uVar1 - 2,param_2);
    return;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1,param_2,param_4,uVar1 - 2);
  return;
}

~~~
