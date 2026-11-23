# 00bbada4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bba97c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba97c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0079.md#compare-37e606e25e7f507f17918b94124832e5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0088.md#compare-27bae1336b980350b9b6b971199fd5ec)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbada4",
  "name": "_ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb",
  "size": 320,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d5c6b31e7d262e4b56b923e94305228fdf07f0b619ec44a72b5b09e5ea47ff15",
  "source_text_sha256": "d5c6b31e7d262e4b56b923e94305228fdf07f0b619ec44a72b5b09e5ea47ff15"
}
~~~

## 呼び出し元

- [00c5aae0](../00c5a/00c5aae0.md)

## 呼び出し先

- [00497a48](../00497/00497a48.md)
- [00574cec](../00574/00574cec.md)
- [00bbaf50](../00bba/00bbaf50.md)
- [00c5aca0](../00c5a/00c5aca0.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b080](../00c5b/00c5b080.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 1241 bytes

~~~c

void _ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb(uint param_1)

{
  char cVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  if (DAT_01126360 == 0) {
    DAT_01126400 = 1;
    if ((param_1 & 1) == 0) {
      DAT_01126400 = 2;
    }
  }
  else {
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv(DAT_01126360);
    if (DAT_01126360 == 0) {
      _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
      _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
      if (DAT_01126360 == 0) {
        FUN_00574cec(uVar2,DAT_01126398,DAT_011262c0,param_1 & 1);
        return;
      }
    }
    uVar3 = _ZNK8firebase3App9GetJNIEnvEv(DAT_01126360);
    cVar1 = FUN_00497a48(uVar3,DAT_01126398,DAT_011262b8);
    FUN_00574cec(uVar2,DAT_01126398,DAT_011262c0,param_1 & 1);
    if (cVar1 != '\0') {
      return;
    }
    if (DAT_01126360 == 0) {
      _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
      _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
      if (DAT_01126360 == 0) goto LAB_00bbae7c;
    }
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
    cVar1 = FUN_00497a48(uVar2,DAT_01126398,DAT_011262b8);
    if (cVar1 != '\0') {
LAB_00bbae7c:
      FUN_00bbaf50();
      return;
    }
  }
  return;
}

~~~
