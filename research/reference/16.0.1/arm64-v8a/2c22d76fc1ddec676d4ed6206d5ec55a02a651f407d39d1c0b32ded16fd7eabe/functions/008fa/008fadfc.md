# 008fadfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `008fac60`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fac60.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0051.md#compare-364594fad21cffd0c7c47e7ed2784b23)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0055.md#compare-520f1057f99952ca5dd10c841d4fa6aa)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008fadfc",
  "name": "FUN_008fadfc",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a815ecb14940f02f45c1ccf1d13add7fe49446796991160ef7f69f2bb3fa9def",
  "source_text_sha256": "a815ecb14940f02f45c1ccf1d13add7fe49446796991160ef7f69f2bb3fa9def"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008514f8](../00851/008514f8.md)
- [008b9178](../008b9/008b9178.md)

## 疑似コード / UTF-8 611 bytes

~~~c

void FUN_008fadfc(undefined8 param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  long lVar2;
  undefined8 uVar3;
  
                    /* try { // try from 008fae04 to 009fae27 has its CatchHandler @ 008fae8c */
  if ((*param_3 == 2) && (*param_4 == 0)) {
    uVar3 = *param_2;
    uVar1 = FUN_0047acf4();
                    /* try { // try from 008fae28 to 009faf13 has its CatchHandler @ 008fa990 */
    FUN_0047cdd4(uVar1,0xb,0);
    lVar2 = FUN_008514f8();
    *(uint *)(lVar2 + 0x4a844) = *(uint *)(lVar2 + 0x4a844) | 8;
    FUN_008b9178(uVar3);
    return;
  }
  return;
}

~~~
